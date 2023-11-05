import torchvision
from torch.utils.data import DataLoader
import torch
from torch import nn
from torch.nn import Linear

dataset = torchvision.datasets.CIFAR10(root='./dataset/torch_data', train=False,
                                        transform=torchvision.transforms.ToTensor(),
                                        download=True)
dataloader = DataLoader(dataset=dataset, batch_size=64,drop_last=True) # drop_last=True表示如果最后一个batch不够64个，就扔掉

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.linear1 = nn.Linear(196608, 10)
    
    def forward(self, input):
        output = self.linear1(input)
        return output


tudui = Tudui()
step = 0

for data in dataloader:
    imgs, targets = data
    print(imgs.shape)
    # output = torch.reshape(imgs, (1,1,1,-1))#这里填-1是为了让程序自动计算，自动计算出代表的是多少个元素
    output = torch.flatten(imgs)
    print(output.shape)
    output = tudui(output)
    print(output.shape)