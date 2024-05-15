# coding=utf-8
"""
@Author:lts
@Time:2024/3/6 17:51
@description:
"""
import os
from PIL import Image

# 源码中220_1.jpg 的mode是"L"即灰度图片，会导致程序报错，需要修改为RGB格式
img1 = Image.open("../data/chinese/res/ne/220_1.jpg")
if img1.mode != 'RGB':
    img1 = img1.convert('RGB')
    # img1.save(os.path.join(os.path.dirname(__file__), "res/ne/220_1.jpg"))
    print(os.path.join(os.path.dirname(__file__)))
    img1.save("220_1.jpg")

