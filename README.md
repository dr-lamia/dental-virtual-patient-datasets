# Dental Virtual Patient Datasets

A curated research-oriented catalog of public datasets useful for building a **dynamic 3D/4D dental virtual patient** for motion-aware smile design.

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

| Dataset | Primary modality | Scale / highlights | Best use in our project | Access |
|---|---|---|---|---|
| **NeRSemble** | Multi-view facial video / dynamic head | Multi-view expression sequences; very large full dataset | Dynamic Gaussian/NeRF avatar development and facial-motion testing | https://github.com/tobias-kirschstein/nersemble-data |
| **FaceScape** | High-resolution 3D faces + expressions | 847 identities × 20 expressions; large multi-view image set | Facial geometry, expression transfer, smile deformation | https://github.com/zhuhao-nju/facescape |
| **MultiFace** | Multi-view dynamic face + meshes + audio | 13 identities; dense multiview performance capture; mini dataset available | Dynamic face validation and multi-view reconstruction | https://github.com/facebookresearch/multiface |
| **VOCASET** | 4D facial motion + speech | ~29 min; 12 speakers; 60 fps; 480 sequences | Speech-driven facial motion and tooth-display experiments | https://voca.is.tue.mpg.de/ |
| **BIWI 3D Audiovisual** | Tracked 3D facial motion + audio | 14 subjects × 40 sentences | Speech/jaw-lip motion experiments | https://data.vision.ee.ethz.ch/cvl/datasets/b3dac2.en.html |
| **3DTeethSeg / Teeth3DS** | IOS / 3D dental meshes | 1,800 scans from 900 patients; upper/lower arches; tooth labels | Tooth instance segmentation, dental landmarks, IOS preprocessing | https://github.com/abenhamadou/3DTeethSeg_MICCAI_Challenges |
| **3D multimodal dental dataset based on CBCT and oral scan** | Paired CBCT + oral scans | 289 paired subjects; CC BY 4.0 | Patient-specific CBCT–IOS registration and virtual-patient integration | https://figshare.com/articles/dataset/_b_3D_multimodal_dental_dataset_based_on_CBCT_and_oral_scan_b_/26965903 |
| **ToothFairy2** | CBCT with detailed labels | Hundreds of CBCT scans; maxilla, mandible, teeth and other structures | Advanced anatomical segmentation and digital-twin extension | https://toothfairy2.grand-challenge.org/ |

## Recommended use by development stage

### Stage 1 — Facial avatar and movement
Use **NeRSemble**, **FaceScape**, **MultiFace** and **VOCASET** to benchmark facial reconstruction, expression control and speech animation.

### Stage 2 — Dental geometry
Use **3DTeethSeg/Teeth3DS** for tooth instance segmentation, FDI identification, gingiva separation and mesh preprocessing.

### Stage 3 — Multimodal anatomy
Use the **paired CBCT + oral-scan dataset** to study coordinate registration between volumetric anatomy and surface dental scans.

### Stage 4 — Full digital twin
Use **ToothFairy2** for automated maxilla/mandible/individual-tooth CBCT segmentation and advanced anatomical integration.

## Important dataset gap

We have not identified a mature public dataset that pairs, for the **same subject**:

1. dynamic facial video or 4D facial scan,
2. upper and lower IOS,
3. bite registration,
4. CBCT,
5. jaw-motion tracking, and
6. a restorative/smile CAD design.

This gap motivates a future purpose-built **4D Dental Virtual Patient Dataset**.

## Proposed minimal clinical research dataset

For a first prospective cohort, collect:

- 30–60 s standardized facial video
- frontal, 45° and profile facial photographs
- natural smile and maximum smile clips
- standardized speech clips
- upper IOS
- lower IOS
- bite scan
- original and proposed smile-design STL/PLY
- optional CBCT when clinically indicated (never acquire CBCT solely for research unless ethically justified)
- optional jaw-tracking record

See [`docs/proposed_capture_protocol.md`](docs/proposed_capture_protocol.md).

## Catalog files

- [`catalog/datasets.csv`](catalog/datasets.csv) — machine-readable dataset table
- [`catalog/software_repositories.csv`](catalog/software_repositories.csv) — related open-source projects
- [`docs/dataset_selection.md`](docs/dataset_selection.md) — which dataset to use for each module
- [`docs/licensing_notes.md`](docs/licensing_notes.md) — license/access checklist

## Related software projects

The companion project repository is designed to integrate ideas/tools from GaussianAvatars, FlashAvatar, MeGA, SplattingAvatar, Gaussian Blendshapes, VHAP, MICA, DECA/EMOCA, 3DTeethLand and Slicer dental tools.

## Citation

When using any listed dataset, cite the **original dataset/paper**, not this catalog.
