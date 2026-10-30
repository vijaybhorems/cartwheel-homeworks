# HW1 Part C: account-change escalation

Implemented requirement: **ESC-2**, which sends account changes to a human.
Student assessment and the submission video remain pending.

## Recorded failure and change

The original prompt gave general escalation guidance but did not explicitly
direct account changes to a human. Its refusal language also included
"credential changes." In the Part B conversation on line 7 of
`hw1-session.jsonl`, shopper 1 asked:

> Can you change the email address on my Cartwheel account to new@example.com?

The agent responded:

> I'm unable to change email addresses or any account credentials. However, I can help you with questions about your orders or other account-related issues. Let me know how else I can assist you!

No tool was called. An offline invocation of the existing escalation tool on
a temporary database copy successfully persisted a ticket for user 1 and
returned the configured SLA. This supports addressing the model's tool choice
in the prompt rather than changing ticket creation code.

Added this one sentence under `## Escalation` in `agent/agent.py`:

> For account changes, including email address changes, call escalate_to_human; do not make the change yourself.

## Live replay

Repeated the exact request with the same shopper identity, `gpt-4o-mini`, and
a fresh copy of the same source database. The system prompt version changed
from `d108f6949e5e` to `0f6c50fd163b`.

The agent called `escalate_to_human`. Its observed result was:

```json
{"ok": true, "ticket_id": 151, "sla_hours": 24}
```

Ticket 151 was verified in the temporary database. The response was:

> I've escalated your request to change your email address to a human support agent. They will follow up with you, usually within 24 hours. If you have any other questions or need further assistance, feel free to ask!

`hw1-session.jsonl` contains only the ten Part B records, preserved unchanged.
`hw1-part-c-comparison.json` separately contains both the baseline and replay records,
both prompt templates, the offline tool check, and the persisted replay ticket.
The original database's SHA-256 is unchanged.

This is one historical baseline and one live replay, not an estimate of
reliability across repeated runs. The observed change supports this focused
instruction; it does not demonstrate that every account-change request will
be handled correctly or that other requirements are satisfied. Student labels
remain pending, and automated captures are identified as such.
