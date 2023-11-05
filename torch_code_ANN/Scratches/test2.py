import torch

outputs = torch.tensor([[0.2, 0.2, 0.3], [0.2, 0.3, 0.3]])

print(outputs.argmax(dim=1)) # dim=1表示按行取最大值，dim=0表示按列取最大值
preds = outputs.argmax(dim=1)
targets = torch.tensor([0, 2])
print(preds == targets)
