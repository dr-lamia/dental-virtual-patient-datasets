# Dataset Selection Guide

## If the task is...

- **Build a controllable dynamic face:** start with NeRSemble.
- **Test facial geometry across many identities/expressions:** use FaceScape.
- **Test speech animation:** use VOCASET first; BIWI as a second benchmark.
- **Test multi-view dynamic reconstruction:** use MultiFace.
- **Segment individual teeth from IOS:** use 3DTeethSeg / Teeth3DS.
- **Register IOS with CBCT:** use the paired CBCT + oral-scan Figshare dataset.
- **Segment craniofacial anatomy from CBCT:** use ToothFairy2.
- **Study clinical mandibular kinematics:** use the 90-subject CADIAX/Mendeley dataset.
- **Study TMD condylar path and lateral guidance:** use the 24-patient Dryad dataset.
- **Prototype jaw-motion sensing/trajectory reconstruction:** use the Figshare magnetic-sensor dataset.
- **Build an open optical jaw-tracking pipeline:** evaluate JawTrackingSystem.

## Important distinction

The jaw-motion datasets above are **partial 4D resources**. They do not provide, for the same subjects, a complete synchronized set of facial dynamics + IOS + bite + CBCT + jaw trajectory. They are appropriate for module development, algorithm testing and external validation, but should not be merged across unrelated people and represented as a single 4D patient.

## Recommended MVP sequence

1. Public face dataset for avatar code sanity checks.
2. Public dental mesh/CBCT datasets for dental geometry and registration.
3. Public jaw-motion resources for motion-model and trajectory-processing development.
4. One de-identified real patient facial video.
5. The **same patient's** upper/lower IOS + bite.
6. The same patient's jaw-motion recording.
7. One CAD smile-design mesh.
8. Registration + render original/design on identical facial and mandibular motion.

See `jaw_motion_resources.md` for details.
