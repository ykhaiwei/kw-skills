# Visual parity

1. Pin reference and candidate states: viewport, scale, fonts, data, theme, scroll,
   and interaction state. Make captures reproducible.
2. Capture both surfaces and compare with an image diff or overlay. Separate
   rendering noise from geometry, typography, color, and behavior differences.
3. Trace the cause and make a focused change. Do not hide differences by changing
   the reference, acceptance region, or threshold without agreement.
4. Repeat captures under the same conditions and drive the relevant interactions.
   Use [verify](../workflows/verify.md); a static image does not prove behavior.
5. Report the measured difference, evidence paths, remaining deviations, and
   authorized delivery. If exact parity cannot be established, state that plainly.
