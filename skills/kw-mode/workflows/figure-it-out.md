# Figure it out

When no narrow playbook fits, design the workflow before committing to an approach.

1. State a falsifiable definition of done, the bounded scope, and material unknowns.
2. Establish a baseline and the checks that will distinguish success from failure.
   Resolve the riskiest unknown before building dependent pieces.
3. Decompose into independently verifiable units using [sequence verifiable units](../principles/sequence-verifiable-units.md).
   Use [architect](architect.md) for open design choices and [swarm](swarm.md) only
   across separable ownership boundaries.
4. Execute each unit as an experiment: hypothesis, change, observation, accept or
   revise. Preserve unrelated work when discarding an unsuccessful attempt.
5. Keep a [decision trail](show-me-your-work.md), then [verify](verify.md) the whole
   result. Stop at the requested deliverable. Report genuine blockers precisely;
   do not silently weaken the acceptance condition.
