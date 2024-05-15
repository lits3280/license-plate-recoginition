# coding=utf-8
"""
@Author:lts
@Time:2024/3/7 16:30
@description:
"""
import os
import cv2
from data.config_gen import cfg
from gen_data import GenData

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
    outputPath = '/home/hanxiao/data/lp-data/train-white-jundui-1'

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
        # cv2.imwrite(filename, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        cv2.imencode(".png",cv2.cvtColor(img, cv2.COLOR_BGR2RGBA))[1].tofile(filename)
    print('viz time: {:.3f}s'.format(time.time() - time1))