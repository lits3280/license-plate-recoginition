# coding=utf-8
"""
@Author:lts
@Time:2024/3/6 15:27
@description:
"""

import cv2,os
import numpy as np
from PIL import Image
# img=cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_粤.jpg"), dtype=np.uint8), -1)
# img=cv2.imdecode(np.fromfile("F:/github_code/license-plate-recoginition/data/chinese/res/ne/220_粤.jpg", dtype=np.uint8), -1)
# img=cv2.imdecode(np.fromfile(r"F:\home\hanxiao\data\lp-data\train-white-jundui-6/20240307-white+jd-CU33468-1709805183245928.png", dtype=np.uint8), -1)
# #
# cv2.imshow('xx',img)
# #
# cv2.waitKey()

# Image.fromarray(img).show()
# Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)).show()



a=[1,2,3]

# print(np.array(a)*3)
#
# from data.chinese import black_plate
# draw=black_plate.Draw()
# clz=type(draw)
# print(clz)
# print(clz.__name__)
# print(clz.__module__)


from enum import Enum


class ArgsPlateType(Enum):
    black = '黑', None
    blue = '蓝', None
    yellow_single = '黄_单层', [1.0, 0.]  # [SINGLE, MULTI]
    yellow_multi = '黄_双层', [0., 1.]  # [SINGLE, MULTI]
    green = '绿', None
    farm = 'farm学', None
    white_jingcha = '白_警察', [0., 1., 0., 0., 0., 0., 0.]  # [COMMON,JINGCHA,JUNDUI,JUNDUI_M,WUJIN,WUJIN_M,YINGJI]
    white_jundui = '白_军队_单层', [0., 0., 1., 0., 0., 0., 0.]
    white_jundui_m = '白_军队_双层', [0., 0., 0., 1., 0., 0., 0.]
    white_wujing = '白_武警_单层', [0., 0., 0., 0., 1., 0., 0.]
    white_wujing_m = '白_武警_双层', [0., 0., 0., 0., 0., 1., 0.]
    white_yingji = '白_应急', [0., 0., 0., 0., 0., 0., 1.]
    airport = '空军', None


# for item in ArgsPlateType:
#     print(item.value[0])

prefix_chars = ['VA', 'VB', 'VC', 'VD', 'VE', 'VF', 'VG', 'VR', 'VT', 'VV', 'VK', 'VM', 'KA', 'KB', 'KC', 'KD', 'KR', 'KE', 'KF', 'KK', 'KU', 'KH', 'KG', 'KJ', 'KM', 'HA', 'HB', 'HC', 'HD', 'HE', 'HF', 'HG', 'HL', 'HR', 'BA',
                          'BB', 'BC', 'BD', 'BK', 'BM', 'BN', 'BR', 'BV', 'BY', 'NA', 'NB', 'NC', 'ND', 'NK', 'NM', 'NN', 'NR', 'NV', 'NY', 'GA', 'GB', 'GC', 'GD', 'GK', 'GJ', 'GM', 'GN', 'GR', 'GV', 'GY', 'SA', 'SB', 'SC', 'SD', 'SK',
                          'SM', 'SN', 'SR', 'SV', 'SY', 'CA', 'CB', 'CC', 'CD', 'CK', 'CM', 'CN', 'CR', 'CV', 'CY', 'LA', 'LB', 'LC', 'LD', 'LK', 'LM', 'LN', 'LR', 'LV', 'LY', 'JA', 'JB', 'JC', 'JD', 'JK', 'JM', 'JN', 'JR', 'JV', 'JY']

import random

char_counter_dict={}
for i in range(50000):
    c=random.choice(prefix_chars)
    cnt=char_counter_dict.get(c)
    cnt=cnt if cnt is not None else 0
    cnt+=1
    char_counter_dict[c]=cnt


sorted_data=[[k,v] for k,v in char_counter_dict.items()]
sorted_data.sort(key=lambda x:x[1],reverse=True)
for item in sorted_data:
    print(item)

print(len(prefix_chars),len(char_counter_dict))