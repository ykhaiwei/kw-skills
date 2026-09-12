# Architect

For an explicit “grill me” request, investigate available facts, then put the
consequential assumptions and choices to the user for discussion. Include your
recommendation and tradeoff, and let answers determine the next questions.
The user is the discussion partner; there need not be an implementing agent.
Use [review's challenge guidance](review.md#challenge-the-reasoning) and the steps
below where relevant. Stay in discussion until implementation is requested.

1. Ground the change with [how](how.md), and [why](why.md) when changing ownership
   or layering. State the behavior and constraints the design must preserve.
2. Sketch the caller's usage before implementation: types, signatures, ownership,
   transitions, and module boundaries. Read [foundational thinking](../principles/foundational-thinking.md)
   and [model the domain](../principles/model-the-domain.md).
3. For a consequential choice with no established local pattern, compare at least
   two structurally distinct candidates using [arena](arena.md). For a settled
   mechanical change, follow the existing shape without another design exercise.
4. Choose using the consumer's needs, interface depth, state ownership, and
   [reader load](../principles/minimize-reader-load.md). Avoid wrappers that merely
   move complexity to the caller. Record the tradeoff that could change the choice.
   Before implementing a consequential choice, apply
   [review's challenge guidance](review.md#challenge-the-reasoning) yourself.
   This adds no reviewer dispatch; settled routine choices need no interview.
5. If implementation is authorized, implement against the chosen shape. A request
   for design or discussion ends with the design. If the code disproves an
   assumption, revise the design rather than accumulating compensating layers.
