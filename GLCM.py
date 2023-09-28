import numpy as np
from skimage.feature import graycomatrix, graycoprops
import cv2
import  os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\方正粗黑宋简体.ttf", size=16) #导入本地汉字字库,pyplot显示中文

gray = np.random.randint(0,255,(10,10))
'''将图片的256阶化为 8个等级'''
gray_8 = (gray/32).astype(np.int32)

Glcm = graycomatrix(gray_8,[1],[0],levels=8)
Glcm_1 = Glcm.squeeze()

temp = graycoprops(Glcm,'ASM')

def cut_img_step(img,step):  # 每个块大小为20x20
    '''传入Gray 图片与 step'''
    new_img = [] #240x240
    for i in np.arange(0, img.shape[0] + 1, step):
        for j in np.arange(0, img.shape[1] + 1, step):
            if i + step <= img.shape[0] and j + step <= img.shape[1]:
                new_img.append(img[i:i + step, j:j + step])
    new_img = np.array(new_img, dtype=np.int32)
    return new_img

# 读取图片
pwd = os.getcwd() #获取当前路径
img = cv2.imdecode(np.fromfile("PATH_FILE/Image.jpg", dtype=np.uint8), -1)
# imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''将原图片的256阶化为 64个等级'''
level = 64
scale_data = 256/level

img_64= (img / scale_data).astype(np.int32)

plt.subplot(211)
plt.imshow(img,cmap='gray')
plt.title("256阶 675x1200",fontproperties=font)
plt.axis("off")
plt.subplot(212)
plt.imshow(img_64,cmap='gray')
plt.title("64阶 675x1200",fontproperties = font)
plt.axis("off")
plt.show()

'''获取整张图片的Glcm纹理 4个方向 0-》3/4 pi,64阶'''
img_glcm64 = graycomatrix(img_64, [1], [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4], levels=level)
'''将四个灰度共生矩阵对应相加后取
平均数得到影像的综合灰度共生矩阵'''
mean = []

for g_level1 in img_glcm64:
    for g_level2 in g_level1:
        for i in g_level2:
            mean.append(np.mean(i))

mean = np.array(mean)
'''Glcm_new 中保存了原图的Glcm4个方向的平均值'''
Glcm_new = mean.reshape(( level, level,1,1))# 后两个参数为步长数，方向数，计算特征需要

plt.subplot(211)
plt.imshow(img_64,cmap='gray')
plt.title("64阶 675x1200",fontproperties=font)
plt.axis("off")
plt.subplot(212)
plt.imshow(Glcm_new.reshape(level,level),cmap='gray')
plt.title("64阶Glcm 64x64",fontproperties = font)
plt.axis("off")
plt.show()

features = []
for prop in {'contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM'}:
    features.append(graycoprops(Glcm_new, prop))
print(features)
