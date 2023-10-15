import cv2
import numpy as np

#空白图像的宽度是60，高度是2550，每一厘米的刻度线长度是10，每一厘米的刻度线间隔是10，总刻度数是150
#卷尺的宽度是60，高度是2550，每一厘米的刻度线长度是10，每一厘米的刻度线间隔是10，总刻度数是150
# 创建一张空白图像，宽度足够容纳卷尺
image_width = 85# 根据需要调整宽度
image_height = 2550  # 根据需要调整高度
image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
image.fill(255)  # 设置背景为白色

# 添加刻度
scale_length = 10  # 每一厘米的刻度线长度
long_scale_length=20
scale_interval =10  # 刻度之间的间隔
num_scales = 150  # 总刻度数

# 绘制矩形框线
border_color = (0, 0, 0)  # 框线颜色为黑色
border_thickness = 1  # 框线线宽
cv2.rectangle(image, (0, 0), (image_width - 1, image_height - 1), border_color, border_thickness)

for i in range(num_scales + 1):
    x1 = 0  # 刻度线起始点横坐标
    y1 = i * (image_height - scale_length) // num_scales+1  # 计算刻度线起始点纵坐标
    x2 = x1 + scale_length  # 刻度线结束点横坐标

    # 判断是否为刻度值为10的倍数
    is_multiple_of_10 = i % 10 == 0
    is_multiple_of_5 = (i % 5 == 0) and (i != 0)

    # 设置刻度线颜色
    line_color = (0, 0, 0)  # 黑色
    if is_multiple_of_10:
        line_color = (0, 0, 255)  # 红色
    # 根据是否为整十刻度设置刻度线长度
    if is_multiple_of_10:
        scale_length_to_use = 2 * scale_length  # 整十刻度长度为原来的两倍
    else:
        scale_length_to_use = scale_length

    # 每五个刻度显示刻度值
    if is_multiple_of_5:
        scale_value = str(i)
        text_x = x2 + 10  # 刻度值文本的横坐标
        text_y = y1 + scale_length // 2  # 刻度值文本的纵坐标
        cv2.line(image, (x1, y1), (x2, y1), line_color, 2)
        cv2.putText(image, scale_value, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, line_color, 1, cv2.LINE_AA)
    else:
        cv2.line(image, (x1, y1), (x2, y1), line_color, 1)

cv2.imwrite('soil_profile_with_scale.jpg', image)

# 显示图像
cv2.imshow('Ruler Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
