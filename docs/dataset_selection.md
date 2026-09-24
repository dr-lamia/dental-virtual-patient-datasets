# Dataset Selection Guide

## If the task is...

- **Build a controllable dynamic face:** start with NeRSemble.
- **Test facial geometry across many identities/expressions:** use FaceScape.
- **Test speech animation:** use VOCASET first; BIWI as a second benchmark.
- **Test multi-view dynamic reconstruction:** use MultiFace.
- **Segment individual teeth from IOS:** use 3DTeethSeg / Teeth3DS.
- **Register IOS with CBCT:** use the paired CBCT + oral-scan Figshare dataset.
- **Segment craniofacial anatomy from CBCT:** use ToothFairy2.

## Recommended MVP sequence

1. Public face dataset for avatar code sanity checks.
2. One de-identified real patient facial video.
3. The same patient's upper/lower IOS + bite.
4. One CAD smile-design mesh.
5. Registration + render original/design on identical facial motion.
