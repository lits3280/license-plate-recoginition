# coding=utf-8
"""
@Author:lts
@Time:2024/3/12 17:15
@description:
"""

import cv2
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:/Program Files/Tesseract-OCR/tesseract.exe'
# 读取图像
image_path = "../rotate_degress.jpg"
# image_path = "11.png"
image = cv2.imread(image_path)
# orig_image = image.copy()
# # 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 使用 pytesseract 库来识别文字
text = pytesseract.image_to_string(image_path,lang='eng+chi_sim',config='')
# text = pytesseract.image_to_string(Image.open(image_path),lang='eng+chi_sim',config='-c min_characters_to_try=5')
# text = pytesseract.image_to_string(gray,lang='chi_sim',config='--psm 0 -c min_characters_to_try=5')

# tessdata_config = r'--tessdata-dir "D:/Program Files/Tesseract-OCR" min_characters_to_try=5'
# text = pytesseract.image_to_string(Image.open(image_path),config=tessdata_config)

# 输出识别的文字内容
print("识别的文字内容:", text)

# 使用 pytesseract 库来识别文字区域的方向
orientation = pytesseract.image_to_osd(Image.open(image_path),lang='eng+chi_sim',config='--dpi 300')

# 提取文字方向
angle = orientation.split('\n')[1].split('Rotation: ')[-1]

# 将角度转换为浮点数

# 输出识别的文字方向
print("识别的文字方向:", angle)

# 显示结果
# cv2.imshow("Original Image", orig_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()