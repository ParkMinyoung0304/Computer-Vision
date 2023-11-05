import torch
from torch import nn
from torch.nn import ReLU
from torch.utils.data import DataLoader
import torchvision
from torch.nn import Sigmoid
from torch.utils.tensorboard import SummaryWriter

# input = torch.tensor([[1,0],
#                     [4,5]])

# output = torch.reshape(input, (1,1,2,2))
# print(output.shape)

dataset = torchvision.datasets.CIFAR10(root='./dataset/torch_data', train=False, 
                                       transform=torchvision.transforms.ToTensor(),
                                        download=True)

dataloader = DataLoader(dataset=dataset, batch_size=64)


class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.relu1 = ReLU()
        self.sigmoid1 = Sigmoid()
    
    def forward(self, input):
        # output = self.relu1(input)
        output = self.sigmoid1(input)
        return output
    
    
tudui = Tudui()
# output = tudui(input)
# print(output)
writer = SummaryWriter('./logs')
step = 0
for data in dataloader:
    imgs, targets = data
    writer.add_images('input', imgs, step)
    output = tudui(imgs)
    writer.add_images('output', output, step)
    step = step + 1