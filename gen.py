#!/usr/bin/env python3
import csv
import urllib.parse as U
from pathlib import Path

ROOT = Path(__file__).resolve().parent
S = {
    r[0]: dict(stars=int(r[1]), forks=int(r[2]), lic=r[3], lang=r[4], push=r[5])
    for r in csv.reader((ROOT / "stats.tsv").open(), delimiter="\t")
}
LICNAME = {"NOASSERTION": "Custom", "none": "None", "OTHER": "Custom"}
AS = "2026-11-15"
ACTIVE_SINCE = "2026-10-16"

# (name, repo, description) — descriptions already include licence / last-push flags
C = [
    (
        "BCI hardware",
        [
            ("FreeEEG32", "neuroidss/FreeEEG32-beta", "Open hardware for a 32-channel mobile EEG based on AD777x converters. Last push 2025-11-14."),
            ("HackEEG Python client", "starcat-io/hackeeg-client-python", "Python client for the HackEEG ADS1299 Arduino shield."),
            ("HackEEG shield", "starcat-io/hackeeg-shield", "Hardware design files for an ADS1299 Arduino EEG shield. GitHub could not match a standard SPDX licence, and the last push was 2021-06-03."),
            ("Neurosity SDK for JavaScript", "neurosity/neurosity-sdk-js", "Official JavaScript SDK for Neurosity headsets."),
            ("Neurosity SDK for Python", "neurosity/neurosity-sdk-python", "Official Python SDK for Neurosity headsets."),
            ("OpenBCI Cyton library", "OpenBCI/OpenBCI_Cyton_Library", "Arduino firmware library for the OpenBCI Cyton board. Last push 2025-07-28."),
            ("OpenBCI GUI", "OpenBCI/OpenBCI_GUI", "Cross-platform application for acquiring and visualising data from OpenBCI Cyton and Ganglion boards."),
            ("Ultracortex", "OpenBCI/Ultracortex", "3D-printable EEG headset files from OpenBCI. Last push 2022-09-29."),
        ],
    ),
    (
        "Signal acquisition and streaming",
        [
            ("BrainFlow", "brainflow-dev/brainflow", "Library to acquire, parse and analyse EEG, EMG, ECG and other biosignals from many boards. GitHub could not match a standard SPDX licence."),
            ("Lab Recorder", "labstreaminglayer/App-LabRecorder", "Application that records one or more Lab Streaming Layer streams to XDF files."),
            ("liblsl", "sccn/liblsl", "C++ core library for Lab Streaming Layer, used to time-synchronise multimodal streams on a local network. GitHub could not match a standard SPDX licence."),
            ("MNE-LSL", "mne-tools/mne-lsl", "Real-time brain-signal streaming framework that connects Lab Streaming Layer to MNE-Python."),
            ("pylsl", "labstreaminglayer/pylsl", "Python bindings for liblsl."),
        ],
    ),
    (
        "EEG, MEG and ECoG analysis",
        [
            ("autoreject", "autoreject/autoreject", "Automated rejection and repair of bad trials and sensors in M/EEG data."),
            ("Brainstorm", "brainstorm-tools/brainstorm3", "MATLAB environment for MEG, EEG, fNIRS, ECoG, sEEG and electrophysiology analysis."),
            ("EEG-ExPy", "NeuroTechX/EEG-ExPy", "Python collection of EEG experiment paradigms from NeuroTechX, formerly EEG-Notebooks."),
            ("EEGLAB", "sccn/eeglab", "MATLAB toolbox for electrophysiological signal processing, developed at SCCN. GitHub could not match a standard SPDX licence."),
            ("FieldTrip", "fieldtrip/fieldtrip", "MATLAB toolbox for MEG, EEG and intracranial EEG analysis."),
            ("FOOOF", "fooof-tools/fooof", "Tool for parameterising neural power spectra into periodic and aperiodic components, also known as specparam."),
            ("MNELAB", "cbrnr/mnelab", "Graphical user interface for MNE-Python."),
            ("MNE-Python", "mne-tools/mne-python", "Python package for acquiring, preprocessing, analysing and visualising MEG, EEG and other electrophysiological data."),
            ("NeuroDSP", "neurodsp-tools/neurodsp", "Digital signal processing tools for neural time series."),
            ("PyPREP", "sappelhoff/pyprep", "Python implementation of the PREP pipeline for EEG preprocessing."),
            ("YASA", "raphaelvallat/yasa", "Python package for analysing polysomnographic sleep recordings, including EEG spindle and staging tools."),
        ],
    ),
    (
        "Spike sorting and electrophysiology",
        [
            ("Elephant", "NeuralEnsemble/elephant", "Electrophysiology analysis toolkit built on Neo, covering spike-train and LFP statistics."),
            ("Intan RHX", "Intan-Technologies/Intan-RHX", "Free data-acquisition software from Intan Technologies for displaying and recording signals from Intan hardware."),
            ("Kilosort", "MouseLand/Kilosort", "Fast spike-sorting algorithm with drift correction, developed by MouseLand."),
            ("MountainSort 5", "flatironinstitute/mountainsort5", "MountainSort spike-sorting algorithm, version 5, from the Flatiron Institute."),
            ("Neo", "NeuralEnsemble/python-neo", "Python package for representing electrophysiology data and reading many acquisition formats."),
            ("Open Ephys GUI", "open-ephys/plugin-GUI", "Modular software for processing, recording and visualising multichannel electrophysiology."),
            ("Open Ephys Python tools", "open-ephys/open-ephys-python-tools", "Python tools for interacting with the Open Ephys GUI and its data formats. Last push 2025-11-07."),
            ("phy", "cortex-lab/phy", "Interactive visualisation and manual curation tool for large-scale spike-sorted ephys data."),
            ("SpikeGLX", "billkarsh/SpikeGLX", "Recording-system GUI widely used with Neuropixels and National Instruments hardware. GitHub could not match a standard SPDX licence."),
            ("SpikeInterface", "SpikeInterface/spikeinterface", "Python framework for building flexible spike-sorting pipelines, with wrappers for many sorters."),
        ],
    ),
    (
        "BCI frameworks and paradigms",
        [
            ("BciPy", "CAMBI-tech/BciPy", "Python research software for building and running BCI experiments, from CAMBI."),
            ("Braindecode", "braindecode/braindecode", "Deep-learning library for decoding EEG, ECG and MEG signals."),
            ("EEGsynth", "eegsynth/eegsynth", "Modular system that converts real-time EEG into sound, music and visual effects."),
            ("MetaBCI", "TBC-TJU/MetaBCI", "Open-source platform for non-invasive BCI research, led by Tianjin University."),
            ("MOABB", "NeuroTechX/moabb", "Mother of All BCI Benchmarks, a framework for reproducible EEG decoding experiments."),
            ("pyRiemann", "pyRiemann/pyRiemann", "Machine learning for multivariate biosignals using the Riemannian geometry of covariance matrices."),
            ("Timeflux", "timeflux/timeflux", "Python framework for real-time biosignal processing and BCI applications. Last push 2024-12-04."),
        ],
    ),
    (
        "Neural decoding and machine learning",
        [
            ("CEBRA", "AdaptiveMotorControlLab/CEBRA", "Learnable latent embeddings for jointly analysing behavioural and neural data. GitHub could not match a standard SPDX licence."),
            ("NLB tools", "neurallatents/nlb_tools", "Python tools for the Neural Latents Benchmark, a challenge on inferring latent dynamics from neural population recordings."),
            ("pynapple", "pynapple-org/pynapple", "Lightweight Python library for analysing neurophysiological data, including tuning, decoding and sleep-related metrics."),
        ],
    ),
    (
        "Datasets and standards",
        [
            ("BIDS specification", "bids-standard/bids-specification", "The Brain Imaging Data Structure standard. It uses CC-BY-4.0, a content licence rather than a typical OSI software licence."),
            ("BIDS Validator", "bids-standard/bids-validator", "Validator for datasets that follow the Brain Imaging Data Structure."),
            ("DANDI CLI", "dandi/dandi-cli", "Command-line client for the DANDI archive of cellular neurophysiology data stored with NWB."),
            ("HDMF", "hdmf-dev/hdmf", "Hierarchical Data Modeling Framework used by NWB. GitHub could not match a standard SPDX licence."),
            ("OpenNeuro", "OpenNeuroOrg/openneuro", "Free platform for sharing and analysing neuroimaging datasets, typically in BIDS."),
            ("PyBIDS", "bids-standard/pybids", "Python tools for querying and manipulating BIDS datasets."),
            ("PyNWB", "NeurodataWithoutBorders/pynwb", "Python API for reading and writing data in the Neurodata Without Borders (NWB) format. GitHub could not match a standard SPDX licence."),
            ("WFDB Python", "MIT-LCP/wfdb-python", "Python toolkit for reading, writing and processing PhysioNet WFDB signals and annotations."),
        ],
    ),
    (
        "Neuroimaging",
        [
            ("ANTs", "ANTsX/ANTs", "Advanced Normalization Tools for medical image registration, segmentation and template building."),
            ("DIPY", "dipy/dipy", "Python library for diffusion MRI and other 3D/4D medical imaging analysis. GitHub could not match a standard SPDX licence."),
            ("fMRIPrep", "nipreps/fmriprep", "Robust, easily used pipeline for preprocessing diverse fMRI datasets."),
            ("FreeSurfer", "freesurfer/freesurfer", "Suite for neuroimaging analysis and visualisation, including cortical surface reconstruction. GitHub could not match a standard SPDX licence, and the project has long used a custom academic licence rather than an OSI licence, so read it before you use the software."),
            ("MRtrix3", "MRtrix3/mrtrix3", "Tools for advanced diffusion MRI analysis, including tractography and fibre-orientation estimation."),
            ("NiBabel", "nipy/nibabel", "Python package for reading and writing many neuroimaging file formats. GitHub could not match a standard SPDX licence."),
            ("Nilearn", "nilearn/nilearn", "Python library for statistical and machine-learning analysis of neuroimaging data."),
            ("Nipype", "nipy/nipype", "Python workflows and interfaces that connect neuroimaging packages into reproducible pipelines. GitHub could not match a standard SPDX licence."),
        ],
    ),
]


