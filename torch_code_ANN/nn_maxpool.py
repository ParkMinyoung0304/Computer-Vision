import torch
from torch.nn import MaxPool2d
from torch import nn
from torch.utils.data import DataLoader
import torchvision
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(root='./dataset/torch_data', train=False, 
                                       transform=torchvision.transforms.ToTensor(),
                                        download=True)
dataloader = DataLoader(dataset=dataset, batch_size=64)

# input = torch.tensor([[1,0,2,3,1],
#                      [4,5,6,7,1],
#                      [8,9,10,11,1],
#                      [2,1,3,4,1],
#                      [2,4,3,6,4]])
# # 第一个1表示batch_size，第二个1表示通道数，5*5表示图像的大小，
# # batchsize是指一次性输入的图片数量，通道数是指图片的通道数，
# # 比如RGB就是3通道，灰度图就是1通道，图像大小就是指图像的长和宽，比如28*28，32*32等等
# input = torch.reshape(input, (1,1,5,5)) 
# print(input.shape)


class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.maxpool1 = MaxPool2d(kernel_size=3, stride=3, ceil_mode=False)
    
    def forward(self, input):
        output = self.maxpool1(input)
        return output
    

tudui = Tudui()

writer = SummaryWriter('./logs')
step = 0
for data in dataloader:
    imgs, targets = data
    writer.add_images('input', imgs, step)
    output = tudui(imgs)
    writer.add_images('output', output, step)
    step = step + 1

writer.close()
    

    
    