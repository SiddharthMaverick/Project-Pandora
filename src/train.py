import torch
from torch.utils.data import DataLoader
from dataset import RetrosynFlowDataset
from model import UNet

dataset = RetrosynFlowDataset("../data/toy_products.txt")
loader = DataLoader(dataset, batch_size=1, shuffle=True)

model = UNet()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = torch.nn.MSELoss()  # flow matching loss

for epoch in range(5):
    for batch in loader:
        optimizer.zero_grad()
        x = batch['adj']  # 1 x N x N
        y = batch['delta']
        y_pred = model(x)
        loss = criterion(y_pred, y)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss={loss.item():.4f}")

torch.save(model.state_dict(), "../outputs/unn_model.pt")
