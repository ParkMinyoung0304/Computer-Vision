import torch
import torchvision
from torch.utils.data import DataLoader
from torch import nn
from torch.nn import Conv2d
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(root='./dataset/torch_data', train=False, transform=torchvision.transforms.ToTensor(), 
                                       download=True)

dataloader = DataLoader(dataset=dataset, batch_size=64)


class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__() #这里是为了继承父类的属性，谁继承谁，这里是继承nn.Module的属性
        self.conv1 = Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)
        
    def forward(self, x):
        x = self.conv1(x)
        return x


tudui = Tudui()
# print(tudui)

writer = SummaryWriter('./logs')


step =  0
for data in dataloader:
    imgs, targets = data
    output = tudui(imgs)
    print(output.shape)
    print(imgs.shape)
    writer.add_images('input', imgs, step)
    
    output = torch.reshape(output, (-1, 3, 30, 30))
    writer.add_images('output', output, step)
    step = step + 1