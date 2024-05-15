# coding=utf-8
"""
@Author:lts
@Time:2024/3/29 10:11
@description:
"""
import glob

from PIL import Image

from matplotlib import pyplot as plt

img_dir=r'D:\临时文件夹\tmp\plate_class_imgs_junyong'
# img_dir=r'F:\tmp\plate\random_size'
# img_dir=r'F:\tmp\plate\tmp19\plate_no_white_白_军牌_单层_中文_00_加背景'

print(img_dir)


img_files=glob.glob(f'{img_dir}/*.jpg')

rate_list=[]
for i,f in enumerate(img_files):
    img=Image.open(f)
    w,h=img.size
    # print(img.size)
    rate_list.append([i,round(w/h,3)])
x=[x[0] for x in rate_list]
y=[x[1] for x in rate_list]
plt.scatter(x,y)
plt.show()

corp_size=int(round(0.1*len(y)))
crop_y=y[corp_size:-corp_size]
print(len(y),len(crop_y))
print(f'avg_rate:{sum(crop_y)/len(crop_y)}')