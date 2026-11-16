# Platoon

Platoon helps you finish a technical interview exercise, verify the result, and explain your work and AI use. You choose the roles, approve the work, and submit it. The prompts guide the session. You control permissions and the clock.

## New to AI coding tools?

An AI coding assistant takes instructions in a chat. If it has access to your project folder, it can usually read files, propose or make edits, and run commands. A **prompt** is the message you give it. Each Platoon role is a ready-to-paste prompt for one part of the exercise.

Once you've set up the exercise below, open its folder in your coding tool and start a new chat. Open the Scout prompt, copy the whole file into the chat, and add a line showing where your working files are, such as “Use `.platoon/rules.md` and `.platoon/brief.md`.” Scout should return a plan for you to review. When you reach Builder, read its proposed change and the checks it plans to run before you approve that step. If the proposal is unclear, ask it to explain. After it makes the change, inspect the edits and check results before moving on.

If your assistant only has a chat box, paste the excerpts it may read. Apply its suggested edits and run commands yourself, then share the results.

## Set up the exercise

1. Choose which interview mode to record in `rules.md`.
   - **`Interview mode: on`** is the default. For interviews, check the policy yourself before opening the exercise in an assistant. Record which tools, prepared prompts, and files are allowed, then mark human clearance as `cleared`. Ask the interviewer about material uncertainties when possible. Each role uses that record to proceed.
   - **`Interview mode: off`** is for benchmarks or practice exercises with material you may share. You can leave the interview policy section blank. Record any benchmark limits in `rules.md`. Builder still asks you to approve each implementation step.
2. If custom files are allowed, copy this `core/` folder into the exercise as `.platoon/core/`. Copy the [templates](templates/) you need into `.platoon/` and fill in `rules.md` and `brief.md`. Keep the original brief or a permitted reference to it. If exercise-local files are forbidden, keep the working notes in a permitted location or maintain them yourself. Give the assistant only permitted inputs and tell it where to find or return each artifact.
3. Record the deadline with its time zone, the start of the finalization reserve, and an initial Scout limit. Reserve roughly 10–15 minutes for finalization in a two-hour build. Roles check an available clock and read the approved timing in `rules.md`. Supply any timing details they cannot determine. Unused time returns to the pool. You can reallocate it within the deadline and reserve.

## Run the roles

Paste the full prompt for the active role into your selected assistant and point it to the working files.

1. [Scout](roles/scout.md) proposes the scope, acceptance checks, cut line, remaining role limits, and whether to use Spy. Confirm the plan and record the approved limits in `rules.md` and the Spy choice in `decisions.md`.
2. [Spy](roles/spy.md) is optional. Use it for a few high-value tests or manual checks. Confirm any changes to acceptance expectations.
3. [Builder](roles/builder.md) proposes one bounded change and its checks at a time. Approve one step, review its results, then approve the next. Reapprove changes to scope, tests, or acceptance expectations. Confirm decision entries and AI attribution before appending them to `decisions.md`.
4. [Review](roles/review.md) uses the original brief, code, diff, tests, and observed results. Start a fresh context when practical. Decide which findings to fix or defer. Route fixes through Builder as bounded steps.
5. **Finalization** is yours. At the reserve, stop optional work and take over any unfinished work or active commands. Run final checks, inspect the exact files to be submitted, confirm any required AI disclosure, and submit before the deadline. Keep `.platoon/` out of the submission by default unless the assignment requires or allows it.
6. [Defender](roles/defender.md) rehearses your explanation. Use a short session before submission if time permits, or use an allowed preparation window after submission.

When pausing, update `resume.md` with the current state and next action. In a fresh chat, give the active role `resume.md` and the other permitted working files. Update `rules.md` if timing or exercise scope has changed.
