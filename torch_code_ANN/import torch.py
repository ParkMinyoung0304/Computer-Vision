from torch.utils.tensorboard import SummaryWriter
from PIL import Image
from torchvision import transforms
# import cv2
img_path = "dataset/7_slip_image/rough_surface_image_file/500153S01_0.jpg"
img = Image.open(img_path)

writer = SummaryWriter("logs")

tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)

writer.add_image("Tensor_img", tensor_img)

writer.close()
# cv_img = cv2.imread(img_path)