import torch
from dataset import RetrosynFlowDataset
from model import UNet
from graph_utils import graph_to_smiles, break_bonds_electron_flow, mol_to_graph
import numpy as np

dataset = RetrosynFlowDataset("../data/toy_products.txt")
model = UNet()
model.load_state_dict(torch.load("../outputs/unn_model.pt"))
model.eval()

predictions = []

for batch in dataset:
    G = mol_to_graph(batch['smiles'])
    adj_tensor = batch['adj']
    with torch.no_grad():
        delta_pred = model(adj_tensor.unsqueeze(0)).squeeze(0).numpy()
    # Convert ΔF to edge list to break
    edges = list(G.edges())
    flow = []
    for i, (u,v) in enumerate(edges):
        if delta_pred[u,v] > 0.5:
            flow.append((u,v))
    H = break_bonds_electron_flow(G, flow)
    smiles_pred = graph_to_smiles(H)
    predictions.append(smiles_pred)

print("Predicted reactants:", predictions)
