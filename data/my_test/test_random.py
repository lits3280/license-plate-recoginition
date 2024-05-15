# coding=utf-8
"""
@Author:lts
@Time:2024/3/29 10:43
@description:
"""
import random
import numpy as np
import cv2

def resize(img: 'np.ndarray', im_resize_w=100,size_stretch_p=0,size_stretch_rate_scope=(-0.2,0.1)):
    im_w, im_h = img.shape[1], img.shape[0]
    if im_resize_w == max(im_w,im_h):
        return img.copy()
    rate_h = 1.0 * im_resize_w / im_h
    rate_w = 1.0 * im_resize_w / im_w
    rate = min(rate_h, rate_w)

    output_w=int(rate * im_w)
    output_h=int(rate * im_h)
    if size_stretch_p>0 and  random.random()<size_stretch_p:
        h_rate_incr=round(random.uniform(size_stretch_rate_scope[0],size_stretch_rate_scope[1]),2)
        output_h = int((rate*(1+h_rate_incr)) * im_h)
    return cv2.resize(img, (output_w, output_h))



img=cv2.imdecode(np.fromfile(r'F:\tmp\plate\tmp18\plate_no_white_白_军牌_单层_字母_00_加背景/15_VV21696_单.jpg', dtype=np.uint8), -1)
print(img.shape)

for i in range(100):
    output_img=resize(img,im_resize_w=490,size_stretch_p=0.5,size_stretch_rate_scope=(-0.25,0.1))

    print(output_img.shape)

    # file_name=f'{output_img.shape[1]}x{output_img.shape[0]}'
    file_name=f'x'

    cv2.imwrite(f'F:/tmp/plate/random_size/{i+1}_{file_name}.jpg',output_img)