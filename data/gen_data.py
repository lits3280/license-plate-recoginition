'''
Date: 2022-01-05 22:53:34
Author: ChHanXiao
Github: https://github.com/ChHanXiao
LastEditors: ChHanXiao
LastEditTime: 2022-01-22 22:16:35
FilePath: /license-plate-recoginition/gen_data.py
'''
import numpy as np
import random
import cv2
import os
from data.random_plate import Draw_cfg
from data.chinese.PlateCommon import *
from data.config_gen import cfg

class GenData:
    def __init__(self, sum_path, bg_path, cfg=None):
        self.smu_path = []
        self.bg_path = []
        self.draw = Draw_cfg(cfg)
        for parent,_,filenames in os.walk(sum_path, followlinks=True):
            for filename in filenames:
                path = parent+"/"+filename
                self.smu_path.append(path)
        if bg_path is not None:
            for parent,_,filenames in os.walk(bg_path, followlinks=True):
                for filename in filenames:
                    path = parent+"/"+filename
                    self.bg_path.append(path)
    def __call__(self, embed=True,p=1) :
        # p对生成车牌做变化【仿射变换、高斯等】的概率
        com, label, color = self.draw()
        if p!=1 and random.random()>p:
            return com, label, color
        # if 1>0:
        #     return com, label, color
        com = aug(image=com)['image']
        if embed:
            com, rot_mask = rotate_image(com, random.choice([1,-1])*max(r(4),1))
            if len(self.bg_path)>0:
                comtmp = random_scene_small(com, self.bg_path, rot_mask, factor=17, factor_base=20)
                if comtmp is not None:
                    com = comtmp
            com = random_xy_shift(com,  (com.shape[1], com.shape[0]), factor=3, factor_base=3)
            com = random_crop(com, factor=2, factor_base=1)
        com = Brightness(com, 0.2)
        com = AddGauss(com, factor=3, factor_base=0)
        com = gamma_transform(com)
        com = addNoise(com)
        com = AddSmudginess(com, self.smu_path)
        return com, label, color

def main():
    gen_num = 100
    SMU_PATH = 'data/sum_imgs'
    BG_PATH = 'data/env_imgs'
    cfg.p = [0.,0.,0.,0.,1.,0.,0.] #[black_plate,blue_plate,yellow_plate,green_plate,white_plate,farm_plate,airport]
    # cfg.p = [0.15,0.15,0.15,0.15,0.15,0.15,0.1] #[black_plate,blue_plate,yellow_plate,green_plate,white_plate,farm_plate,airport]
    gen = GenData(sum_path=SMU_PATH, bg_path=BG_PATH, cfg=cfg)
    # outputPath = '/home/hanxiao/data/lp-data/train-green-1'
    # outputPath = '/home/hanxiao/data/lp-data/train-blue-1'
    # outputPath = '/home/hanxiao/data/lp-data/train-black-1'
    # outputPath = '/home/hanxiao/data/lp-data/train-yellow-1'
    # outputPath = '/home/hanxiao/data/lp-data/train-white-1'
    # outputPath = '/home/hanxiao/data/lp-data/train-farm-1'
    # outputPath = '/home/hanxiao/data/lp-data/train-airport-1'
    # outputPath = '/home/hanxiao/data/lp-data/train-all-2'
    outputPath = '/home/hanxiao/data/lp-data/train-white-jundui-6'

    if not os.path.exists(outputPath):
        os.makedirs(outputPath)
    import time
    time1 = time.time()
    for i in range(gen_num):
        img, lab, color = [],[],[]
        img,lab,color = gen(embed=False)
        print('{:12s}{:10s}'.format(color,lab))
        datamark = time.strftime("%Y%m%d", time.localtime()) 
        filename = os.path.join(outputPath, datamark + '-' + color+'-' + lab + '-' + str(int(round(time.time()*1000000))) + ".png")
        # im_resize = 100
        im_resize = 490
        im_w, im_h = img.shape[1], img.shape[0]
        rate_h = 1.0 * im_resize / im_h
        rate_w = 1.0 * im_resize / im_w
        rate = min(rate_h, rate_w)
        img_size = [int(rate*im_w), int(rate*im_h)]
        img = cv2.resize(img, (img_size[0], img_size[1]))

        # _img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # cv2.imshow('xx',_img)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        Image.fromarray(img).show('xxx')

        # cv2.imwrite(filename, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        cv2.imencode(".png",cv2.cvtColor(img, cv2.COLOR_BGR2RGBA))[1].tofile(filename)
    print('viz time: {:.3f}s'.format(time.time() - time1))


# def test_gen_plate()

if __name__ == '__main__':

    main()
