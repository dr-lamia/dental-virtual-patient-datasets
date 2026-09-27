# Dental Virtual Patient Datasets

A curated research-oriented catalog of public datasets and open tools useful for building a **dynamic 3D/4D dental virtual patient** for motion-aware smile design.

> This repository does **not** redistribute third-party datasets. It provides links, modality summaries, intended use, and licensing/access notes. Always review the original license and ethics/data-use terms before downloading or publishing.

## Goal

Support development of systems that combine:

- dynamic photorealistic facial avatars
- facial expression and speech motion
- intraoral scan (IOS) geometry
- CBCT anatomy
- tooth instance segmentation and landmarks
- jaw/mandibular motion
- replaceable CAD smile designs

## Dataset map

| Dataset | Primary modality | Scale / highlights | Best use in our project |
|---|---|---|---|
| **NeRSemble** | Multi-view facial video / dynamic head | Large multi-view facial-performance dataset | Dynamic avatar development |
| **FaceScape** | 3D faces + expressions | 847 identities × 20 expressions | Facial geometry/expression validation |
| **MultiFace** | Multi-view face + meshes + audio | 13 identities | Dynamic face validation |
| **VOCASET** | 4D facial motion + speech | 12 speakers; 480 sequences; 60 fps | Speech-driven facial motion |
| **BIWI 3D Audiovisual** | 3D facial motion + audio | 14 subjects × 40 sentences | Speech/jaw-lip motion |
| **3DTeethSeg / Teeth3DS** | IOS / dental meshes | 1,800 scans from 900 patients | Tooth segmentation and IOS preprocessing |
| **CBCT + oral-scan multimodal dataset** | Paired CBCT + oral scans | 289 paired subjects | Patient-specific CBCT–IOS registration |
| **ToothFairy2** | CBCT + labels | 480 public training CBCT volumes | Anatomical segmentation |
| **Premolar extraction & mandibular kinematics** | 3D CADIAX axiography | 90 subjects | Clinical jaw-kinematics benchmarking |
| **TMD jaw biodynamics** | Axiography + K7-derived measures | 24 patients | TMJ/lateral-motion benchmarking |
| **Magnetic jaw-tracking dataset** | Magnetometer + accelerometry | Engineering/simulator dataset | Low-cost trajectory/sensor research |

Machine-readable details and access URLs are in [catalog/datasets.csv](catalog/datasets.csv).

## Open jaw-tracking software

The catalog now includes **JawTrackingSystem**, an open-source optical jaw-tracking package with calibration, rigid-body transformations, smoothing, trajectory visualization/export and 3D-printable hardware components.

See:

- [catalog/software_repositories.csv](catalog/software_repositories.csv)
- [docs/jaw_motion_resources.md](docs/jaw_motion_resources.md)

## Recommended use by development stage

### Stage 1 — Facial avatar and movement
Use **NeRSemble**, **FaceScape**, **MultiFace** and **VOCASET** to benchmark facial reconstruction, expression control and speech animation.

### Stage 2 — Dental geometry
Use **3DTeethSeg/Teeth3DS** for tooth instance segmentation, FDI identification, gingiva separation and mesh preprocessing.

### Stage 3 — Multimodal anatomy
Use the **paired CBCT + oral-scan dataset** to study coordinate registration between volumetric anatomy and surface dental scans.

### Stage 4 — Jaw-motion module
Use the public CADIAX/TMD/sensor datasets for kinematic analysis and external benchmarking, and evaluate an open tracker for patient-specific trajectory capture.

### Stage 5 — Full same-patient digital twin
Fuse dynamic face + upper/lower IOS + bite + jaw motion for the **same subject**. Add CBCT only when clinically indicated.

## Important dataset gap

We have still not identified a mature public dataset that pairs, for the **same subject**:

1. dynamic facial video or 4D facial scan,
2. upper and lower IOS,
3. bite registration,
4. patient-specific jaw-motion trajectory,
5. CBCT where clinically indicated, and
6. a restorative/smile CAD design.

The newly added jaw-motion datasets are therefore **partial 4D resources**, not complete dental digital-twin cohorts. Do not fuse unrelated subjects and describe the result as one patient.

This gap motivates a purpose-built **4D Dental Virtual Patient Dataset**.

## Proposed clinical research dataset

For the prospective same-patient protocol collect:

- 30–60 s standardized facial video
- standardized expressions and speech
- upper IOS
- lower IOS
- bite scan
- jaw-motion recording
- original and proposed smile-design STL/PLY
- optional CBCT when clinically indicated
- optional calibrated facial scan / calibrated dental photography

See [docs/proposed_capture_protocol.md](docs/proposed_capture_protocol.md).

## Catalog files

- [catalog/datasets.csv](catalog/datasets.csv) — machine-readable dataset table
- [catalog/software_repositories.csv](catalog/software_repositories.csv) — related open-source projects
- [docs/dataset_selection.md](docs/dataset_selection.md) — which dataset to use for each module
- [docs/jaw_motion_resources.md](docs/jaw_motion_resources.md) — jaw-motion datasets/tools and limitations
- [docs/licensing_notes.md](docs/licensing_notes.md) — license/access checklist

## Companion implementation

The implementation repository is **dr-lamia/dynamic-dental-gaussian-avatar**, which combines facial tracking/avatars, dental meshes, registration, jaw motion and design swapping.

## Citation

When using any listed dataset, cite the **original dataset/paper**, not this catalog.