def k(n):
    if n >= 1e6:
        return f"{n/1e6:.2f}M"
    if n >= 1000:
        return f"{n/1000:.1f}k"
    return str(n)


def anchor(n):
    return n.lower().replace(",", "").replace(" ", "-")


def fact(text):
    return f'<span class="evi-fact">{text}</span>'


def estimate(text):
    return f'<span class="evi-est">{text}</span>'


def goal(text):
    return f'<span class="evi-goal">{text}</span>'


tools = [t for _, ts in C for t in ts]
missing = [t[1] for t in tools if t[1] not in S]
if missing:
    raise SystemExit(f"missing stats for: {missing}")

urls = [f"https://github.com/{t[1]}" for t in tools]
if len(urls) != len(set(urls)):
    raise SystemExit("duplicate GitHub URLs")

tot = sum(S[t[1]]["stars"] for t in tools)
forks = sum(S[t[1]]["forks"] for t in tools)
langs = sorted({S[t[1]]["lang"] for t in tools if S[t[1]]["lang"] not in ("", "none")})
active = sum(1 for t in tools if S[t[1]]["push"] >= ACTIVE_SINCE)

o = []
o.append(
    f"""<div align="center">

# Awesome Craft Neuro [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open-source tools for brain-computer interfaces, electrophysiology and neurotechnology.

<img src="assets/craft-neuro.svg" alt="Pixel-art neuroscience lab with a generic EEG cap, a monitor showing brain-wave traces, and connected neurons" width="100%">

![Tools](https://img.shields.io/badge/tools-{len(tools)}-6366f1?style=for-the-badge)
[![Categories](https://img.shields.io/badge/categories-{len(C)}-0ea5e9?style=for-the-badge)](#contents)
[![Combined stars](https://img.shields.io/badge/combined_stars-{k(tot)}-f59e0b?style=for-the-badge&logo=github)](#-leaderboard)
[![Stars](https://img.shields.io/github/stars/EdisonTKPcom/Awesome-Craft-Neuro?style=for-the-badge&color=22c55e)](https://github.com/EdisonTKPcom/Awesome-Craft-Neuro/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/EdisonTKPcom/Awesome-Craft-Neuro?style=for-the-badge&color=ec4899)](https://github.com/EdisonTKPcom/Awesome-Craft-Neuro/commits/main)

</div>

Open-source tools now cover much of the neural-data stack: board-level acquisition, streaming, EEG and MEG analysis, spike sorting, BCI experiment frameworks, neural decoding, shared datasets, and MRI pipelines. Every entry below has a public GitHub repository that was checked on {AS}. Check each project's licence before you use, modify or redistribute it.

**Ethics and medical safety:** nothing in this list is a medical device, a treatment, or clinical advice. Invasive brain-computer interfaces and implant hardware are subject to medical-device regulation, institutional review and surgical oversight. Consumer or research EEG hardware is not a diagnostic instrument. Do not treat company announcements, press photos or blog posts as evidence of safety or efficacy.

This snapshot of the [neuralink](https://github.com/neuralink) GitHub organisation found two public repositories, `tsui` (a Tailscale terminal UI) and `DicomPreview` (a macOS Quick Look plugin for DICOM files). Neither is implant or BCI software, so they are not listed as tools here. A public Neuralink compression-challenge repository was not found on that organisation. Published patient-count or milestone claims from companies are {goal("GOAL")} or company statements unless they come from a peer-reviewed paper or a regulator.

Official BCI2000 and OpenViBE distributions were not found as maintained public GitHub repositories in this snapshot, so they are not listed. The same is true for official POYO and Neural Data Transformer (NDT) source repositories.

Related list: [Awesome Craft](https://github.com/EdisonTKPcom/Awesome-Craft), open-source alternatives to popular SaaS tools.

## Contents
"""
)
o += ["- [Dashboard](#dashboard)"] + [f"- [{n}](#{anchor(n)})" for n, _ in C]
o.append("\n## Dashboard\n")
o.append(
    f"""<style>
.evi-fact{{border-bottom:3px solid #0f172a;padding-bottom:1px}}
.evi-goal{{border-bottom:3px dashed #0f172a;padding-bottom:1px}}
.evi-est{{border-bottom:3px dotted #0f172a;padding-bottom:1px}}
</style>

<table>
<tr>
<td align="center"><h2>{fact(str(len(tools)))}</h2>listed projects</td>
<td align="center"><h2>{fact(str(len(C)))}</h2>categories</td>
<td align="center"><h2>{estimate(k(tot))}</h2>combined GitHub stars</td>
<td align="center"><h2>{estimate(k(forks))}</h2>combined forks</td>
<td align="center"><h2>{estimate(f"{active}/{len(tools)}")}</h2>pushed in the last 30 days</td>
<td align="center"><h2>{fact(str(len(langs)))}</h2>languages</td>
</tr>
</table>

**Evidence tags**

<table>
<tr><th>Tag</th><th>Style</th><th>Meaning</th></tr>
<tr><td><span class="evi-fact">FACT</span></td><td>solid underline</td><td>A measured figure, with the source named.</td></tr>
<tr><td><span class="evi-goal">GOAL</span></td><td>dashed underline</td><td>A stated roadmap, plan or company claim, not a verified result.</td></tr>
<tr><td><span class="evi-est">ESTIMATE</span></td><td>dotted underline</td><td>A sum or count we computed from the facts.</td></tr>
</table>

The dashboard numbers themselves are FACT or ESTIMATE values from GitHub. This snapshot has no GOAL figures in the table above. Company claims about implants, patients or performance should be read as {goal("GOAL")} unless a paper or regulator is cited.

**Sources and method**

- Star counts, fork counts, licences, primary languages and last-push dates are {fact("FACT")} values from the GitHub Search and REST APIs on {AS} (`stargazers_count`, `forks_count`, `license.spdx_id`, `language`, `pushed_at`).
- Combined stars ({estimate(k(tot))}) and combined forks ({estimate(k(forks))}) are {estimate("ESTIMATE")}s: the arithmetic sum of those per-repository FACT counts, with no weighting and no unique-user deduplication. A person who stars two projects is counted twice.
- Pushed in the last 30 days ({estimate(f"{active}/{len(tools)}")}) is an {estimate("ESTIMATE")}: the number of listed repositories whose FACT `pushed_at` date is on or after {ACTIVE_SINCE}.
- Language and category counts, and the licence badges, are {estimate("ESTIMATE")}s of FACT fields. Star badges next to each entry update live and may differ from this snapshot.
"""
)
top = sorted(tools, key=lambda t: -S[t[1]]["stars"])[:10]
mx = S[top[0][1]]["stars"]
o.append(
    '### 🏆 Leaderboard\n\nStar counts in this table are FACT values from the snapshot. The bars are only a visual scale.\n\n<table>\n<tr><th>Rank</th><th>Project</th><th>Kind</th><th align="right">Stars</th><th></th></tr>'
)
kind = {t[1]: n for n, ts in C for t in ts}
for i, t in enumerate(top, 1):
    s = S[t[1]]["stars"]
    bar = "█" * max(1, round(s / mx * 20))
    medal = ["🥇", "🥈", "🥉"][i - 1] if i < 4 else i
    o.append(
        f'<tr><td align="center">{medal}</td><td><b>{t[0]}</b></td><td>{kind[t[1]]}</td><td align="right">{fact(k(s))}</td><td><code>{bar}</code></td></tr>'
    )
