from PIL import Image
import torchvision
from torch.utils.data import DataLoader
import torch.nn as nn
import torch


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


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

image_path = "imgs/airplane3.png"
image = Image.open(image_path).convert("RGB")
print(image)

transform = torchvision.transforms.Compose([torchvision.transforms.Resize((32, 32)), torchvision.transforms.ToTensor()])
image = transform(image).to(device)
print(image.shape)

image = torch.reshape(image, (1, 3, 32, 32)) # 1是batch_size，3是通道数，32是图片的长和宽
print(image.shape)

model = torch.load("model_pth/tudui_49.pth")
model = model.to(device)
print(model)

model.eval()
with torch.no_grad():
    output = model(image)
print(output)

print(torch.argmax(output, dim=1))