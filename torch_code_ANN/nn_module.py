import torch
from torch import nn

class Tudui(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, input):
        output = input + 1
        return output
    
    def backward(self, input):
        output = input - 1
        print("+++++++++++++++++++++++")
        return output


tudui = Tudui()
x = torch.tensor(1.0) #requires_grad=True表示需要计算梯度
output = tudui(x)
print(output)