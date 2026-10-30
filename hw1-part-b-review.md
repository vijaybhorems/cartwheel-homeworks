# HW1 Part B: conversation review

Status: ten live conversations captured in `hw1-session.jsonl` using
`gpt-4o-mini`; student review and manual interaction remain pending.
These ten Part B records used the original system prompt. The Part C replay is
saved separately in `hw1-part-c-comparison.json`; see `hw1-part-c.md` for details.

Each conversation used a fresh copy of the existing Cartwheel database.
The original database's SHA-256 was verified unchanged after the runs.
Tracing was disabled; tool arguments and results were captured directly from
the SDK run items. All responses and tool results are observed output, not
reconstructed examples. Capture method, model, prompt version, timestamp, and
source database hash are included in each record.

The ten selected requests are in `hw1-part-b-cases.json`. They cover the seven
specified cases and the three additional cases selected by the student:
cancellation of delivered order 4127, support access to order 4127, and a
merchant's recent store orders. Expected behaviors and requirement references
are proposed review aids; the student should confirm them against `SPEC.md`.

## Student review

Examine each of the ten lines of `hw1-session.jsonl` alongside `SPEC.md` for Part B:

1. Read the request, authenticated identity, actual tool calls/results, and response.
2. Confirm or revise `expected` and `requirement`.
3. Set `met_requirement` to `true` or `false` based on the observed behavior.
4. Set `problem_source` to `null` for success, or `prompt`, `tool`, or
   `specification` for a failure, using the handout's definitions.
5. Change `review_status` to `reviewed_by_student` when the assessment is complete.

Until reviewed, `met_requirement: null` is an intentional pending marker rather
than a completed homework label. A pending `problem_source: null` is not a
judgment that the case succeeded. The file is not submission-ready until all
ten assessments are completed.

Live runs use the same agent and authenticated identity resolver as the CLI,
with one independent conversation per request. Automated captures must not be
represented as student-conducted manual sessions. The student should personally
examine the conversations and use `uv run python -m agent.cli --role ROLE --user
USER_ID --debug` for the assignment's manual interaction requirement.

Do not revise the system prompt as part of this review; that is Part C. The
student's video recording is also pending and is not produced by this capture.
