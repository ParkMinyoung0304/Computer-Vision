import io
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, transform, color
import cv2
from PIL import Image, ImageOps
from skimage import color

# 同时处理多张图片，每张图片的目标高度不一样，设置一个数组循环遍历处理每一张图片
image_dir=''
filenames = os.listdir(image_dir)
target_heights=[137,42,131,135,95,138,107]
k = 1
l=1
for i, filename in enumerate(filenames):
    target_height = target_heights[i]*17
    image_path=os.path.join(image_dir,filename)
    image = Image.open(image_path)
    width, height = image.size

    ratio = target_height / height
    target_width = int(width * ratio)
    resized_image = image.resize((target_width, target_height))

    # resize后的图片放在一个指定高度大小的白色模板中
    # 获取resize后图片的宽高
    resize_width,resize_height=resized_image.size
    # 指定白板的宽度和高度
    board_width=target_width
    board_height=resize_height

    # # 创建一个蓝色板
    # blue_color=(0,0,0)
    # white_board = Image.new("RGB", (board_width, board_height), blue_color)
    # 创建一个白板
    white_board = Image.new("RGB", (board_width, board_height), "white")

    # 将图片粘贴到白板上
    white_board.paste(resized_image, (0, 0))

    # 保存合成后的图像,图片名仍然是原名
    output_path = f""
    white_board.save(output_path)







