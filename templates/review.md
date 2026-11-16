# Review

- Scope: [code, diff, or submission reviewed]
- Context: [fresh, or limitation and reason]
- Evidence: [original brief reference, checks and observed results, and anything unverified]

## Findings

Rank material defects first. Cite the requirement and where the behavior occurs. Mark a check as unverified if it has no observed result.

| Severity | Finding and evidence | Estimated fix cost | Human disposition |
| --- | --- | --- | --- |
| [blocking / major / minor] | [file or check, behavior, and impact] | [minutes or scope] | [pending / fix / defer, with reason if relevant] |

## Likely interview questions

Choose three to five questions. Adapt these examples to specific requirements, code paths, tests, or findings from this review.

- Walk me through what happens from [representative input] to [observable result]. Where is the key rule enforced?
- What happens when [specific edge case] occurs? What does the caller see, and what state is left behind?
- Why did you choose [data structure or design]? What tradeoff does it make under the assignment's constraints?
- Which test would catch [plausible regression]? What behavior still needs a check?
- If you had another 30 minutes, which known limitation would you address first and why?
- Where did AI help, and how did you verify the code or tests it contributed?
