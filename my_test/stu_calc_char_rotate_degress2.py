# coding=utf-8
"""
@Author:lts
@Time:2024/3/12 17:15
@description:
"""

import cv2
import numpy as np

# 读取图像
image_path = "../rotate_degress.jpg"
image = cv2.imread(image_path)
orig_image = image.copy()

# 将图像转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用 Canny 边缘检测
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

cv2.imshow('xx',edges)
cv2.waitKey()
cv2.destroyAllWindows()

# 检测直线
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

# 计算直线的角度
angles = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    angle = np.arctan2(y2 - y1, x2 - x1) * 180.0 / np.pi
    angles.append(angle)

# 计算角度的中值
median_angle = np.median(angles)

# 输出估计的文本方向
print("估计的文本方向:", median_angle)

# 显示结果
cv2.imshow("Original Image", orig_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
