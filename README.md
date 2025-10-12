# Project Pandora


**Open Source Software for Molecule Retrosynthesis using Riemannian Flow-Matching (OSS-MRRFM)**


---


## 🌌 Project Philosophy


Project Pandora is inspired by the mythological **Pandora’s Box**, symbolizing hidden possibilities waiting to be discovered. In chemistry, **retrosynthesis** is the process of uncovering the hidden reactants that can form a desired product.


This project combines:


- **Electron/Bond graph representations (Kekulé-style)**
- **Riemannian Flow-Matching**, a mathematical framework for smooth and constrained transformations
- **Backward generative modeling**, to predict reactants from products while obeying chemical conservation laws


The goal is **educational and research-oriented**, providing an open-source framework to explore **mechanistic retrosynthesis** with chemically valid vector fields.


---


## ⚙️ Key Features


- **Backward retrosynthesis**: Predict reactants from a product using a learned Riemannian flow.
- **Riemannian Flow Matching (RFM)**: Moves along a chemically valid manifold instead of naive Euclidean interpolation.
- **Bond–Electron (BE) representation**: Ensures electron conservation and valence rules are respected.
- **Toy and real SMILES support**: Run experiments on synthetic toy molecules or small real molecule sets (via RDKit).
- **Modular design**: Easy to extend or integrate new molecule representations or flow matching methods.


---


## 📦 Repository Structure
ProjectPandora/
├─ README.md # Project overview (this file)
├─ LICENSE # MIT License
├─ requirements.txt # Python dependencies
├─ data/
│ └─ toy_smiles.txt # Toy SMILES dataset for experiments
├─ src/
│ ├─ __init__.py
│ ├─ dataset.py # ToyReactionDataset + BE conversions
│ ├─ utils.py # Riemannian metric, vector field, BE helpers
│ ├─ model.py # RetroFlowModel + TimeEmbedding + Riemannian flow
│ ├─ train.py # Training loop with Riemannian conditional flow matching
│ └─ sample.py # Sampling / retrosynthesis inference
└─ examples/
└─ run_toy_retro.py # Demo for training + sampling

---


## 🛠 Installation


```bash
# Clone the repository
git clone https://github.com/yourusername/ProjectPandora.git
cd ProjectPandora


# Create a Python environment
python -m venv venv


# Activate environment
# Linux/macOS
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd)
venv\Scripts\activate


# Install dependencies
pip install -r requirements.txt


# Optional: install RDKit for real SMILES support (recommended for chemistry workflows)
conda install -c conda-forge rdkit
