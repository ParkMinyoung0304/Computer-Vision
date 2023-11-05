import torch
import torch.nn as nn
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
# from model import *
import time

# 定义设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# 1、加载数据
train_data = torchvision.datasets.CIFAR10(root="./dataset/torch_data", train=True, transform=torchvision.transforms.ToTensor(),
                                            download=True)  
test_data = torchvision.datasets.CIFAR10(root="./dataset/torch_data", train=False, transform=torchvision.transforms.ToTensor(),
                                            download=True)

# 2、得到length 长度
train_data_size = len(train_data)
test_data_size = len(test_data)
print("训练集的长度为:{}".format(train_data_size))
print("测试集的长度为:{}".format(test_data_size))

# 3、利用dataloaders来加载数据
train_data_loader = DataLoader(train_data, batch_size=64)
test_data_loader = DataLoader(test_data, batch_size=64)

# 4、创建网络模型
class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, 1, 2), # 3是输入的通道数，32是输出的通道数，5是卷积核的大小，1是步长，2是padding
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(32, 32, 5, 1, 2),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.MaxPool2d(kernel_size=2),
            nn.Flatten(),
            nn.Linear(64*4*4, 64),
            nn.Linear(64, 10)
        )
        
    def forward(self, x):
        x = self.model(x)
        return x
    
    
tudui = Tudui()
tudui.to(device)

# 5、定义损失函数
loss_function = nn.CrossEntropyLoss()
loss_function.to(device)

# 6、定义优化器
# 1e-2 = 1 * 10 ^ (-2) = 0.01
learning_rate = 1e-2
optimizer = torch.optim.SGD(tudui.parameters(), lr=learning_rate)

# 7、设置训练网络的一些参数
total_train_step = 0
# 记录测试的次数
total_test_step = 0
# 训练的轮数
epoch = 20

#8、添加tensorboard
writer = SummaryWriter("./logs")

for i in range(epoch):
    print("--------第{}轮训练开始------------".format(i+1))
    for data in train_data_loader:
        start_time = time.time()
        imgs, targets = data
        imgs = imgs.to(device)
        targets = targets.to(device)
        outputs = tudui(imgs)
        loss = loss_function(outputs, targets)
        
        # 优化器调优模型
        # 梯度清零
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        total_train_step += 1
        if total_train_step % 100 == 0:
            end_time = time.time()
            #输出运行时间
            print("训练100次所用时间为:{}".format(end_time - start_time))
            print("训练次数：{}, Loss:{}".format(total_train_step, loss.item()))
            writer.add_scalar("train_loss", loss.item(), total_train_step)
            
    #测试步骤
    total_test_loss = 0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_data_loader:
            imgs, targets = data
            imgs = imgs.to(device)
            targets = targets.to(device)
            outputs = tudui(imgs)
            loss = loss_function(outputs, targets)
            total_test_loss += loss.item()
            accuracy = (outputs.argmax(1) == targets).sum()
            total_accuracy = accuracy + total_accuracy
            
    print("整体测试集上的Loss为:{}".format(total_test_loss))
    print("整体测试集上的正确率为:{}".format(total_accuracy / test_data_size))
    writer.add_scalar("test_loss", total_test_loss, total_test_step)
    writer.add_scalar("test_accuracy", total_accuracy / test_data_size, total_test_step)
    total_test_step += 1
    
    torch.save(tudui, "tudui_{}.pth".format(i))
    print("模型已保存")
    
writer.close()