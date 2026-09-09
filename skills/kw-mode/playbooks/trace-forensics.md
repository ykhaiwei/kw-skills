# Trace forensics

1. Identify the artifact format, capture conditions, time range, and sampling
   limits. Preserve the original and work on a derived analysis.
2. Parse with tools appropriate to the actual format. Locate dominant stacks,
   allocation retainers, long tasks, or timing gaps relevant to the question.
3. Distinguish inclusive from self cost and correlation from causation. Ground
   relevant frames in source using [how](../workflows/how.md).
4. Produce a rerunnable extraction or query for material findings using
   [build the lever](../principles/build-the-lever.md).
5. Explain the diagnosis, evidence, capture limitations, and what a fresh runtime
   probe would resolve. Route an authorized fix to [bug fix](bug-fix.md) or
   [performance](perf-issue.md).
