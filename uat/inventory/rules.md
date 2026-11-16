# Exercise rules

- Interview mode: on
- Working notes location: `.platoon/`
- Exercise scope: Synthetic brief and local exercise files. Keep the reviewer checker outside the exercise.

## Interview policy

| Item | Permission or requirement |
| --- | --- |
| AI tools and models | Codex or another coding assistant selected by the participant |
| Prepared prompts, external tooling, and code agents | Platoon prompts, editor, and local shell allowed. The participant approves each Builder step. |
| Brief and repository access by the selected model | The synthetic brief and local exercise files may be shared with the selected assistant. |
| Local working files and notes for discussion | Keep notes in `.platoon/` and retain them for discussion. |
| AI disclosure | Participant-confirmed summary in the submission README covering material assistance and what the participant verified. |

- Policy source: `.platoon/brief.md`
- Human clearance for the intended workflow: pending

## Deliverables and commands

- Required deliverables: `stock.py`, `README.md` with AI-use disclosure, and any tests written
- Submission: Record the deliverable paths and submission time locally. Exclude `.platoon/`.
- Stack and working directory: Python 3 standard library, run from the exercise folder
- Setup: Check `python --version`
- Run: `python stock.py INPUT.csv`
- Check: Reproduce the brief's example and record the agreed test commands or manual checks in the plan.
- Final submission check: Run agreed checks, inspect the exact submitted paths, and confirm the disclosure.

## Timing

- Start time and time zone: [fill in at kickoff]
- Submission deadline: [start plus two hours]
- Protected finalization reserve begins: [15 minutes before the submission deadline]
- Initial Scout limit: [suggest 10 minutes, confirm at kickoff]
- Clock source: [local clock or participant checkpoints]
- Separate discussion preparation window: [confirm if available]

| Role | Human-confirmed limit |
| --- | --- |
| Scout | [confirm at kickoff] |
| Spy | [limit or skipped] |
| Builder | [limit] |
| Review | [limit] |
| Defender | [limit and window] |
