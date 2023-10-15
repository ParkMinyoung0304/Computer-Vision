import io
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, transform, color
import cv2
from PIL import Image, ImageOps
from skimage import color

ori_image_dir = ''
smooth_surface_dir = ''
rough_surface_dir = ''

# 取出文件夹下所有的文件名
ori_image_dir_filenames = os.listdir(ori_image_dir)
smooth_surface_dirfilenames = os.listdir(smooth_surface_dir)

k = 1
l = 1
ori_jpg_files = [filename for filename in ori_image_dir_filenames if filename.endswith('.jpg')]

for i, ori_image_jpg in enumerate(ori_jpg_files):
    ori_image_path = os.path.join(ori_image_dir, ori_image_jpg)
    smooth_surface_path = os.path.join(smooth_surface_dir, ori_image_jpg)
    
    ori_image = Image.open(ori_image_path)
    smooth_surface_image = Image.open(smooth_surface_path)
    
    ori_image_width, ori_image_height = ori_image.size
    smooth_surface_image_width, smooth_surface_image_height = smooth_surface_image.size
    
    '''裁剪(互不重叠)'''
    column_width = smooth_surface_image_width
    column_images = []
    # 计算每一列的左上角和右下角坐标
    left = 0
    upper = 0
    right = ori_image_width - smooth_surface_image_width - 7
    lower = ori_image_height
    # 使用crop方法切割图片
    column_image = ori_image.crop((left, upper, right, lower))
    # # 将切割后的图片添加到列表中
    # column_images.append(column_image)
    # 保存切割后的每一列图片
    output_path = rough_surface_dir+ ori_image_jpg# 替换为你想要保存的路径
    column_image.save(output_path)
    print("图片" + str(k) + "保存成功")
    k += 1