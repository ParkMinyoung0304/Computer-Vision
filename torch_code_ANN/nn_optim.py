import torch
import torchvision
import torchvision.transforms as transforms
from torch import nn
from torch.nn import (Conv2d, CrossEntropyLoss, Flatten, L1Loss, Linear,
                      MaxPool2d, MSELoss, Sequential)
from torch.utils.data import DataLoader
from torch.optim import SGD

dataset = torchvision.datasets.CIFAR10(root='./dataset/torch_data', train=False, download=True, transform=transforms.ToTensor())

dataloader = DataLoader(dataset=dataset, batch_size=1, drop_last=True)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.model1 = Sequential(
            Conv2d(3,32,5,padding=2),
            MaxPool2d(2),
            Conv2d(32,32,5,padding=2),
            MaxPool2d(2),
            Conv2d(32,64,5,padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024, 64),
            Linear(64, 10)
        )

    def forward(self, x):
        x = self.model1(x)
        return x


loss = nn.CrossEntropyLoss()
tudui = Tudui()
optim = SGD(tudui.parameters(), lr=0.01) #momentum是动量，weight_decay是权重衰减
for epoch in range(20):
    running_loss = 0.0
    for data in dataloader:
        imgs, targets = data
        output = tudui(imgs)
        result_loss = loss(output, targets)
        optim.zero_grad()
        result_loss.backward()
        optim.step()
        running_loss += result_loss
    print(running_loss)
