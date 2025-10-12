from rdkit import Chem
import networkx as nx
import numpy as np

def mol_to_graph(smiles: str) -> nx.Graph:
    mol = Chem.MolFromSmiles(smiles)
    G = nx.Graph()
    for atom in mol.GetAtoms():
        G.add_node(atom.GetIdx(), atomic_num=atom.GetAtomicNum())
    for bond in mol.GetBonds():
        G.add_edge(bond.GetBeginAtomIdx(), bond.GetEndAtomIdx(), bond_type=bond.GetBondType())
    return G

def graph_to_smiles(G: nx.Graph) -> str:
    mol = Chem.RWMol()
    idx_map = {}
    for i, (node, data) in enumerate(G.nodes(data=True)):
        idx_map[node] = mol.AddAtom(Chem.Atom(data['atomic_num']))
    for u, v, data in G.edges(data=True):
        mol.AddBond(idx_map[u], idx_map[v], data['bond_type'])
    try:
        return Chem.MolToSmiles(mol)
    except:
        return None

def electron_adjacency(G: nx.Graph) -> np.ndarray:
    n = G.number_of_nodes()
    adj = np.zeros((n, n))
    for u, v, data in G.edges(data=True):
        bond_order = 1
        if data['bond_type'] == Chem.rdchem.BondType.DOUBLE:
            bond_order = 2
        elif data['bond_type'] == Chem.rdchem.BondType.TRIPLE:
            bond_order = 3
        adj[u, v] = bond_order
        adj[v, u] = bond_order
    return adj

def compute_hessian_trace(adj: np.ndarray) -> np.ndarray:
    """Riemannian metric proxy: diagonal of Laplacian"""
    L = np.diag(adj.sum(axis=1)) - adj
    return np.diag(L)

def generate_electron_flow(G: nx.Graph, threshold=0.5) -> np.ndarray:
    """
    Return ΔF matrix: 1 where bond should break, 0 otherwise.
    Toy version: pick edges with trace > threshold
    """
    adj = electron_adjacency(G)
    trace = compute_hessian_trace(adj)
    n = G.number_of_nodes()
    delta_F = np.zeros((n, n))
    edges = list(G.edges())
    for idx, (u, v) in enumerate(edges):
        if idx < len(trace) and trace[idx] > threshold:
            delta_F[u, v] = 1
            delta_F[v, u] = 1
    if delta_F.sum() == 0 and edges:
        u, v = edges[0]
        delta_F[u, v] = 1
        delta_F[v, u] = 1
    return delta_F
