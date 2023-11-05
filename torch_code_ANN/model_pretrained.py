import torchvision
from torchvision import transforms
from torch import nn
# train_data = torchvision.datasets.ImageNet(root='./dataset/imaget_net/', split='train', download=True, transform=transforms.ToTensor())

vgg16_false = torchvision.models.vgg16(pretrained=False)
vgg16_true = torchvision.models.vgg16(pretrained=True)
print(vgg16_true)

train_data = torchvision.datasets.CIFAR10(root='./dataset/torch_data/', train=True, download=True, transform=transforms.ToTensor())

#1、增加vgg16的module
# vgg16_true.add_module("add_linear", nn.Linear(1000, 10))
print(vgg16_true)
#2、增加vgg16的classifier的内容
vgg16_true.classifier.add_module("add_linear", nn.Linear(1000, 10))
print(vgg16_true)
#3、修改vgg16的classifier的内容
vgg16_false.classifier[6] = nn.Linear(4096, 10)
print(vgg16_false)