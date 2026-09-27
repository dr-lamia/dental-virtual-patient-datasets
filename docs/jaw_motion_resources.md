# Jaw-Motion Resources for a 4D Dental Patient

## Why this module matters

A true 4D dental patient requires the mandible to move independently from the maxilla/head. Facial animation alone is not sufficient: the lower IOS should be driven by a mandibular transform sequence that can be synchronized with facial motion.

## Public datasets

### 1. Premolar extraction and mandibular kinematics — Mendeley Data

- 90 subjects: 45 orthodontically treated extraction patients and 45 paired untreated controls.
- Computerized 3D CADIAX axiography.
- Includes condylar movement variables during protrusion/retrusion and speech.
- License listed by the repository: CC BY 4.0.
- Best use here: kinematic feature analysis, external validation targets, movement-distribution priors.
- Limitation: not a synchronized face + IOS + CBCT 4D patient cohort.

Source: https://data.mendeley.com/datasets/3tcs5c47jg

### 2. Jaw biodynamic data for unilateral TMD — Dryad

- 24 adult patients with chronic unilateral TMD.
- Condylar-path measurements from axiography and lateral guidance from K7 jaw tracking.
- Best use here: functional/TMJ validation and comparison of left/right movement metrics.
- Limitation: primarily derived/tabular measures rather than full frame-by-frame dental geometry.

Source: https://datadryad.org/dataset/doi%3A10.5061/dryad.n5d23

### 3. Accelerometry-enhanced magnetic jaw tracking — Figshare

- Magnetic sensor + accelerometry engineering dataset.
- Demonstrates 3D jaw-trajectory estimation and occlusal-impact detection on controlled motion/simulator experiments.
- Repository license: CC BY 4.0.
- Best use here: trajectory-processing experiments and low-cost sensing research.
- Limitation: engineering/simulator data, not a clinical multimodal 4D cohort.

Source: https://figshare.com/articles/dataset/Accelerometry-enhanced_Magnetic_Sensor_for_Intra-oral_Continuous_Jaw_Motion_Tracking_and_Bruxism_Detection/13397528/1

## Open-source tracking software

### JawTrackingSystem

Repository: https://github.com/paulotto/jaw_tracking_system

The project provides a modular Python pipeline for optical jaw motion capture, including calibration, coordinate transformation, smoothing, trajectory visualization and export. Its published repository also provides 3D-printable hardware components and documents an optical motion-capture validation workflow.

This is particularly relevant to the 4D dental project because its output can be converted into a per-frame `mandible_to_face` rigid transform and used to drive the lower IOS independently of facial/head motion.

## Standardized downstream representation

For interoperability, the companion project should convert any tracker-specific output to one neutral representation:

```text
frame_index
timestamp_s
tx_mm, ty_mm, tz_mm
qw, qx, qy, qz
jaw_opening_mm (optional)
```

or a full 4x4 rigid transform for each frame.

## Research rule

Do **not** combine jaw trajectories from one public subject with CBCT/IOS from another subject and describe the result as that patient's 4D digital twin. Cross-dataset combinations are acceptable only for software development, simulation and module-level benchmarking, with clear labeling.
