# Project Pandora

**Open Source Software for Molecule Retrosynthesis using Riemannian Flow-Matching (OSS-MRRFM)**

---

## 🌌 Project Philosophy

Project Pandora is inspired by the mythological Pandora’s Box, symbolizing **hidden possibilities waiting to be discovered**. In chemistry, retrosynthesis is the process of **uncovering the hidden reactants** that can form a desired product.  

This project combines:
- **Electron/Bond graph representations (Kekulé-style)**
- **Riemannian Flow-Matching**, a mathematical framework for smooth and constrained transformations
- **Backward generative modeling**, to predict reactants from products while obeying chemical conservation laws

The goal is **educational and research-oriented**: providing an open-source, extensible framework to explore **mechanistic retrosynthesis** with physically consistent vector fields.

---

## ⚙️ Key Features

- **Backward retrosynthesis**: Predict reactants from a product using a learned Riemannian flow.
- **Riemannian Flow Matching (RFM)**: Moves along a chemically valid manifold instead of naive Euclidean interpolation.
- **Bond–Electron (BE) representation**: Ensures electron conservation and valence rules are respected.
- **Toy and real SMILES support**: Can run experiments on synthetic toy molecules or small sets of real molecules (via RDKit).
- **Modular design**: Easy to extend, integrate, or experiment with new molecule representations or flow matching ideas.

---

## 📦 Repository Structure

