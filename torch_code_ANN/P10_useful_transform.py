from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter
writer=  SummaryWriter("logs")
img = Image.open("dataset/7_slip_image/rough_surface_image_file/500153S01_0.jpg")
print(img) 

#ToTensor
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
writer.add_image("ToTensor", img_tensor)


#Normalize
print(img_tensor[0][0][0])
trans_normalize = transforms.Normalize([1,0.5,1],[0.5,2,0.5]) #括号内两个参数分别是均值和标准差，三个值分别对应三个通道
img_normalize = trans_normalize(img_tensor)
print(img_normalize[0][0][0])
writer.add_image("Normalize", img_normalize,2)


# Resize
print(img.size)
trans_resize = transforms.Resize((100, 100))
img_resize = trans_resize(img)
img_resize = trans_totensor(img_resize)
print(img_resize)
writer.add_image("Resize", img_resize, 3)
print("++++++++++++++++++++")
print(type(img_resize))

# Compose - resize - 2
trans_resize_2 = transforms.Resize(512) #512是最长边的长度
trans_compose = transforms.Compose([trans_resize_2, trans_totensor])
img_resize_2 = trans_compose(img)
writer.add_image("Compose", img_resize_2, 4)

# RandomCrop
trans_random = transforms.RandomCrop((100,200))
trans_compose_2 = transforms.Compose([trans_random,trans_totensor])
for i in range(10):
    img_crop = trans_compose_2(img)
    writer.add_image("RandomCropHW", img_crop, i)



writer.close()