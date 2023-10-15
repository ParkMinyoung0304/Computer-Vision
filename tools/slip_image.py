import io
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, transform, color
import cv2
from PIL import Image, ImageOps
from skimage import color

rough_image_dir='./rough_surface/JPEGImages/'
smooth_iamge_dir='./smooth_surface/JPEGImages/'
rough_label_dir='./rough_surface/SegmentationClassPNG/'
smooth_label_dir='./smooth_surface/SegmentationClassPNG/'

rough_image_slip_dir='./rough_surface_image_file/'
smooth_image_slip_dir='./smooth_surface_image_file/'
rough_label_slip_dir='./rough_surface_label_file/'
smooth_label_slip_dir='./smooth_surface_label_file/'

def slip_image(image_dir,slip_image_target_dir):
    filenames = os.listdir(image_dir)
    k=1
    l=1
    for i, filename in enumerate(filenames):
        image_path=os.path.join(image_dir,filename)
        image = Image.open(image_path)
        width, height = image.size

        '''裁剪(互不重叠)'''
        ruler_width = 85
        column_width =400
        num_columns =int((width - ruler_width) /column_width)
        print("num_columns:",num_columns)
        column_images =[]
        # 循环切割图片
        for j in range(num_columns):
            # 计算每一列的左上角和右下角坐标
            left = j * column_width + ruler_width
            upper = 0
            right = (j + 1) * column_width + ruler_width
            right = min(right, width)
            lower = height
            # 使用crop方法切割图片
            print(left, upper, right, lower)
            column_image = image.crop((left, upper, right, lower))
            # 仅保留宽度大于等于400像素的列图像
            if column_image.width >= 400:
                column_images.append(column_image)
            # # 将切割后的图片添加到列表中
            # column_images.append(column_image)
            # 保存切割后的每一列图片
        for j, column_image in enumerate(column_images):
            # 保存到指定slip_image_target_dir路径下，文件名为filename_j
            output_path = slip_image_target_dir + filename[:-4] + "_" + str(j) + ".jpg"
            # Convert 'P' mode image to 'RGB' mode and then save it as JPEG
            column_image_rgb = column_image.convert('RGB')
            column_image_rgb.save(output_path)
            print("图片" + str(k) + "保存成功")
            k += 1
                
def slip_image_with_stride(image_dir,slip_image_target_dir):
    filenames = os.listdir(image_dir)
    k=1
    for i, filename in enumerate(filenames):
        image_path=os.path.join(image_dir,filename)
        image = Image.open(image_path)
        width, height = image.size
 
        '''裁剪（设置固定步长）'''
        column_width = 400
        stride = 100
        # num_columns=int(board_width/column_width)
        column_images = []
        # 循环切割图片
        for left in range(85, width, stride):
            # 计算裁剪的右边界
            right = min(left + column_width, width)
            # 使用crop方法裁剪列图像
            column_image = image.crop((left, 0, right, height))
            # 仅保留宽度大于等于400像素的列图像
            if column_image.width >= 400:
                column_images.append(column_image)
            # 保存切割后的每一列图片
            for j, column_image in enumerate(column_images):
                output_path = slip_image_target_dir + filename[:-4] + "_" + "100" + "_" + str(j) + ".jpg"
                # Convert 'P' mode image to 'RGB' mode and then save it as JPEG
                column_image_rgb = column_image.convert('RGB')
                column_image_rgb.save(output_path)
                # print("图片类别" + str(j) + "保存成功")

# 将8条路径两组两组代入两个函数
slip_image(rough_image_dir,rough_image_slip_dir)
slip_image(smooth_iamge_dir,smooth_image_slip_dir)
slip_image(rough_label_dir,rough_label_slip_dir)
slip_image(smooth_label_dir,smooth_label_slip_dir)

slip_image_with_stride(rough_image_dir,rough_image_slip_dir)
slip_image_with_stride(smooth_iamge_dir,smooth_image_slip_dir)
slip_image_with_stride(rough_label_dir,rough_label_slip_dir)
slip_image_with_stride(smooth_label_dir,smooth_label_slip_dir)


