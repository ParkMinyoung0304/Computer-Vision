import torchvision
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

dataset_transform = transforms.Compose([
    transforms.ToTensor()
])  # Compose是将多个transform组合起来使用

train_set = torchvision.datasets.CIFAR10(root='./dataset/torch_data', train = True, transform=dataset_transform, download=True)
test_set = torchvision.datasets.CIFAR10(root='./dataset/torch_data', train = False, transform=dataset_transform, download=True)

# print(test_set[0][0])
# print(test_set.classes)

# img, target = test_set[0]
# print(img)
# print(target)
# print(test_set.classes[target])
# img.show()

# print(test_set[0])
writer = SummaryWriter("logs")
for i in range(10):
    img, target = test_set[i]
    writer.add_image("test_set", img, i)
    
writer.close()