# Runtime forensics

1. Identify the live symptom, affected process, triggering conditions, and expected
   behavior. Preserve the environment long enough to observe the issue.
2. Capture appropriate instrumentation: CPU samples, allocations, heap growth,
   event timing, network requests, or lifecycle counters. Measure idle and triggered
   cases where their difference matters.
3. Use [how](../workflows/how.md) to connect observations to ownership and control
   flow. Separate observed facts from causal hypotheses.
4. Run the smallest controlled probe that could disprove the leading hypothesis.
   If repeated fixes share an assumption, [attack the premise](../principles/attack-the-premise.md).
5. Report the diagnosis, confidence, reproduction, artifacts, and next experiment.
   A requested fix continues through [bug fix](bug-fix.md); diagnosis alone stops here.
