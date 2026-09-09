# How

Trace the behavior from its entry point through state changes, side effects, and
the user-visible result. Read callers and consumers as well as the named module.
Use [model the domain](../principles/model-the-domain.md) to describe the shape.

For a narrow question, read and explain directly. For a subsystem with independent
areas, split exploration under the [runtime contract](../runtime.md), then verify
the joins yourself. Do not substitute parallel summaries for a traced call path.

Explain the key concepts, ownership, data flow, and non-obvious failure or lifecycle
conditions. Cite actual paths and symbols. Separate what source shows from what
you observed at runtime. Recover historical intent through [why](why.md).
