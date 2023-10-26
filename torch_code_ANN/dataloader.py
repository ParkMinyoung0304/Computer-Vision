import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

test_data = torchvision.datasets.CIFAR10(root='./dataset/torch_data', train=False, transform=torchvision.transforms.ToTensor(), download=True)

test_loader = DataLoader(dataset=test_data, batch_size=4, shuffle=False, num_workers=0, drop_last=True) # shuflle=True表示打乱数据

# Testing the first image and its target
img, target = test_data[0]
print(img.shape)
print(target)

writer = SummaryWriter("dataloader_logs")
for epoch in range(2):
    step = 0
    # Iterating through the data loader
    for data in test_loader:
        imgs, targets = data
        # print(imgs.shape)
        # print(targets)
        writer.add_images("Epoch:{}".format(epoch), imgs, step)
        step = step + 1

writer.close()