import torch
from torch_geometric.nn import GCNConv

class FlowMatchingGNN(torch.nn.Module):
    """
    Flow-matching GNN predicting bond-breaking probability per node.
    """
    def __init__(self, node_feature_dim=1, hidden_dim=32):
        super().__init__()
        self.conv1 = GCNConv(node_feature_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim)
        self.fc = torch.nn.Linear(hidden_dim, 1)

    def forward(self, x, edge_index):
        h = torch.relu(self.conv1(x, edge_index))
        h = torch.relu(self.conv2(h, edge_index))
        return torch.sigmoid(self.fc(h))
