# Inventory ledger UAT

This two-hour mock tests Platoon on a synthetic Python CLI assignment. Use this guide and the checker outside the exercise folder. The participant works from the original brief and creates the implementation during the run.

## Start the run

1. Put [brief.md](brief.md) and [rules.md](rules.md) at the root of the exercise's `.platoon/` folder. In the prepared UAT folder, prompts are under `.platoon/roles/` and the remaining template files are under `.platoon/templates/`. Copy each working template to `.platoon/` as needed.
2. For the interview mock, confirm the policy in `.platoon/rules.md` and mark human clearance as `cleared`. For a benchmark run, set `Interview mode: off`. Fill in the absolute start, reserve, deadline, and Scout stop times, then open `C:\src\platoon-uat` in a fresh local chat. Start the clock when ready to begin the exercise.
3. Paste `.platoon/roles/scout.md` and point Scout to `.platoon/rules.md` and `.platoon/brief.md`. Confirm the plan, Spy decision, role limits, and cut line. Approve each bounded Builder step before edits.
4. After a usable Builder step, pause and save `resume.md`. Start a fresh chat for Builder and check that the next action and approval status can be recovered from the files. Run Review in a separate fresh chat with the brief, code, tests, and observed results. Record any limitation or expired role and the handoff it produced.
5. At the reserve, finish the agreed checks and mark the exact deliverables ready. Record the local submission time and confirm the AI-use disclosure. Run Defender within the agreed preparation window and have the participant answer from memory.

## Check the submission

Run the black-box checker from outside the exercise folder once the submission is marked ready.

```powershell
python 'C:\src\platoon\uat\inventory\check.py' 'C:\src\platoon-uat'
```

Record its score along with manual checks of the README, disclosed AI use, and submitted files. Compare any failure with the original brief.

## Record the outcome

| Evidence | Record during the run |
| --- | --- |
| Timing | Start, first working result, reserve start, submission time, and deadline |
| Scope and approvals | Spy choice and reason, Builder approvals, and work dropped or deferred |
| Verification | Commands and actual results, checker score, and unresolved defects |
| Handoffs | Fresh Review, files-only resume result, and any clock-triggered stop |
| Overhead | Approximate participant time spent approving, switching chats, and maintaining notes |
| Submission | Exact paths and participant-confirmed disclosure |
| Discussion | What the participant could explain from memory and gaps to revisit |

If the timed run does not exercise a role expiry or the other Spy choice, record that and use a short separate check after the run.
