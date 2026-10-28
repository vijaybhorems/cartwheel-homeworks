import asyncio

import pytest
from fastapi import HTTPException

from server import app as server_app


@pytest.fixture
def isolated_sessions(world, tmp_path, monkeypatch):
    monkeypatch.setattr(server_app, "_SESSIONS", {})
    monkeypatch.setattr(
        server_app, "SESSIONS_DB", tmp_path / "sessions.db"
    )


def test_session_rejects_role_mismatch(isolated_sessions):
    with pytest.raises(HTTPException) as caught:
        server_app.create_session(
            server_app.SessionCreate(user_id=1, role="support")
        )

    assert caught.value.status_code == 403
    assert server_app._SESSIONS == {}


def test_token_cannot_authorize_another_session(
    isolated_sessions, monkeypatch
):
    first = server_app.create_session(
        server_app.SessionCreate(user_id=1, role="shopper")
    )
    second = server_app.create_session(
        server_app.SessionCreate(user_id=1, role="shopper")
    )

    def unexpected_agent(*args, **kwargs):
        pytest.fail("The agent must not run for an unauthorized request")

    monkeypatch.setattr(server_app, "build_agent", unexpected_agent)

    with pytest.raises(HTTPException) as caught:
        asyncio.run(server_app.post_message(
            second["session_id"],
            server_app.MessageIn(message="Show my recent orders."),
            authorization=f"Bearer {first['token']}",
        ))

    assert caught.value.status_code == 403
