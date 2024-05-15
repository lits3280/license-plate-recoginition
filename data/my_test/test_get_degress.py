# coding=utf-8
"""
@Author:lts
@Time:2024/3/12 16:09
@description:
"""
from typing import Union
import numpy as np
import cv2
import os
import math, random
from PIL import Image, ImageDraw, ImageFont
import glob
from torchvision import transforms
from shapely.geometry import Polygon
from torchvision.transforms import functional as F
from torch import Tensor


class RandomAffine(transforms.RandomAffine):

    def __init__(self, degrees, translate=None, scale=None, shear=None, interpolation=transforms.InterpolationMode.NEAREST, fill=0, center=None):
        super().__init__(degrees, translate, scale, shear, interpolation, fill, center)
        self.ret=None

    def forward(self, img):
        """
            img (PIL Image or Tensor): Image to be transformed.

        Returns:
            PIL Image or Tensor: Affine transformed image.
        """
        fill = self.fill
        channels, height, width = F.get_dimensions(img)
        if isinstance(img, Tensor):
            if isinstance(fill, (int, float)):
                fill = [float(fill)] * channels
            else:
                fill = [float(f) for f in fill]

        img_size = [width, height]  # flip for keeping BC on get_params call

        ret = self.get_params(self.degrees, self.translate, self.scale, self.shear, img_size)
        self.ret=ret

        return F.affine(img, *ret, interpolation=self.interpolation, fill=fill, center=self.center)


import random

provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新"]
ads = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ads=[ads]*6

def random_plateno():
    gen_chars=[provinces]+ads
    plate_no_chars=[random.choice(x) for x in gen_chars ]
    return ''.join(plate_no_chars)


def sort_four_points(points: 'list', clockwise=True):
    # 计算四个点的质心
    centroid = np.mean(points, axis=0)
    ndarray_points = np.array(points)
    # 计算四个点相对于质心的角度
    angles = np.arctan2(ndarray_points[:, 1] - centroid[1], ndarray_points[:, 0] - centroid[0])
    # 按照角度进行排序
    sorted_indices = np.argsort(angles)
    if not clockwise:
        sorted_indices = sorted_indices[::-1]
    # sorted_points = points[sorted_indices]
    sorted_points = [points[x] for x in sorted_indices]

    # 取中心点上面x最小的作为第一个点
    upper_points = [x for x in sorted_points if x[1] < centroid[1]]
    upper_points.sort(key=lambda x: x[0])

    i = points.index(upper_points[0])

    return sorted_points[i:] + sorted_points[0:i]


def draw_outline(img, four_points_list: 'list'):
    new_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    for four_points in four_points_list:

        # # print(points)
        # points=[[ 63 ,27],[93, 33],[18,84],[ 4 ,69]]
        _box = np.array(four_points).astype(np.int32).reshape(-1, 2)
        cv2.polylines(new_img, [_box], isClosed=True, color=(0, 0, 255), thickness=2)

        for i, (x, y) in enumerate(four_points):
            cv2.putText(new_img, str(i + 1), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)  # 蓝色

    output_img = Image.fromarray(cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))
    # 写中文文字
    # draw = ImageDraw.Draw(output_img)  # 图片上打印
    # font = ImageFont.truetype('C:\Windows\Fonts\SIMYOU.TTF', 30, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
    # centor = np.mean(four_points_list[0], axis=0)-50
    # draw.text((centor[0], centor[1]), 'KA123456', (255, 0, 0), font=font, align='left', stroke_width=1)

    return output_img



img = Image.new('RGB', (800, 800), color=(255, 255, 255))
points = [(200, 300), (600, 300), (600, 500), (200, 500)]

img = draw_outline(img, [points])

cv2.imshow('x', cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
cv2.waitKey()
cv2.destroyAllWindows()

# degrees = (-180, 180)
degrees = (0, 360)
translate = (0, 0.2)
# scale=(1, 1) #比例因子区间，例如（a，b），则从范围a<=比例<=b中随机采样比例。默认情况下，将保留原始比例。
scale = None
# fillcolor = (0, 0, 255)
shear = 30  # 可从中选择的度数范围。放射变换的角度
# shear = None  # 可从中选择的度数范围。放射变换的角度
# fill = (0, 125, 0)
fill = 0
# transform_affine = transforms.RandomAffine(degrees=degrees, translate=None, scale=None, shear=shear, fill=fill, interpolation=transforms.InterpolationMode.BILINEAR)
transform_affine = RandomAffine(degrees=degrees, translate=None, scale=None, shear=shear, fill=fill, interpolation=transforms.InterpolationMode.BILINEAR)

rotate_img = transform_affine(img)
_angle, _translations, _scale, _shear=transform_affine.ret
print(_angle)
#
# # 将PIL图像转换为numpy数组
# image_np = np.array(rotate_img)
#
# # 查找非白色像素的位置
# non_white_pixels = np.where(image_np != 0)
#
# # 计算旋转角度的平均值
# rotation_angle = -np.arctan2(np.mean(non_white_pixels[0] - image_np.shape[0] / 2),
#                              np.mean(non_white_pixels[1] - image_np.shape[1] / 2)) * 180 / np.pi
#
# print("实际旋转角度:", rotation_angle)
rotate_img.save("rotate_degress.jpg")
cv2.imshow(f'xxx', cv2.cvtColor(np.array(rotate_img), cv2.COLOR_RGB2BGR))
cv2.waitKey()
cv2.destroyAllWindows()
