from torch.utils.data import Dataset
from graph_utils import mol_to_graph, generate_electron_flow, electron_adjacency
import torch
import numpy as np

class RetrosynFlowDataset(Dataset):
    """
    Product -> reactant dataset for UNet flow matching
    """
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            self.products = [line.strip() for line in f.readlines()]

    def __len__(self):
        return len(self.products)

    def __getitem__(self, idx):
        smiles = self.products[idx]
        G = mol_to_graph(smiles)
        adj = electron_adjacency(G)
        delta_F = generate_electron_flow(G)  # Target ΔF
        # convert to torch tensor
        adj_tensor = torch.tensor(adj, dtype=torch.float32).unsqueeze(0)  # 1 x N x N
        delta_tensor = torch.tensor(delta_F, dtype=torch.float32).unsqueeze(0)
        return {"adj": adj_tensor, "delta": delta_tensor, "smiles": smiles}
