import torch
from torch import nn
from torch.nn import L1Loss
from torch.nn import MSELoss
from torch.nn import CrossEntropyLoss

inputs = torch.tensor([1, 2, 3], dtype=torch.float32)
targets = torch.tensor([1, 2, 5], dtype=torch.float32)

# inputs = inputs.reshape(inputs, (1, 1, 1, 3))
# targets = targets.reshape(targets, (1, 1, 1, 3))

loss = L1Loss(reduction='sum')
result = loss(inputs, targets)

loss_mse = nn.MSELoss()
result_mse = loss_mse(inputs, targets)

# print(result_mse)

x = torch.tensor([0.1, 0.2, 0.3, 0.4])
y = torch.tensor([1])
x = x.reshape(1, 4)
loss_cross = nn.CrossEntropyLoss()
result_cross = loss_cross(x, y)
print(result_cross)