o.append("</table>\n")
o.append("\n### Stars by category\n")
o.append(
    "These category totals are ESTIMATE sums of the per-repository FACT star counts.\n\n```mermaid\npie showData\n    title Combined GitHub stars by category"
)
for n, ts in C:
    o.append(f'    "{n}" : {sum(S[t[1]]["stars"] for t in ts)}')
o.append("```\n")
lc = {}
for t in tools:
    L = LICNAME.get(S[t[1]]["lic"], S[t[1]]["lic"])
    lc[L] = lc.get(L, 0) + 1
o.append(
    "### Licences\n\n"
    + " ".join(
        f"![{L}](https://img.shields.io/badge/{U.quote(str(L).replace('-', '--'))}-{c}-64748b?style=flat-square)"
        for L, c in sorted(lc.items(), key=lambda x: -x[1])
    )
    + "\n\nThese badge counts are ESTIMATE tallies of the SPDX identifier GitHub returned for each repository. "
    + '"Custom" or "None" means GitHub could not match a standard SPDX licence. '
    + "The BIDS specification uses CC-BY-4.0, a content licence rather than a typical OSI software licence. "
    + "FreeSurfer has long used a custom academic licence rather than an OSI licence. "
    + "Read each project licence before you use it commercially or in a clinic.\n"
)
for n, ts in C:
    o.append(f"## {n}\n")
    for t in sorted(ts, key=lambda t: t[0].lower()):
        desc = t[2]
        if not desc.endswith("."):
            desc += "."
        o.append(
            f"- [{t[0]}](https://github.com/{t[1]}) - {desc} ![Stars](https://img.shields.io/github/stars/{t[1]}?style=flat-square&label=%E2%AD%90)"
        )
    o.append("")
o.append(
    "## Contributing\n\nContributions welcome! Read the [contribution guidelines](contributing.md) first.\n\n"
    '<div align="center">\n\n'
    "If this list helped you find a tool, give it a ⭐ so others can find it.\n\n"
    "</div>\n"
)
(ROOT / "README.md").write_text("\n".join(o))
print(
    f"wrote README.md tools={len(tools)} stars={tot} "
    f"forks={forks} langs={len(langs)} active={active}/{len(tools)}"
)
for n, ts in C:
    print(f"  {n}: {len(ts)}  stars={sum(S[t[1]]['stars'] for t in ts)}")
