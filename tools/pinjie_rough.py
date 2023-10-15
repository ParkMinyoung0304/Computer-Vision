import os
import cv2
import numpy as np
from PIL import Image, ImageOps
from matplotlib import pyplot as plt
image_dir=''
filenames = os.listdir(image_dir)#获取文件夹下所有文件名

image1_path = os.path.join('soil_profile_with_scale.jpg')
image1 = Image.open(image1_path)
width1, height1 = image1.size

image_original = image1.copy()

for i, filename in enumerate(filenames):
    image_path = os.path.join(image_dir, filename)#获取文件路径
    image2 = Image.open(image_path)
    width2, height2 = image2.size
    image1 = image_original.copy()
    
    # 将尺子图像的高度调整为和图片1一样的高度
    image1 = image1.crop((0, 0, width1, height2))
    
    # 创建一个白板（空白图像），高度是图片2的高度，宽度是图片2的宽度，这样尺子才能覆盖到图片2上
    combined_image = np.zeros((height2, width2+width1, 3), dtype=np.uint8)
    combined_image.fill(255)  # 设置背景为白色

    # 将新图像放在画布上
    combined_image[:height2, width1:width1 + width2] = np.array(image2)
    combined_image = cv2.cvtColor(combined_image, cv2.COLOR_BGR2RGB)
    
    # 将基础图像放在画布的左侧
    combined_image[:height2, :width1] = image1
    
    # 保存拼接后的图片
    output_filepath = f"{filename}"
    cv2.imwrite(output_filepath, combined_image)