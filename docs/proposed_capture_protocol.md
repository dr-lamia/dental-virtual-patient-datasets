# Proposed Capture Protocol for a 4D Dental Virtual Patient Dataset

## Core same-patient 4D capture

1. **Facial video**: 30–60 seconds, stable illumination, neutral background and fixed camera parameters when possible.
2. **Expressions**: rest, social smile, maximum smile, lip purse, cheek puff and mouth opening/closing.
3. **Head motion**: slow left/right rotation and slight up/down movement.
4. **Speech**: predefined short phrases containing labial, dental and sibilant phonemes.
5. **Dental scans**: upper IOS, lower IOS and buccal bite scan.
6. **Jaw motion**: synchronized or time-alignable recording of opening/closing, protrusion/retrusion and right/left lateral excursion. A validated optical or video-marker workflow may be used.
7. **Design mesh**: original dentition plus proposed smile/restorative STL/PLY.

## Optional advanced capture

- CBCT **only when clinically indicated**
- calibrated 3D facial scan
- dedicated optical jaw tracker / axiograph
- color-calibrated dental photography
- repeated follow-up capture for longitudinal 4D analysis

## Minimum synchronization metadata

For every dynamic stream, record:

- acquisition date/time
- frame rate or sampling frequency
- coordinate-system definition
- calibration procedure
- start/end event markers
- movement/task label
- file units
- device/model/software version

The facial stream and jaw-motion stream should contain a shared visible or instructed synchronization event (for example a distinct opening/closing cue) so trajectories can be temporally aligned.

## Suggested movement protocol

Record at least three repetitions of:

1. maximum opening and closing
2. protrusion and retrusion
3. right lateral excursion
4. left lateral excursion
5. natural smile to maximum smile
6. standardized speech segment

## Privacy and ethics

Facial video and 3D face geometry are identifiable biometric data. Obtain specific consent, ethics approval where applicable, controlled storage and pseudonymization procedures. Do not acquire CBCT solely to satisfy this research protocol unless radiation exposure is independently clinically justified and ethics approval permits the acquisition.
