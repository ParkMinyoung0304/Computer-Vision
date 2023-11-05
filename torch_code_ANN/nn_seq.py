import torch
from torch import nn
from torch.nn import Conv2d, Flatten, Linear, MaxPool2d, Sequential
from torch.utils.tensorboard import SummaryWriter


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
    

tudui = Tudui()
print(tudui)
#这里的ones代表的是输入的图片，64代表的是batch_size，3代表的是通道数，32代表的是图片的高度，32代表的是图片的宽度
input = torch.ones((64,3,32,32))
output = tudui(input)
print(output.shape)

writer = SummaryWriter('./logs')
writer.add_graph(tudui, input)
writer.close()