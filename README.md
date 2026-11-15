<div align="center">

# Awesome Craft Neuro [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open-source tools for brain-computer interfaces, electrophysiology and neurotechnology.

<img src="assets/craft-neuro.svg" alt="Pixel-art neuroscience lab with a generic EEG cap, a monitor showing brain-wave traces, and connected neurons" width="100%">

![Tools](https://img.shields.io/badge/tools-60-6366f1?style=for-the-badge)
[![Categories](https://img.shields.io/badge/categories-8-0ea5e9?style=for-the-badge)](#contents)
[![Combined stars](https://img.shields.io/badge/combined_stars-32.0k-f59e0b?style=for-the-badge&logo=github)](#-leaderboard)
[![Stars](https://img.shields.io/github/stars/EdisonTKPcom/Awesome-Craft-Neuro?style=for-the-badge&color=22c55e)](https://github.com/EdisonTKPcom/Awesome-Craft-Neuro/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/EdisonTKPcom/Awesome-Craft-Neuro?style=for-the-badge&color=ec4899)](https://github.com/EdisonTKPcom/Awesome-Craft-Neuro/commits/main)

</div>

Open-source tools now cover much of the neural-data stack: board-level acquisition, streaming, EEG and MEG analysis, spike sorting, BCI experiment frameworks, neural decoding, shared datasets, and MRI pipelines. Every entry below has a public GitHub repository that was checked on 2026-11-15. Check each project's licence before you use, modify or redistribute it.

**Ethics and medical safety:** nothing in this list is a medical device, a treatment, or clinical advice. Invasive brain-computer interfaces and implant hardware are subject to medical-device regulation, institutional review and surgical oversight. Consumer or research EEG hardware is not a diagnostic instrument. Do not treat company announcements, press photos or blog posts as evidence of safety or efficacy.

This snapshot of the [neuralink](https://github.com/neuralink) GitHub organisation found two public repositories, `tsui` (a Tailscale terminal UI) and `DicomPreview` (a macOS Quick Look plugin for DICOM files). Neither is implant or BCI software, so they are not listed as tools here. A public Neuralink compression-challenge repository was not found on that organisation. Published patient-count or milestone claims from companies are <span class="evi-goal">GOAL</span> or company statements unless they come from a peer-reviewed paper or a regulator.

Official BCI2000 and OpenViBE distributions were not found as maintained public GitHub repositories in this snapshot, so they are not listed. The same is true for official POYO and Neural Data Transformer (NDT) source repositories.


## Contents

- [Dashboard](#dashboard)
- [BCI hardware](#bci-hardware)
- [Signal acquisition and streaming](#signal-acquisition-and-streaming)
- [EEG, MEG and ECoG analysis](#eeg-meg-and-ecog-analysis)
- [Spike sorting and electrophysiology](#spike-sorting-and-electrophysiology)
- [BCI frameworks and paradigms](#bci-frameworks-and-paradigms)
- [Neural decoding and machine learning](#neural-decoding-and-machine-learning)
- [Datasets and standards](#datasets-and-standards)
- [Neuroimaging](#neuroimaging)
- [Related lists](#related-lists)
- [Star history](#star-history)


## Dashboard

<style>
.evi-fact{border-bottom:3px solid #0f172a;padding-bottom:1px}
.evi-goal{border-bottom:3px dashed #0f172a;padding-bottom:1px}
.evi-est{border-bottom:3px dotted #0f172a;padding-bottom:1px}
</style>

<table>
<tr>
<td align="center"><h2><span class="evi-fact">60</span></h2>listed projects</td>
<td align="center"><h2><span class="evi-fact">8</span></h2>categories</td>
<td align="center"><h2><span class="evi-est">32.0k</span></h2>combined GitHub stars</td>
<td align="center"><h2><span class="evi-est">12.6k</span></h2>combined forks</td>
<td align="center"><h2><span class="evi-est">40/60</span></h2>pushed in the last 30 days</td>
<td align="center"><h2><span class="evi-fact">8</span></h2>languages</td>
</tr>
</table>

**Evidence tags**

<table>
<tr><th>Tag</th><th>Style</th><th>Meaning</th></tr>
<tr><td><span class="evi-fact">FACT</span></td><td>solid underline</td><td>A measured figure, with the source named.</td></tr>
<tr><td><span class="evi-goal">GOAL</span></td><td>dashed underline</td><td>A stated roadmap, plan or company claim, not a verified result.</td></tr>
<tr><td><span class="evi-est">ESTIMATE</span></td><td>dotted underline</td><td>A sum or count we computed from the facts.</td></tr>
</table>

The dashboard numbers themselves are FACT or ESTIMATE values from GitHub. This snapshot has no GOAL figures in the table above. Company claims about implants, patients or performance should be read as <span class="evi-goal">GOAL</span> unless a paper or regulator is cited.

**Sources and method**

- Star counts, fork counts, licences, primary languages and last-push dates are <span class="evi-fact">FACT</span> values from the GitHub Search and REST APIs on 2026-11-15 (`stargazers_count`, `forks_count`, `license.spdx_id`, `language`, `pushed_at`).
- Combined stars (<span class="evi-est">32.0k</span>) and combined forks (<span class="evi-est">12.6k</span>) are <span class="evi-est">ESTIMATE</span>s: the arithmetic sum of those per-repository FACT counts, with no weighting and no unique-user deduplication. A person who stars two projects is counted twice.
- Pushed in the last 30 days (<span class="evi-est">40/60</span>) is an <span class="evi-est">ESTIMATE</span>: the number of listed repositories whose FACT `pushed_at` date is on or after 2026-10-16.
- Language and category counts, and the licence badges, are <span class="evi-est">ESTIMATE</span>s of FACT fields. Star badges next to each entry update live and may differ from this snapshot.

### 🏆 Leaderboard

Star counts in this table are FACT values from the snapshot. The bars are only a visual scale.

<table>
<tr><th>Rank</th><th>Project</th><th>Kind</th><th align="right">Stars</th><th></th></tr>
<tr><td align="center">🥇</td><td><b>MNE-Python</b></td><td>EEG, MEG and ECoG analysis</td><td align="right"><span class="evi-fact">3.6k</span></td><td><code>████████████████████</code></td></tr>
<tr><td align="center">🥈</td><td><b>BrainFlow</b></td><td>Signal acquisition and streaming</td><td align="right"><span class="evi-fact">1.8k</span></td><td><code>██████████</code></td></tr>
<tr><td align="center">🥉</td><td><b>ANTs</b></td><td>Neuroimaging</td><td align="right"><span class="evi-fact">1.5k</span></td><td><code>████████</code></td></tr>
<tr><td align="center">4</td><td><b>Nilearn</b></td><td>Neuroimaging</td><td align="right"><span class="evi-fact">1.5k</span></td><td><code>████████</code></td></tr>
<tr><td align="center">5</td><td><b>Braindecode</b></td><td>BCI frameworks and paradigms</td><td align="right"><span class="evi-fact">1.3k</span></td><td><code>███████</code></td></tr>
<tr><td align="center">6</td><td><b>CEBRA</b></td><td>Neural decoding and machine learning</td><td align="right"><span class="evi-fact">1.1k</span></td><td><code>██████</code></td></tr>
<tr><td align="center">7</td><td><b>MOABB</b></td><td>BCI frameworks and paradigms</td><td align="right"><span class="evi-fact">1.1k</span></td><td><code>██████</code></td></tr>
<tr><td align="center">8</td><td><b>FieldTrip</b></td><td>EEG, MEG and ECoG analysis</td><td align="right"><span class="evi-fact">993</span></td><td><code>██████</code></td></tr>
<tr><td align="center">9</td><td><b>OpenBCI GUI</b></td><td>BCI hardware</td><td align="right"><span class="evi-fact">983</span></td><td><code>█████</code></td></tr>
<tr><td align="center">10</td><td><b>FreeSurfer</b></td><td>Neuroimaging</td><td align="right"><span class="evi-fact">887</span></td><td><code>█████</code></td></tr>
</table>


### Stars by category

These category totals are ESTIMATE sums of the per-repository FACT star counts.

```mermaid
pie showData
    title Combined GitHub stars by category
    "BCI hardware" : 2221
    "Signal acquisition and streaming" : 2480
    "EEG, MEG and ECoG analysis" : 8532
    "Spike sorting and electrophysiology" : 3100
    "BCI frameworks and paradigms" : 4565
    "Neural decoding and machine learning" : 1596
    "Datasets and standards" : 2042
    "Neuroimaging" : 7480
```

### Licences

![MIT](https://img.shields.io/badge/MIT-16-64748b?style=flat-square) ![BSD-3-Clause](https://img.shields.io/badge/BSD--3--Clause-14-64748b?style=flat-square) ![Custom](https://img.shields.io/badge/Custom-12-64748b?style=flat-square) ![Apache-2.0](https://img.shields.io/badge/Apache--2.0-7-64748b?style=flat-square) ![GPL-3.0](https://img.shields.io/badge/GPL--3.0-7-64748b?style=flat-square) ![AGPL-3.0](https://img.shields.io/badge/AGPL--3.0-1-64748b?style=flat-square) ![GPL-2.0](https://img.shields.io/badge/GPL--2.0-1-64748b?style=flat-square) ![CC-BY-4.0](https://img.shields.io/badge/CC--BY--4.0-1-64748b?style=flat-square) ![MPL-2.0](https://img.shields.io/badge/MPL--2.0-1-64748b?style=flat-square)

These badge counts are ESTIMATE tallies of the SPDX identifier GitHub returned for each repository. "Custom" or "None" means GitHub could not match a standard SPDX licence. The BIDS specification uses CC-BY-4.0, a content licence rather than a typical OSI software licence. FreeSurfer has long used a custom academic licence rather than an OSI licence. Read each project licence before you use it commercially or in a clinic.

## BCI hardware

- [FreeEEG32](https://github.com/neuroidss/FreeEEG32-beta) - Open hardware for a 32-channel mobile EEG based on AD777x converters. Last push 2025-11-14. ![Stars](https://img.shields.io/github/stars/neuroidss/FreeEEG32-beta?style=flat-square&label=%E2%AD%90)
- [HackEEG Python client](https://github.com/starcat-io/hackeeg-client-python) - Python client for the HackEEG ADS1299 Arduino shield. ![Stars](https://img.shields.io/github/stars/starcat-io/hackeeg-client-python?style=flat-square&label=%E2%AD%90)
- [HackEEG shield](https://github.com/starcat-io/hackeeg-shield) - Hardware design files for an ADS1299 Arduino EEG shield. GitHub could not match a standard SPDX licence, and the last push was 2021-06-03. ![Stars](https://img.shields.io/github/stars/starcat-io/hackeeg-shield?style=flat-square&label=%E2%AD%90)
- [Neurosity SDK for JavaScript](https://github.com/neurosity/neurosity-sdk-js) - Official JavaScript SDK for Neurosity headsets. ![Stars](https://img.shields.io/github/stars/neurosity/neurosity-sdk-js?style=flat-square&label=%E2%AD%90)
- [Neurosity SDK for Python](https://github.com/neurosity/neurosity-sdk-python) - Official Python SDK for Neurosity headsets. ![Stars](https://img.shields.io/github/stars/neurosity/neurosity-sdk-python?style=flat-square&label=%E2%AD%90)
- [OpenBCI Cyton library](https://github.com/OpenBCI/OpenBCI_Cyton_Library) - Arduino firmware library for the OpenBCI Cyton board. Last push 2025-07-28. ![Stars](https://img.shields.io/github/stars/OpenBCI/OpenBCI_Cyton_Library?style=flat-square&label=%E2%AD%90)
- [OpenBCI GUI](https://github.com/OpenBCI/OpenBCI_GUI) - Cross-platform application for acquiring and visualising data from OpenBCI Cyton and Ganglion boards. ![Stars](https://img.shields.io/github/stars/OpenBCI/OpenBCI_GUI?style=flat-square&label=%E2%AD%90)
- [Ultracortex](https://github.com/OpenBCI/Ultracortex) - 3D-printable EEG headset files from OpenBCI. Last push 2022-09-29. ![Stars](https://img.shields.io/github/stars/OpenBCI/Ultracortex?style=flat-square&label=%E2%AD%90)

## Signal acquisition and streaming

- [BrainFlow](https://github.com/brainflow-dev/brainflow) - Library to acquire, parse and analyse EEG, EMG, ECG and other biosignals from many boards. GitHub could not match a standard SPDX licence. ![Stars](https://img.shields.io/github/stars/brainflow-dev/brainflow?style=flat-square&label=%E2%AD%90)
- [Lab Recorder](https://github.com/labstreaminglayer/App-LabRecorder) - Application that records one or more Lab Streaming Layer streams to XDF files. ![Stars](https://img.shields.io/github/stars/labstreaminglayer/App-LabRecorder?style=flat-square&label=%E2%AD%90)
- [liblsl](https://github.com/sccn/liblsl) - C++ core library for Lab Streaming Layer, used to time-synchronise multimodal streams on a local network. GitHub could not match a standard SPDX licence. ![Stars](https://img.shields.io/github/stars/sccn/liblsl?style=flat-square&label=%E2%AD%90)
- [MNE-LSL](https://github.com/mne-tools/mne-lsl) - Real-time brain-signal streaming framework that connects Lab Streaming Layer to MNE-Python. ![Stars](https://img.shields.io/github/stars/mne-tools/mne-lsl?style=flat-square&label=%E2%AD%90)
- [pylsl](https://github.com/labstreaminglayer/pylsl) - Python bindings for liblsl. ![Stars](https://img.shields.io/github/stars/labstreaminglayer/pylsl?style=flat-square&label=%E2%AD%90)

## EEG, MEG and ECoG analysis

- [autoreject](https://github.com/autoreject/autoreject) - Automated rejection and repair of bad trials and sensors in M/EEG data. ![Stars](https://img.shields.io/github/stars/autoreject/autoreject?style=flat-square&label=%E2%AD%90)
- [Brainstorm](https://github.com/brainstorm-tools/brainstorm3) - MATLAB environment for MEG, EEG, fNIRS, ECoG, sEEG and electrophysiology analysis. ![Stars](https://img.shields.io/github/stars/brainstorm-tools/brainstorm3?style=flat-square&label=%E2%AD%90)
- [EEG-ExPy](https://github.com/NeuroTechX/EEG-ExPy) - Python collection of EEG experiment paradigms from NeuroTechX, formerly EEG-Notebooks. ![Stars](https://img.shields.io/github/stars/NeuroTechX/EEG-ExPy?style=flat-square&label=%E2%AD%90)
- [EEGLAB](https://github.com/sccn/eeglab) - MATLAB toolbox for electrophysiological signal processing, developed at SCCN. GitHub could not match a standard SPDX licence. ![Stars](https://img.shields.io/github/stars/sccn/eeglab?style=flat-square&label=%E2%AD%90)
- [FieldTrip](https://github.com/fieldtrip/fieldtrip) - MATLAB toolbox for MEG, EEG and intracranial EEG analysis. ![Stars](https://img.shields.io/github/stars/fieldtrip/fieldtrip?style=flat-square&label=%E2%AD%90)
- [FOOOF](https://github.com/fooof-tools/fooof) - Tool for parameterising neural power spectra into periodic and aperiodic components, also known as specparam. ![Stars](https://img.shields.io/github/stars/fooof-tools/fooof?style=flat-square&label=%E2%AD%90)
- [MNE-Python](https://github.com/mne-tools/mne-python) - Python package for acquiring, preprocessing, analysing and visualising MEG, EEG and other electrophysiological data. ![Stars](https://img.shields.io/github/stars/mne-tools/mne-python?style=flat-square&label=%E2%AD%90)
- [MNELAB](https://github.com/cbrnr/mnelab) - Graphical user interface for MNE-Python. ![Stars](https://img.shields.io/github/stars/cbrnr/mnelab?style=flat-square&label=%E2%AD%90)
- [NeuroDSP](https://github.com/neurodsp-tools/neurodsp) - Digital signal processing tools for neural time series. ![Stars](https://img.shields.io/github/stars/neurodsp-tools/neurodsp?style=flat-square&label=%E2%AD%90)
- [PyPREP](https://github.com/sappelhoff/pyprep) - Python implementation of the PREP pipeline for EEG preprocessing. ![Stars](https://img.shields.io/github/stars/sappelhoff/pyprep?style=flat-square&label=%E2%AD%90)
- [YASA](https://github.com/raphaelvallat/yasa) - Python package for analysing polysomnographic sleep recordings, including EEG spindle and staging tools. ![Stars](https://img.shields.io/github/stars/raphaelvallat/yasa?style=flat-square&label=%E2%AD%90)

## Spike sorting and electrophysiology

- [Elephant](https://github.com/NeuralEnsemble/elephant) - Electrophysiology analysis toolkit built on Neo, covering spike-train and LFP statistics. ![Stars](https://img.shields.io/github/stars/NeuralEnsemble/elephant?style=flat-square&label=%E2%AD%90)
- [Intan RHX](https://github.com/Intan-Technologies/Intan-RHX) - Free data-acquisition software from Intan Technologies for displaying and recording signals from Intan hardware. ![Stars](https://img.shields.io/github/stars/Intan-Technologies/Intan-RHX?style=flat-square&label=%E2%AD%90)
- [Kilosort](https://github.com/MouseLand/Kilosort) - Fast spike-sorting algorithm with drift correction, developed by MouseLand. ![Stars](https://img.shields.io/github/stars/MouseLand/Kilosort?style=flat-square&label=%E2%AD%90)
- [MountainSort 5](https://github.com/flatironinstitute/mountainsort5) - MountainSort spike-sorting algorithm, version 5, from the Flatiron Institute. ![Stars](https://img.shields.io/github/stars/flatironinstitute/mountainsort5?style=flat-square&label=%E2%AD%90)
- [Neo](https://github.com/NeuralEnsemble/python-neo) - Python package for representing electrophysiology data and reading many acquisition formats. ![Stars](https://img.shields.io/github/stars/NeuralEnsemble/python-neo?style=flat-square&label=%E2%AD%90)
- [Open Ephys GUI](https://github.com/open-ephys/plugin-GUI) - Modular software for processing, recording and visualising multichannel electrophysiology. ![Stars](https://img.shields.io/github/stars/open-ephys/plugin-GUI?style=flat-square&label=%E2%AD%90)
- [Open Ephys Python tools](https://github.com/open-ephys/open-ephys-python-tools) - Python tools for interacting with the Open Ephys GUI and its data formats. Last push 2025-11-07. ![Stars](https://img.shields.io/github/stars/open-ephys/open-ephys-python-tools?style=flat-square&label=%E2%AD%90)
- [phy](https://github.com/cortex-lab/phy) - Interactive visualisation and manual curation tool for large-scale spike-sorted ephys data. ![Stars](https://img.shields.io/github/stars/cortex-lab/phy?style=flat-square&label=%E2%AD%90)
- [SpikeGLX](https://github.com/billkarsh/SpikeGLX) - Recording-system GUI widely used with Neuropixels and National Instruments hardware. GitHub could not match a standard SPDX licence. ![Stars](https://img.shields.io/github/stars/billkarsh/SpikeGLX?style=flat-square&label=%E2%AD%90)
- [SpikeInterface](https://github.com/SpikeInterface/spikeinterface) - Python framework for building flexible spike-sorting pipelines, with wrappers for many sorters. ![Stars](https://img.shields.io/github/stars/SpikeInterface/spikeinterface?style=flat-square&label=%E2%AD%90)

## BCI frameworks and paradigms

- [BciPy](https://github.com/CAMBI-tech/BciPy) - Python research software for building and running BCI experiments, from CAMBI. ![Stars](https://img.shields.io/github/stars/CAMBI-tech/BciPy?style=flat-square&label=%E2%AD%90)
- [Braindecode](https://github.com/braindecode/braindecode) - Deep-learning library for decoding EEG, ECG and MEG signals. ![Stars](https://img.shields.io/github/stars/braindecode/braindecode?style=flat-square&label=%E2%AD%90)
- [EEGsynth](https://github.com/eegsynth/eegsynth) - Modular system that converts real-time EEG into sound, music and visual effects. ![Stars](https://img.shields.io/github/stars/eegsynth/eegsynth?style=flat-square&label=%E2%AD%90)
- [MetaBCI](https://github.com/TBC-TJU/MetaBCI) - Open-source platform for non-invasive BCI research, led by Tianjin University. ![Stars](https://img.shields.io/github/stars/TBC-TJU/MetaBCI?style=flat-square&label=%E2%AD%90)
- [MOABB](https://github.com/NeuroTechX/moabb) - Mother of All BCI Benchmarks, a framework for reproducible EEG decoding experiments. ![Stars](https://img.shields.io/github/stars/NeuroTechX/moabb?style=flat-square&label=%E2%AD%90)
- [pyRiemann](https://github.com/pyRiemann/pyRiemann) - Machine learning for multivariate biosignals using the Riemannian geometry of covariance matrices. ![Stars](https://img.shields.io/github/stars/pyRiemann/pyRiemann?style=flat-square&label=%E2%AD%90)
- [Timeflux](https://github.com/timeflux/timeflux) - Python framework for real-time biosignal processing and BCI applications. Last push 2024-12-04. ![Stars](https://img.shields.io/github/stars/timeflux/timeflux?style=flat-square&label=%E2%AD%90)

## Neural decoding and machine learning

- [CEBRA](https://github.com/AdaptiveMotorControlLab/CEBRA) - Learnable latent embeddings for jointly analysing behavioural and neural data. GitHub could not match a standard SPDX licence. ![Stars](https://img.shields.io/github/stars/AdaptiveMotorControlLab/CEBRA?style=flat-square&label=%E2%AD%90)
- [NLB tools](https://github.com/neurallatents/nlb_tools) - Python tools for the Neural Latents Benchmark, a challenge on inferring latent dynamics from neural population recordings. ![Stars](https://img.shields.io/github/stars/neurallatents/nlb_tools?style=flat-square&label=%E2%AD%90)
- [pynapple](https://github.com/pynapple-org/pynapple) - Lightweight Python library for analysing neurophysiological data, including tuning, decoding and sleep-related metrics. ![Stars](https://img.shields.io/github/stars/pynapple-org/pynapple?style=flat-square&label=%E2%AD%90)

## Datasets and standards

- [BIDS specification](https://github.com/bids-standard/bids-specification) - The Brain Imaging Data Structure standard. It uses CC-BY-4.0, a content licence rather than a typical OSI software licence. ![Stars](https://img.shields.io/github/stars/bids-standard/bids-specification?style=flat-square&label=%E2%AD%90)
- [BIDS Validator](https://github.com/bids-standard/bids-validator) - Validator for datasets that follow the Brain Imaging Data Structure. ![Stars](https://img.shields.io/github/stars/bids-standard/bids-validator?style=flat-square&label=%E2%AD%90)
- [DANDI CLI](https://github.com/dandi/dandi-cli) - Command-line client for the DANDI archive of cellular neurophysiology data stored with NWB. ![Stars](https://img.shields.io/github/stars/dandi/dandi-cli?style=flat-square&label=%E2%AD%90)
- [HDMF](https://github.com/hdmf-dev/hdmf) - Hierarchical Data Modeling Framework used by NWB. GitHub could not match a standard SPDX licence. ![Stars](https://img.shields.io/github/stars/hdmf-dev/hdmf?style=flat-square&label=%E2%AD%90)
- [OpenNeuro](https://github.com/OpenNeuroOrg/openneuro) - Free platform for sharing and analysing neuroimaging datasets, typically in BIDS. ![Stars](https://img.shields.io/github/stars/OpenNeuroOrg/openneuro?style=flat-square&label=%E2%AD%90)
- [PyBIDS](https://github.com/bids-standard/pybids) - Python tools for querying and manipulating BIDS datasets. ![Stars](https://img.shields.io/github/stars/bids-standard/pybids?style=flat-square&label=%E2%AD%90)
- [PyNWB](https://github.com/NeurodataWithoutBorders/pynwb) - Python API for reading and writing data in the Neurodata Without Borders (NWB) format. GitHub could not match a standard SPDX licence. ![Stars](https://img.shields.io/github/stars/NeurodataWithoutBorders/pynwb?style=flat-square&label=%E2%AD%90)
- [WFDB Python](https://github.com/MIT-LCP/wfdb-python) - Python toolkit for reading, writing and processing PhysioNet WFDB signals and annotations. ![Stars](https://img.shields.io/github/stars/MIT-LCP/wfdb-python?style=flat-square&label=%E2%AD%90)

## Neuroimaging

- [ANTs](https://github.com/ANTsX/ANTs) - Advanced Normalization Tools for medical image registration, segmentation and template building. ![Stars](https://img.shields.io/github/stars/ANTsX/ANTs?style=flat-square&label=%E2%AD%90)
- [DIPY](https://github.com/dipy/dipy) - Python library for diffusion MRI and other 3D/4D medical imaging analysis. GitHub could not match a standard SPDX licence. ![Stars](https://img.shields.io/github/stars/dipy/dipy?style=flat-square&label=%E2%AD%90)
- [fMRIPrep](https://github.com/nipreps/fmriprep) - Robust, easily used pipeline for preprocessing diverse fMRI datasets. ![Stars](https://img.shields.io/github/stars/nipreps/fmriprep?style=flat-square&label=%E2%AD%90)
- [FreeSurfer](https://github.com/freesurfer/freesurfer) - Suite for neuroimaging analysis and visualisation, including cortical surface reconstruction. GitHub could not match a standard SPDX licence, and the project has long used a custom academic licence rather than an OSI licence, so read it before you use the software. ![Stars](https://img.shields.io/github/stars/freesurfer/freesurfer?style=flat-square&label=%E2%AD%90)
- [MRtrix3](https://github.com/MRtrix3/mrtrix3) - Tools for advanced diffusion MRI analysis, including tractography and fibre-orientation estimation. ![Stars](https://img.shields.io/github/stars/MRtrix3/mrtrix3?style=flat-square&label=%E2%AD%90)
- [NiBabel](https://github.com/nipy/nibabel) - Python package for reading and writing many neuroimaging file formats. GitHub could not match a standard SPDX licence. ![Stars](https://img.shields.io/github/stars/nipy/nibabel?style=flat-square&label=%E2%AD%90)
- [Nilearn](https://github.com/nilearn/nilearn) - Python library for statistical and machine-learning analysis of neuroimaging data. ![Stars](https://img.shields.io/github/stars/nilearn/nilearn?style=flat-square&label=%E2%AD%90)
- [Nipype](https://github.com/nipy/nipype) - Python workflows and interfaces that connect neuroimaging packages into reproducible pipelines. GitHub could not match a standard SPDX licence. ![Stars](https://img.shields.io/github/stars/nipy/nipype?style=flat-square&label=%E2%AD%90)

## Related lists

Other lists in the Awesome Craft series:

- [Awesome Craft](https://github.com/EdisonTKPcom/Awesome-Craft) - A curated list of open-source, self-hostable alternatives to popular SaaS tools.
- [Awesome Craft Agents](https://github.com/EdisonTKPcom/Awesome-Craft-Agents) - A curated list of open-source chat apps, coding agents, self-hosted agent bots, workflow automation and image-generation UIs.
- [Awesome Craft AI](https://github.com/EdisonTKPcom/Awesome-Craft-AI) - A curated list of open-source, self-hostable AI runtimes, servers, Hugging Face libraries and related infrastructure.
- [Awesome Craft BSC](https://github.com/EdisonTKPcom/Awesome-Craft-BSC) - A curated list of verified open-source clients, SDKs, dev tools and protocol code for BNB Smart Chain and opBNB.
- [Awesome Craft CUDA](https://github.com/EdisonTKPcom/Awesome-Craft-CUDA) - A curated list of open-source CUDA learning material, kernel libraries, tooling and portability projects.
- [Awesome Craft DeepSeek](https://github.com/EdisonTKPcom/Awesome-Craft-DeepSeek) - A curated list of official DeepSeek repositories and open-source harnesses, serving engines, eval tools and fine-tuning stacks that work with DeepSeek models.
- [Awesome Craft DevOps](https://github.com/EdisonTKPcom/Awesome-Craft-DevOps) - A curated list of open-source, self-hostable alternatives to popular DevOps and hosting SaaS tools.
- [Awesome Craft DNA](https://github.com/EdisonTKPcom/Awesome-Craft-DNA) - A curated list of open-source tools for DNA, genomics and synthetic biology.
- [Awesome Craft Ethereum](https://github.com/EdisonTKPcom/Awesome-Craft-Ethereum) - A curated list of verified open-source Ethereum clients, SDKs, dev frameworks, wallets and security tools.
- [Awesome Craft EV](https://github.com/EdisonTKPcom/Awesome-Craft-EV) - A curated list of open-source software and hardware for electric vehicles and charging.
- [Awesome Craft Hardware](https://github.com/EdisonTKPcom/Awesome-Craft-Hardware) - A curated list of open-source tools for PCB, FPGA, ASIC and chip design.
- [Awesome Craft Hyperliquid](https://github.com/EdisonTKPcom/Awesome-Craft-Hyperliquid) - A curated list of verified open-source SDKs, node tools, analytics and community libraries for the Hyperliquid ecosystem.
- [Awesome Craft Malaysia](https://github.com/EdisonTKPcom/Awesome-Craft-Malaysia) - A curated list of open-source tools useful to Malaysian SMEs, with verified MyInvois support called out separately.
- [Awesome Craft Mars](https://github.com/EdisonTKPcom/Awesome-Craft-Mars) - A curated list of open-source tools and open data for Mars missions and settlement planning.
- [Awesome Craft Robotics](https://github.com/EdisonTKPcom/Awesome-Craft-Robotics) - A curated list of open-source robotics software and hardware, including Microduck, Unitree SDKs, open humanoids, arms, simulation and middleware.
- [Awesome Craft Solana](https://github.com/EdisonTKPcom/Awesome-Craft-Solana) - A curated list of verified open-source Solana clients, SDKs, frameworks, explorers and program libraries.
- [Awesome Craft Space](https://github.com/EdisonTKPcom/Awesome-Craft-Space) - A curated list of open-source tools for spaceflight and rockets, covering orbit simulation, telemetry, launch data and more.
- [Awesome Craft Starlink](https://github.com/EdisonTKPcom/Awesome-Craft-Starlink) - A curated list of open-source tools for Starlink and other LEO satellite internet systems.
- [Awesome Craft Web3](https://github.com/EdisonTKPcom/Awesome-Craft-Web3) - A curated list of open-source DEX protocol code, self-custody software, indexers, frameworks and Blockchain infrastructure.

## Star history

[![Star History Chart](https://api.star-history.com/chart?repos=EdisonTKPcom/Awesome-Craft-Neuro&amp;type=Date)](https://www.star-history.com/#EdisonTKPcom/Awesome-Craft-Neuro&Date)

## Contributing

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

<div align="center">

If this list helped you find a tool, give it a ⭐ so others can find it.

</div>
