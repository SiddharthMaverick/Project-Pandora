# Project Pandora

**Open Source Software for Molecule Retrosynthesis using Riemannian Flow-Matching (OSS-MRRFM)**

## 🌌 Project Philosophy

Project Pandora is inspired by the mythological **Pandora’s Box**, symbolizing hidden possibilities waiting to be discovered. In chemistry, **retrosynthesis** is the process of uncovering the hidden reactants that can form a desired product.

This project combines:

- **Electron/Bond graph representations (Kekulé-style)**
- **Riemannian Flow-Matching**, a mathematical framework for smooth and constrained transformations
- **Backward generative modeling**, to predict reactants from products while obeying chemical conservation laws

The goal is **educational and research-oriented**, providing an open-source framework to explore **mechanistic retrosynthesis** with chemically valid vector fields.

## ⚙️ Key Features

- **Backward retrosynthesis**: Predict reactants from a product using a learned Riemannian flow.
- **Riemannian Flow Matching (RFM)**: Moves along a chemically valid manifold instead of naive Euclidean interpolation.
- **Bond–Electron (BE) representation**: Ensures electron conservation and valence rules are respected.
- **Toy and real SMILES support**: Run experiments on synthetic toy molecules or small real molecule sets (via RDKit).
- **Modular design**: Easy to extend or integrate new molecule representations or flow matching methods.
- **UNet-based flow prediction (FlowER-style)**: Predicts edge-level bond changes directly from adjacency/electron matrices.

## 📦 Installation

```bash
git clone https://github.com/SiddharthMaverick/Project-Pandora.git
cd RetrosynFlowER_UNN
pip install -r requirements.txt

```
---

## 🧪 Usage

- **Training**:

```bash
python src/train.py
```
- **Prediction**:

```bash
python src/predict.py

```

---


## 📜 License

This software is released under the **MIT License**.  
Copyright © 2025 Siddharth.


## 🛡 Authorship & Innovation Notice

This software, including its **UNet-based flow matching algorithms** for retrosynthesis, is authored and innovated by **Siddharth (2025)**.  

- Anyone using, reproducing, or distributing this code must **acknowledge this authorship**.  
- This repository serves as **public proof of creation date and innovation**, suitable for journals or establishing priority of invention.

