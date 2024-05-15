# coding=utf-8
"""
@Author:lts
@Time:2024/3/8 10:11
@description:
"""

from PIL import Image, ImageDraw, ImageFont
import cv2,os
import numpy as np


def _draw_char(ch,scale=10):
    is_en_char = ch.isupper() or ch.isdigit()
    img = Image.new("RGB", (55*scale+500 if is_en_char else 95*scale, scale*140+500), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text(
        (0, -11*scale if is_en_char else 3*scale), ch,
        # fill=(255, 255, 255),
        fill=(0, 0, 0),
        # font=ImageFont.truetype("eng_92.ttf", 126*scale) if is_en_char else ImageFont.truetype("zh_cn_92.ttf", 95*scale)
        # font=ImageFont.truetype("platechar.ttf", 100*scale)
        # font=ImageFont.truetype("zh_cn_92.ttf", 20*scale)
        font=ImageFont.truetype("zh_cn_92.ttf",180*scale)
        # font=ImageFont.truetype("simsun.ttc",100*scale)
    )
    # if img.width > 45:
    #     img = img.resize((45, 140))
    # return np.array(img)
    return img


def crop_text(img):
    # return img
    w, h = img.size
    not_blank_xy = []
    for x in range(0, w):
        for y in range(0, h):
            pixel = img.getpixel((x, y))
            if pixel != (255, 255, 255):
                not_blank_xy.append([x, y])

    x_axis = [x[0] for x in not_blank_xy]
    y_axis = [x[1] for x in not_blank_xy]
    min_x, min_y, max_x, max_y = min(x_axis), min(y_axis), max(x_axis), max(y_axis)
    img_crop = img.crop((min_x, min_y, max_x, max_y))
    return img_crop


def test():
    # img = Image.new('RGB',(200,200),color=(255,255,255))
    img = Image.new('RGB', (400, 400), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    textSize = 350
    # fontText = ImageFont.truetype("NotoSansCJK-Regular.ttc", size=textSize, encoding="utf-8")
    fontText = ImageFont.truetype("zh_cn_92.ttf", size=textSize, encoding="utf-8")
    pos = (10, 10)
    text = '辽'
    textColor = (0, 0, 0)
    anchors = ['la', 'lt', 'lm', 'ls', 'lb', 'ld']
    draw.text(pos, text, textColor, font=fontText, stroke_width=1, anchor='la')
    img.show()
    # img.resize((130, 97))
    # img.show()

def create_chars_wj():

    # jundui_chars="军,北,南,广,济,沈,兰,成,海,空".split(',')
    # 武警车牌数字样式和其他车牌不一致，且需要对"1"特出处理
    jundui_chars="0,2,3,4,5,6,7,8,9".split(',')
    # jundui_chars="军".split(',')

    save_dir='chars_wj'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for c in jundui_chars:

        img = _draw_char(c)
        # img.show()
        c_img=crop_text(img)
        # c_img.show(c)
        # c_img.save(f'{save_dir}/{c}.png')
        #窄图140_： (76, 152)
        c_img.resize((76, 152)).save(f'{save_dir}/my_wj_140_{c}.jpg')
        # 宽图220_：(132, 98)
        # c_img.resize((132, 98)).save(f'{save_dir}/my_wj220_{c}.jpg')

create_chars_wj()

# print("','".join('京,军,北,南,广,济,沈,兰,成,海,空'.split(',')))
#
# jundui_chars="军,北,南,广,济,沈,兰,成,海,空".split(',')
#
# s='"新": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_新.jpg"), dtype=np.uint8), -1),'
# for c in jundui_chars:
#     # s_140=s.replace('140_新',f'my_140_{c}').replace('新',c)
#     s_220=s.replace('140_新',f'my_220_{c}').replace('新',c)
#     print(s_220)
