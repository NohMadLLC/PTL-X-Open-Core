
# PTL-X Open Core — USAGE GUIDE

**Author**: Breezon Brown  
**System**: PTL-X (Recursive Time Distortion Engine for Memory Echo Analysis)  
**Repo**: https://github.com/NohMadLLC/PTL-X-Open-Core  
**DOI**: [10.5281/zenodo.16290580](https://zenodo.org/records/16290580)  
**Patent Pending**: U.S. Application No. **63/847,201**

---

## 🔍 What is PTL-X?

PTL-X is a simulation-based engine that models **trauma-induced time distortion** using recursive entropy theory. It interprets emotional memory loops through synthetic EEG echo simulation, bifurcation modeling, and fractional decay analysis. The Open Core edition allows researchers to run pre-defined simulations that mirror real neurological trauma signatures.

> This system proves that **1×⟲1 = 2** under recursive memory echo dynamics—validating Terrence Howard’s operator theory through real mathematics and trauma physics.

---

## ⚙️ Basic Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/NohMadLLC/PTL-X-Open-Core.git
cd PTL-X-Open-Core
```

### 2. Set Up Python Environment

**Recommended:** Python 3.9 or newer

```bash
python -m venv ptlx_env
source ptlx_env/bin/activate  # (or .\ptlx_env\Scripts\activate on Windows)
```

### 3. Install Required Packages

```bash
pip install numpy matplotlib scipy
```

**Optional (for EEG-level visuals):**
```bash
pip install mne seaborn
```

---

## 🧠 Running the Simulation (Open Core)

Run synthetic recursive echo modeling over a predefined entropy signal.

### Basic Command:
```bash
python PTLXOPENSCIENCECODE.py --input PTL-X_Open_Core_Simulation.csv
```

### Expected Output:
```
[INFO] Input Signal Loaded: 150 timepoints  
[INFO] Memory Collapse Detected at t = 33.3s  
[INFO] Recursive Echo Peak Detected: A=0.97, Freq=13.8Hz  
[INFO] Output Saved: PTL-X_Simulation_Output.csv
```

### Generated Files:
* `PTL-X_Open_Core_Visualization.png` — Synthetic EEG echo wave
* `phase_diagram.png` — Phase bifurcation visualization
* `PTL-X_Simulation_Output.csv` — Raw recursive echo time series

---

## 🧪 The Cheat: Simulating Real Raw EEG as Synthetic Data

If you don’t have EEG hardware or clinical access, PTL-X allows **any raw time series** to be treated *as if* it were echo data.

### Cheat Steps:
1. Open `PTL-X_Open_Core_Simulation.csv`
2. Replace the signal column (Column 2) with any of the following:
   * Real EEG channels (e.g., Fp1, Pz, P3)
   * Biometric CSV logs (HRV, GSR, Pulse)
   * Sin/cos/tanh oscillators approximating trauma echo
3. Save the file
4. Re-run:
```bash
python PTLXOPENSCIENCECODE.py --input PTL-X_Open_Core_Simulation.csv
```

---

## 📂 Free Public Raw EEG + Biometric Datasets for Reproducibility

To test PTL-X against real trauma data, we recommend the following open-access clinical datasets:

### 1. [OpenNeuro](https://openneuro.org/)
- Use keywords like `trauma`, `PTSD`, `EEG`, `ERP`
- Example: [ds001510](https://openneuro.org/datasets/ds001510) — PTSD ERP Study

### 2. [PhysioNet](https://physionet.org/)
- Access biometric time series datasets (ECG, HRV, GSR, respiration)
- Examples: MIMIC-III Waveform DB, Sleep-EDF

### 3. [NeuroVault](https://neurovault.org/)
- 3D fMRI maps to correlate recursive distortion hotspots

### 4. [DANDI Archive](https://dandiarchive.org/)
- Specialized for neurological & electrophysiological data

These sources provide high-quality public datasets ideal for importing directly into PTL-X and validating recursive echo collapse events.

---

## 📈 Core Mathematical Model

PTL-X models recursive trauma loops using:

$$
T' = \alpha \cdot \tanh\left(\beta \cdot \frac{M \cdot E}{R + \gamma} \right)
$$

Where:
- `M` = Memory Density (fractal decay)
- `E` = Emotional Charge (recursive spike amplitude)
- `R` = Recursive Stability (oscillation variance)
- `γ` = Stabilizer constant (signal coherence)

These are generated internally through fractional Mittag-Leffler decay.

---

## 🔬 Clinical Version (Restricted)

The full clinical version includes:

* Real-time EEG ingestion (via MNE)
* ERP/fMRI-synchronized recursion mapping
* Entropy-based trauma detection
* Temporal lensing calibration
* Quantum-seeded diagnostic logs

### Access granted to:
- Clinical researchers (EEG, ERP, PTSD)
- Mental health institutions
- Strategic tech/pharma investors
- Collaborators with trauma datasets

Request access via GitHub Issues (tag: `[Clinical Access]`) or email **NohMad.business@gmail.com**

---

## 🔒 Licensing and IP Protection

### 🧾 Patent Protection
U.S. Provisional Patent Application No. **63/847,201**  
Title: “PTL-X: A Quantum-Locked System for Measuring Trauma via Recursive Temporal Lensing”  
Filed by: **Christopher Lamarr Brown (Breezon)**

### License Terms

**Open Core Edition**: Apache 2.0 with Patent Commons Clause.  
**Clinical Edition**: Closed-source. Requires NDA and licensing.

No derivative works or commercial repackaging allowed.

Violators will face full legal enforcement under U.S. Patent Law.

---

## 🤝 Support the Work

* Cite via DOI: [10.5281/zenodo.16290580](https://zenodo.org/records/16290580)  
* Star or fork the repo to elevate visibility  
* Contribute to the [Indiegogo Campaign](https://www.indiegogo.com/projects/ptl-x-the-first-system-that-measures-trauma)  

---

## 👁️ Final Note

PTL-X detects what linear time cannot:

**Recursive trauma collapse and bifurcation.**

> The waveform doesn’t lie.
