import os
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import random
from enum import Enum
class White_Type(Enum):
    COMMON = 0      # 7位
    JINGCHA = 1     # 7位
    JUNDUI = 2      # 7位
    JUNDUI_M = 3    # 7位
    WUJIN = 4       # 8位
    WUJIN_M = 5     # 8位
    YINGJI = 6      # 8位
    WUJIN_07 = 7  # 9位
    WUJIN_07_M = 8  # 9位
    WUJIN_12 = 9  # 9位
    WUJIN_12_M = 10  # 9位


def show_img(img):
    cv2.imshow('xx', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def set_font_red(img, x, y,red=[0, 0, 255]):
    x0, y0 = x
    x1, y1 = y
    imgcrop = img[y0:y1, x0:x1, :]
    imgcrop1 = imgcrop.sum(axis=2)
    imgcrop[imgcrop1 < 200] = red
    img[y0:y1, x0:x1] = imgcrop

def load_font():
    return {

        "警": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_警.jpg"), dtype=np.uint8), -1),
        "消": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_消.jpg"), dtype=np.uint8), -1),
        "边": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_边.jpg"), dtype=np.uint8), -1),
        "通": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_通.jpg"), dtype=np.uint8), -1),
        "森": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_森.jpg"), dtype=np.uint8), -1),
        "金": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_金.jpg"), dtype=np.uint8), -1),
        "电": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_电.jpg"), dtype=np.uint8), -1),

        "甲": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_甲.jpg"), dtype=np.uint8), -1),
        "乙": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_乙.jpg"), dtype=np.uint8), -1),
        "丙": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_丙.jpg"), dtype=np.uint8), -1),
        "丁": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_丁.jpg"), dtype=np.uint8), -1),
        "戊": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_戊.jpg"), dtype=np.uint8), -1),
        "己": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_己.jpg"), dtype=np.uint8), -1),
        "庚": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_庚.jpg"), dtype=np.uint8), -1),
        "辛": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_辛.jpg"), dtype=np.uint8), -1),
        "壬": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_壬.jpg"), dtype=np.uint8), -1),
        "癸": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_癸.jpg"), dtype=np.uint8), -1),
        "子": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_子.jpg"), dtype=np.uint8), -1),
        "丑": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_丑.jpg"), dtype=np.uint8), -1),
        "寅": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_寅.jpg"), dtype=np.uint8), -1),
        "卯": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_卯.jpg"), dtype=np.uint8), -1),
        "辰": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_辰.jpg"), dtype=np.uint8), -1),
        "巳": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_巳.jpg"), dtype=np.uint8), -1),
        "午": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_午.jpg"), dtype=np.uint8), -1),
        "未": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_未.jpg"), dtype=np.uint8), -1),
        "申": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_申.jpg"), dtype=np.uint8), -1),
        "酉": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_酉.jpg"), dtype=np.uint8), -1),
        "戌": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_戌.jpg"), dtype=np.uint8), -1),
        "亥": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_亥.jpg"), dtype=np.uint8), -1),

        "军": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_军.jpg"), dtype=np.uint8), -1),
        "北": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_北.jpg"), dtype=np.uint8), -1),
        "南": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_南.jpg"), dtype=np.uint8), -1),
        "广": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_广.jpg"), dtype=np.uint8), -1),
        "济": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_济.jpg"), dtype=np.uint8), -1),
        "沈": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_沈.jpg"), dtype=np.uint8), -1),
        "兰": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_兰.jpg"), dtype=np.uint8), -1),
        "成": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_成.jpg"), dtype=np.uint8), -1),
        "海": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_海.jpg"), dtype=np.uint8), -1),
        "空": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_140_空.jpg"), dtype=np.uint8), -1),

        "京": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_京.jpg"), dtype=np.uint8), -1),
        "津": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_津.jpg"), dtype=np.uint8), -1),
        "冀": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_冀.jpg"), dtype=np.uint8), -1),
        "晋": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_晋.jpg"), dtype=np.uint8), -1),
        "蒙": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_蒙.jpg"), dtype=np.uint8), -1),
        "辽": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_辽.jpg"), dtype=np.uint8), -1),
        "吉": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_吉.jpg"), dtype=np.uint8), -1),
        "黑": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_黑.jpg"), dtype=np.uint8), -1),
        "沪": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_沪.jpg"), dtype=np.uint8), -1),
        "苏": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_苏.jpg"), dtype=np.uint8), -1),
        "浙": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_浙.jpg"), dtype=np.uint8), -1),
        "皖": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_皖.jpg"), dtype=np.uint8), -1),
        "闽": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_闽.jpg"), dtype=np.uint8), -1),
        "赣": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_赣.jpg"), dtype=np.uint8), -1),
        "鲁": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_鲁.jpg"), dtype=np.uint8), -1),
        "豫": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_豫.jpg"), dtype=np.uint8), -1),
        "鄂": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_鄂.jpg"), dtype=np.uint8), -1),
        "湘": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_湘.jpg"), dtype=np.uint8), -1),
        "粤": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_粤.jpg"), dtype=np.uint8), -1),
        "桂": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_桂.jpg"), dtype=np.uint8), -1),
        "琼": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_琼.jpg"), dtype=np.uint8), -1),
        "渝": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_渝.jpg"), dtype=np.uint8), -1),
        "川": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_川.jpg"), dtype=np.uint8), -1),
        "贵": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_贵.jpg"), dtype=np.uint8), -1),
        "云": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_云.jpg"), dtype=np.uint8), -1),
        "藏": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_藏.jpg"), dtype=np.uint8), -1),
        "陕": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_陕.jpg"), dtype=np.uint8), -1),
        "甘": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_甘.jpg"), dtype=np.uint8), -1),
        "青": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_青.jpg"), dtype=np.uint8), -1),
        "宁": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_宁.jpg"), dtype=np.uint8), -1),
        "新": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_新.jpg"), dtype=np.uint8), -1),
        # "澳":  cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_澳.jpg"), dtype=np.uint8), -1),
        # "港":  cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_港.jpg"), dtype=np.uint8), -1),
        # "学":  cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_学.jpg"), dtype=np.uint8), -1),
        "警": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_警.jpg"), dtype=np.uint8), -1),
        # "使":  cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_使.jpg"), dtype=np.uint8), -1),
        # "领":  cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_领.jpg"), dtype=np.uint8), -1),
        "A": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_A.jpg"), dtype=np.uint8), -1),
        "B": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_B.jpg"), dtype=np.uint8), -1),
        "C": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_C.jpg"), dtype=np.uint8), -1),
        "D": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_D.jpg"), dtype=np.uint8), -1),
        "E": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_E.jpg"), dtype=np.uint8), -1),
        "F": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_F.jpg"), dtype=np.uint8), -1),
        "G": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_G.jpg"), dtype=np.uint8), -1),
        "H": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_H.jpg"), dtype=np.uint8), -1),
        "J": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_J.jpg"), dtype=np.uint8), -1),
        "K": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_K.jpg"), dtype=np.uint8), -1),
        "L": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_L.jpg"), dtype=np.uint8), -1),
        "M": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_M.jpg"), dtype=np.uint8), -1),
        "N": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_N.jpg"), dtype=np.uint8), -1),
        "P": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_P.jpg"), dtype=np.uint8), -1),
        "Q": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_Q.jpg"), dtype=np.uint8), -1),
        "R": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_R.jpg"), dtype=np.uint8), -1),
        "S": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_S.jpg"), dtype=np.uint8), -1),
        "T": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_T.jpg"), dtype=np.uint8), -1),
        "U": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_U.jpg"), dtype=np.uint8), -1),
        "V": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_V.jpg"), dtype=np.uint8), -1),
        "W": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_W.jpg"), dtype=np.uint8), -1),
        "X": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_X.jpg"), dtype=np.uint8), -1),
        "Y": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_Y.jpg"), dtype=np.uint8), -1),
        "Z": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_Z.jpg"), dtype=np.uint8), -1),
        "0": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_0.jpg"), dtype=np.uint8), -1),
        "1": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_1.jpg"), dtype=np.uint8), -1),
        "2": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_2.jpg"), dtype=np.uint8), -1),
        "3": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_3.jpg"), dtype=np.uint8), -1),
        "4": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_4.jpg"), dtype=np.uint8), -1),
        "5": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_5.jpg"), dtype=np.uint8), -1),
        "6": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_6.jpg"), dtype=np.uint8), -1),
        "7": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_7.jpg"), dtype=np.uint8), -1),
        "8": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_8.jpg"), dtype=np.uint8), -1),
        "9": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_9.jpg"), dtype=np.uint8), -1)
    }
def load_font_up():
    return {
        "警": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_警.jpg"), dtype=np.uint8), -1),
        "消": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_消.jpg"), dtype=np.uint8), -1),
        "边": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_边.jpg"), dtype=np.uint8), -1),
        "通": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_通.jpg"), dtype=np.uint8), -1),
        "森": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_森.jpg"), dtype=np.uint8), -1),
        "金": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_金.jpg"), dtype=np.uint8), -1),
        "电": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_电.jpg"), dtype=np.uint8), -1),

        "甲": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_甲.jpg"), dtype=np.uint8), -1),
        "乙": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_乙.jpg"), dtype=np.uint8), -1),
        "丙": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_丙.jpg"), dtype=np.uint8), -1),
        "丁": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_丁.jpg"), dtype=np.uint8), -1),
        "戊": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_戊.jpg"), dtype=np.uint8), -1),
        "己": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_己.jpg"), dtype=np.uint8), -1),
        "庚": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_庚.jpg"), dtype=np.uint8), -1),
        "辛": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_辛.jpg"), dtype=np.uint8), -1),
        "壬": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_壬.jpg"), dtype=np.uint8), -1),
        "癸": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_癸.jpg"), dtype=np.uint8), -1),
        "子": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_子.jpg"), dtype=np.uint8), -1),
        "丑": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_丑.jpg"), dtype=np.uint8), -1),
        "寅": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_寅.jpg"), dtype=np.uint8), -1),
        "卯": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_卯.jpg"), dtype=np.uint8), -1),
        "辰": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_辰.jpg"), dtype=np.uint8), -1),
        "巳": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_巳.jpg"), dtype=np.uint8), -1),
        "午": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_午.jpg"), dtype=np.uint8), -1),
        "未": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_未.jpg"), dtype=np.uint8), -1),
        "申": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_申.jpg"), dtype=np.uint8), -1),
        "酉": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_酉.jpg"), dtype=np.uint8), -1),
        "戌": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_戌.jpg"), dtype=np.uint8), -1),
        "亥": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_亥.jpg"), dtype=np.uint8), -1),

        "军": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_军.jpg"), dtype=np.uint8), -1),
        "北": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_北.jpg"), dtype=np.uint8), -1),
        "南": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_南.jpg"), dtype=np.uint8), -1),
        "广": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_广.jpg"), dtype=np.uint8), -1),
        "济": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_济.jpg"), dtype=np.uint8), -1),
        "沈": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_沈.jpg"), dtype=np.uint8), -1),
        "兰": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_兰.jpg"), dtype=np.uint8), -1),
        "成": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_成.jpg"), dtype=np.uint8), -1),
        "海": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_海.jpg"), dtype=np.uint8), -1),
        "空": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_220_空.jpg"), dtype=np.uint8), -1),


    "京": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_京.jpg"), dtype=np.uint8), -1),
        "津": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_津.jpg"), dtype=np.uint8), -1),
        "冀": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_冀.jpg"), dtype=np.uint8), -1),
        "晋": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_晋.jpg"), dtype=np.uint8), -1),
        "蒙": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_蒙.jpg"), dtype=np.uint8), -1),
        "辽": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_辽.jpg"), dtype=np.uint8), -1),
        "吉": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_吉.jpg"), dtype=np.uint8), -1),
        "黑": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_黑.jpg"), dtype=np.uint8), -1),
        "沪": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_沪.jpg"), dtype=np.uint8), -1),
        "苏": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_苏.jpg"), dtype=np.uint8), -1),
        "浙": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_浙.jpg"), dtype=np.uint8), -1),
        "皖": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_皖.jpg"), dtype=np.uint8), -1),
        "闽": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_闽.jpg"), dtype=np.uint8), -1),
        "赣": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_赣.jpg"), dtype=np.uint8), -1),
        "鲁": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_鲁.jpg"), dtype=np.uint8), -1),
        "豫": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_豫.jpg"), dtype=np.uint8), -1),
        "鄂": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_鄂.jpg"), dtype=np.uint8), -1),
        "湘": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_湘.jpg"), dtype=np.uint8), -1),
        "粤": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_粤.jpg"), dtype=np.uint8), -1),
        "桂": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_桂.jpg"), dtype=np.uint8), -1),
        "琼": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_琼.jpg"), dtype=np.uint8), -1),
        "渝": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_渝.jpg"), dtype=np.uint8), -1),
        "川": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_川.jpg"), dtype=np.uint8), -1),
        "贵": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_贵.jpg"), dtype=np.uint8), -1),
        "云": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_云.jpg"), dtype=np.uint8), -1),
        "藏": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_藏.jpg"), dtype=np.uint8), -1),
        "陕": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_陕.jpg"), dtype=np.uint8), -1),
        "甘": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_甘.jpg"), dtype=np.uint8), -1),
        "青": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_青.jpg"), dtype=np.uint8), -1),
        "宁": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_宁.jpg"), dtype=np.uint8), -1),
        "新": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_新.jpg"), dtype=np.uint8), -1),
        "A": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_A.jpg"), dtype=np.uint8), -1),
        "B": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_B.jpg"), dtype=np.uint8), -1),
        "C": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_C.jpg"), dtype=np.uint8), -1),
        "D": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_D.jpg"), dtype=np.uint8), -1),
        "E": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_E.jpg"), dtype=np.uint8), -1),
        "F": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_F.jpg"), dtype=np.uint8), -1),
        "G": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_G.jpg"), dtype=np.uint8), -1),
        "H": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_H.jpg"), dtype=np.uint8), -1),
        "J": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_J.jpg"), dtype=np.uint8), -1),
        "K": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_K.jpg"), dtype=np.uint8), -1),
        "L": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_L.jpg"), dtype=np.uint8), -1),
        "M": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_M.jpg"), dtype=np.uint8), -1),
        "N": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_N.jpg"), dtype=np.uint8), -1),
        "P": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_P.jpg"), dtype=np.uint8), -1),
        "Q": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_Q.jpg"), dtype=np.uint8), -1),
        "R": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_R.jpg"), dtype=np.uint8), -1),
        "S": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_S.jpg"), dtype=np.uint8), -1),
        "T": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_T.jpg"), dtype=np.uint8), -1),
        "U": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_U.jpg"), dtype=np.uint8), -1),
        "V": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_V.jpg"), dtype=np.uint8), -1),
        "W": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_W.jpg"), dtype=np.uint8), -1),
        "X": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_X.jpg"), dtype=np.uint8), -1),
        "Y": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_Y.jpg"), dtype=np.uint8), -1),
        "Z": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_up_Z.jpg"), dtype=np.uint8), -1),
    }

def load_font_down():
    return {
        "挂": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_挂.jpg"), dtype=np.uint8), -1),
        "A": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_A.jpg"), dtype=np.uint8), -1),
        "B": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_B.jpg"), dtype=np.uint8), -1),
        "C": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_C.jpg"), dtype=np.uint8), -1),
        "D": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_D.jpg"), dtype=np.uint8), -1),
        "E": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_E.jpg"), dtype=np.uint8), -1),
        "F": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_F.jpg"), dtype=np.uint8), -1),
        "G": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_G.jpg"), dtype=np.uint8), -1),
        "H": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_H.jpg"), dtype=np.uint8), -1),
        "J": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_J.jpg"), dtype=np.uint8), -1),
        "K": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_K.jpg"), dtype=np.uint8), -1),
        "L": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_L.jpg"), dtype=np.uint8), -1),
        "M": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_M.jpg"), dtype=np.uint8), -1),
        "N": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_N.jpg"), dtype=np.uint8), -1),
        "P": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_P.jpg"), dtype=np.uint8), -1),
        "Q": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_Q.jpg"), dtype=np.uint8), -1),
        "R": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_R.jpg"), dtype=np.uint8), -1),
        "S": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_S.jpg"), dtype=np.uint8), -1),
        "T": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_T.jpg"), dtype=np.uint8), -1),
        "U": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_U.jpg"), dtype=np.uint8), -1),
        "V": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_V.jpg"), dtype=np.uint8), -1),
        "W": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_W.jpg"), dtype=np.uint8), -1),
        "X": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_X.jpg"), dtype=np.uint8), -1),
        "Y": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_Y.jpg"), dtype=np.uint8), -1),
        "Z": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_down_Z.jpg"), dtype=np.uint8), -1),
        "0": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_0.jpg"), dtype=np.uint8), -1),
        "1": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_1.jpg"), dtype=np.uint8), -1),
        "2": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_2.jpg"), dtype=np.uint8), -1),
        "3": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_3.jpg"), dtype=np.uint8), -1),
        "4": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_4.jpg"), dtype=np.uint8), -1),
        "5": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_5.jpg"), dtype=np.uint8), -1),
        "6": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_6.jpg"), dtype=np.uint8), -1),
        "7": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_7.jpg"), dtype=np.uint8), -1),
        "8": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_8.jpg"), dtype=np.uint8), -1),
        "9": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_9.jpg"), dtype=np.uint8), -1)
    }

def load_font_num_wj():

    return {
        "0": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_wj_140_0.jpg"), dtype=np.uint8), -1),
        "1": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_wj_140_1.jpg"), dtype=np.uint8), -1),
        "2": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_wj_140_2.jpg"), dtype=np.uint8), -1),
        "3": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_wj_140_3.jpg"), dtype=np.uint8), -1),
        "4": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_wj_140_4.jpg"), dtype=np.uint8), -1),
        "5": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_wj_140_5.jpg"), dtype=np.uint8), -1),
        "6": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_wj_140_6.jpg"), dtype=np.uint8), -1),
        "7": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_wj_140_7.jpg"), dtype=np.uint8), -1),
        "8": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_wj_140_8.jpg"), dtype=np.uint8), -1),
        "9": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/my_wj_140_9.jpg"), dtype=np.uint8), -1),
    }

class Draw:
    def __init__(self):
        self.lplen = [7,8,9]
        self._font = load_font()
        self._font_up = load_font_up()
        self._font_down = load_font_down()

        self._bg_common = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/white/white_{imgnum}.png")), (440, 140)) for imgnum in np.arange(2)
            ]
        self._bg_jingcha = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/white/white_jc_{imgnum}.png")), (440, 140)) for imgnum in np.arange(2)
            ]
        self._bg_jundui = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/white/white_jd_{imgnum}.png")), (490, 140)) for imgnum in [0,2]
            ]
        self._bg_jundui_m = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/white/white_jd_m_{imgnum}.png")), (495, 240)) for imgnum in np.arange(2)
            ]
        self._bgs_wujing = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/white/white_wj_{imgnum}.png")), (480, 140)) for imgnum in np.arange(1)
            ]
        self._bgs_wujing_m = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/white/white_wj_m_{imgnum}.png")), (495, 240)) for imgnum in np.arange(1)
            ]
        self._bgs_yingji = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/white/white_yj_{imgnum}.png")), (480, 140)) for imgnum in np.arange(1)
            ]

        #07式武警
        self._bgs_wujing_07 = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/white/wj_07_bg_{imgnum}.png")), (495, 140)) for imgnum in np.arange(2)
            ]
        self._bgs_wujing_07_m = [
        cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/white/wj_07_bg_m_{imgnum}.png")), (495, 240)) for imgnum in np.arange(2)
        ]
        # 12式武警
        self._bgs_wujing_12 = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/white/wj_12_bg_{imgnum}.png")), (535, 140)) for imgnum in np.arange(2)
        ]
        self._bgs_wujing_12_m = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/white/wj_12_bg_m_{imgnum}.png")), (485, 240)) for imgnum in np.arange(2)
        ]

        self._font_num_wj=load_font_num_wj()

        self._wj_flags_chars = {"警", "消", "边", "通", "森", "金", "电", "H", "S", "D", "T", "B", "X", "J"}

    def __call__(self, plate, bg_type=White_Type.COMMON, front_=False):
        if len(plate) not in self.lplen:
            print(f"ERROR: plate length:{plate},bg_type:{bg_type}")
            return None
        if (len(plate) == 7):
            if bg_type not in [White_Type.COMMON, White_Type.JINGCHA, White_Type.JUNDUI, White_Type.JUNDUI_M ]:
                print(f"ERROR: plate length:{plate},bg_type:{bg_type}")
                return None
        if (len(plate) == 8):
            if bg_type not in [White_Type.WUJIN, White_Type.WUJIN_M, White_Type.JUNDUI, White_Type.YINGJI,White_Type.WUJIN_12,White_Type.WUJIN_12_M ]:
                print(f"ERROR: plate length:{plate},bg_type:{bg_type}")
                return None        
        if (len(plate) == 9):
            if bg_type not in [White_Type.WUJIN_07,White_Type.WUJIN_07_M]:
                print(f"ERROR: plate length:{plate},bg_type:{bg_type}")
                return None
        bg = self._draw_bg(bg_type)
        fg = self._draw_fg(plate, bg_type,p_front=front_)
        new_img=cv2.cvtColor(cv2.bitwise_and(fg, bg), cv2.COLOR_BGR2RGB)
        return new_img

    def _draw_char(self, ch,):
            return cv2.resize(self._font[ch], (45, 90))
    def _draw_char_jd(self, ch,):
            return cv2.resize(self._font[ch], (50, 84))
    def _draw_char_yj(self, ch,):
            return cv2.resize(self._font[ch], (43, 90))

    def _draw_char_wj_my(self, ch, w_h=(38, 50)):
        if ch.isdigit():
            # 武警数字字体特殊
            img = self._font_num_wj[ch]
        else:
            img = self._font[ch]
        return cv2.resize(img, (w_h[0], w_h[1]))

    def _draw_char_multi(self, ch, upper=True):
        if upper:
            return cv2.resize(self._font[ch], (100,70))
        else:
            return cv2.resize(self._font[ch], (73, 100))
    def _draw_char_wj(self, ch,):
            return cv2.resize(self._font[ch], (56, 70))
    def _draw_char_wj_multi(self, ch, upper=True):
        if upper:
            return cv2.resize(self._font[ch], (73, 70))
        else:
            return cv2.resize(self._font[ch], (73, 100))
    
    def _draw_fg(self, plate, bg_type, p_front):
        if bg_type==White_Type.COMMON:  # 单行 未定义白色
            img = np.array(Image.new("RGB", (440, 140), (255, 255, 255)))
            offset = 15
            img[25:115, offset:offset+45] = self._draw_char(plate[0])
            offset = offset + 45 + 34
            for i in range(1, len(plate)-1):
                img[25:115, offset:offset+45] = self._draw_char(plate[i])
                offset = offset + 45 + 12
        elif bg_type==White_Type.JINGCHA:  # 单行警牌
            img = np.array(Image.new("RGB", (440, 140), (255, 255, 255)))
            if (plate[-1]!='警'):
                raise NotImplementedError
            offset = 15
            img[25:115, offset:offset+45] = self._draw_char(plate[0])
            offset = offset + 45 + 34
            for i in range(1, len(plate)-1):
                img[25:115, offset:offset+45] = self._draw_char(plate[i])
                offset = offset + 45 + 12
        elif bg_type==White_Type.JUNDUI:  # 单行军牌
            img = np.array(Image.new("RGB", (490, 140), (255, 255, 255)))
            offset = 17
            img[28:112, offset:offset+50] = self._draw_char_jd(plate[0])
            offset = offset + 50 + 12
            img[28:112, offset:offset+50] = self._draw_char_jd(plate[1])
            offset = offset + 50 + 45
            for i in range(2, len(plate)):
                img[28:112, offset:offset+50] = self._draw_char_jd(plate[i])
                offset = offset + 50 + 12

            if p_front:     #前车牌点号红色
                imgcrop=img[28:112,15:169,:]
                imgcrop1 = imgcrop.sum(axis=2)
                imgcrop[imgcrop1<200]=[0,0,255]
                img[28:112,15:169]=imgcrop
            else:
                imgcrop=img[28:112,15:67,:]
                imgcrop1 = imgcrop.sum(axis=2)
                imgcrop[imgcrop1<200]=[0,0,255]
                img[28:112,15:67]=imgcrop
        elif bg_type==White_Type.WUJIN:  # 单行武警牌
            img = np.array(Image.new("RGB", (480, 140), (255, 255, 255)))
            offset = 15
            img[25:115, offset:offset+43] = self._draw_char_wj_my(plate[0],w_h=(43, 90))
            offset = offset + 43 + 8
            img[25:115, offset:offset+43] = self._draw_char_wj_my(plate[1],w_h=(43, 90))
            offset = offset + 43 + 35
            for i in range(2, len(plate)):
                img[25:115, offset:offset+43] = self._draw_char_wj_my(plate[i],w_h=(43, 90))
                offset = offset + 43 + 12
            if p_front:     #前车牌点号红色
                imgcrop=img[25:115,15:110,:]
                imgcrop1 = imgcrop.sum(axis=2)
                imgcrop[imgcrop1<200]=[0,0,255]
                img[25:115,15:110]=imgcrop
            else:
                imgcrop=img[25:115,15:197,:]
                imgcrop1 = imgcrop.sum(axis=2)
                imgcrop[imgcrop1<200]=[0,0,255]
                img[25:115,15:197]=imgcrop
        elif bg_type==White_Type.WUJIN_07:  # 单行武警牌:07式
            img = np.array(Image.new("RGB", (495, 140), (255, 255, 255)))
            red_boxes=[]

            offset = 108
            img[62:112, offset:offset + 38] = self._draw_char_wj_my(plate[2],w_h=(38, 50))
            offset = offset + 38 + 6
            img[62:112, offset:offset + 38] = self._draw_char_wj_my(plate[3],w_h=(38, 50))
            red_boxes.append([[108,62],[190,112]])
            offset = 192
            for i in range(4, len(plate)):
                ch=plate[i]
                img[30:112, offset:offset + 52] = self._draw_char_wj_my(ch,w_h=(52, 82))
                if (i == 4 or i == len(plate) - 1) and ch in self._wj_flags_chars:
                    red_boxes.append([[offset, 30], [offset + 52,112]])

                offset = offset + 52 + 7

            if p_front:     #前车牌点号红色
                for x,y in red_boxes:
                    # 因为底图WJ不是纯红,RGB=(220,50,76)，这需要做下处理
                    # set_font_red(img,x,y,red=[76,50,220])
                    set_font_red(img,x,y,red=[78,49,222])
            # else:
            #     imgcrop=img[25:115,15:197,:]
            #     imgcrop1 = imgcrop.sum(axis=2)
            #     imgcrop[imgcrop1<200]=[0,0,255]
            #     img[25:115,15:197]=imgcrop
        elif bg_type == White_Type.WUJIN_07_M:  # 双行武警牌:07式
            img = np.array(Image.new("RGB", (495, 240), (255, 255, 255)))
            red_boxes = []

            offset = 265
            img[27:99, offset:offset + 57] = self._draw_char_wj_my(plate[2], w_h = (57, 72))
            offset = offset + 57 + 29
            img[27:99, offset:offset + 57] = self._draw_char_wj_my(plate[3], w_h = (57, 72))

            red_boxes.append([[265, 27], [offset + 57, 99]])

            offset = 25
            for i in range(4, len(plate)):
                ch = plate[i]
                img[110:214, offset:offset + 78] = self._draw_char_wj_my(ch,  w_h = (78, 104))
                if (i == 4 or i == len(plate) - 1) and ch in self._wj_flags_chars:
                    red_boxes.append([[offset, 110], [offset + 78, 214]])

                offset = offset + 78 + 14

            if p_front:  # 前车牌点号红色
                for x, y in red_boxes:
                    # 因为底图WJ不是纯红,RGB=(220,50,76)，这需要做下处理
                    # set_font_red(img,x,y,red=[76,50,220])
                    set_font_red(img, x, y, red=[78, 49, 222])
        elif bg_type==White_Type.WUJIN_12:  # 单行武警牌:12式
            img = np.array(Image.new("RGB", (535, 140), (255, 255, 255)))
            red_boxes=[]

            offset = 120
            img[32:114, offset:offset + 52] = self._draw_char_wj_my(plate[2],w_h=(52, 82))
            red_boxes.append([[120,32],[offset + 52,114]])

            offset = 226
            for i in range(3, len(plate)):
                ch=plate[i]
                img[32:114, offset:offset + 50] = self._draw_char_wj_my(ch,w_h=(50, 82))
                if (i == 3 or i == len(plate) - 1) and ch in self._wj_flags_chars:
                    red_boxes.append([[offset, 32], [offset + 50,114]])

                offset = offset + 50 + 11

            if p_front:     #前车牌点号红色
                for x,y in red_boxes:
                    # 因为底图WJ不是纯红,RGB=(220,50,76)，这需要做下处理
                    set_font_red(img,x,y,red=[76,50,220])

        elif bg_type==White_Type.WUJIN_12_M:  # 双行武警牌:12式
            img = np.array(Image.new("RGB", (485, 240), (255, 255, 255)))
            red_boxes=[]

            offset = 294
            img[32:98, offset:offset + 80] = self._draw_char_wj_my(plate[2], w_h=(80, 66))
            red_boxes.append([[294,32],[offset + 80,98]])

            offset = 25
            for i in range(3, len(plate)):
                ch=plate[i]
                img[114:210, offset:offset + 76] = self._draw_char_wj_my(ch , w_h=(76, 96))
                if (i == 3 or i == len(plate) - 1) and ch in self._wj_flags_chars:
                    red_boxes.append([[offset, 114], [offset + 76,210]])

                offset = offset + 76 + 14

            if p_front:     #前车牌点号红色
                for x,y in red_boxes:
                    # 因为底图WJ不是纯红,RGB=(220,50,76)，这需要做下处理
                    set_font_red(img,x,y,red=[76,50,220])

        elif bg_type==White_Type.YINGJI:  # 应急车牌
            img = np.array(Image.new("RGB", (480, 140), (255, 255, 255)))
            if ((plate[-1]!='急')|(plate[-2]!='应')):
                raise NotImplementedError
            offset = 15
            img[25:115, offset:offset+45] = self._draw_char(plate[0])
            offset = offset + 45 + 31
            for i in range(1, len(plate)-2):
                img[25:115, offset:offset+43] = self._draw_char_yj(plate[i])
                offset = offset + 43 + 12
            if p_front:     #前车牌点号红色
                imgcrop=img[25:115,86:139,:]
                imgcrop1 = imgcrop.sum(axis=2)
                imgcrop[imgcrop1<200]=[0,0,255]
                img[25:115,86:139]=imgcrop
        elif bg_type==White_Type.JUNDUI_M:  # 双行军牌
            img = np.array(Image.new("RGB", (495, 240), (255, 255, 255)))
            offset = 118
            img[30:100, offset:offset+100] = self._draw_char_multi(plate[0])
            offset = offset + 100 + 60
            img[30:100, offset:offset+100] = self._draw_char_multi(plate[1])
            offset = 25
            for i in range(2, len(plate)):
                img[120:220, offset:offset+73] = self._draw_char_multi(plate[i],upper=False)
                offset = offset + 73 + 20
            if p_front:     #前车牌点号红色
                imgcrop=img[30:100,110:220,:]
                imgcrop1 = imgcrop.sum(axis=2)
                imgcrop[imgcrop1<200]=[0,0,255]
                img[30:100,110:220]=imgcrop
            else:
                imgcrop=img[30:100,110:380,:]
                imgcrop1 = imgcrop.sum(axis=2)
                imgcrop[imgcrop1<200]=[0,0,255]
                img[30:100,110:380]=imgcrop
        elif bg_type==White_Type.WUJIN_M:  # 双行武警牌
            img = np.array(Image.new("RGB", (495, 240), (255, 255, 255)))
            offset = 118
            img[30:100, offset:offset+73] = self._draw_char_wj_multi(plate[0])
            offset = offset + 73+4
            img[30:100, offset:offset+56] = self._draw_char_wj(plate[1])
            offset = offset + 56+20+15+20
            img[30:100, offset:offset+73] = self._draw_char_wj_multi(plate[2])
            offset = 25
            for i in range(3, len(plate)):
                img[120:220, offset:offset+73] = self._draw_char_wj_multi(plate[i],upper=False)
                offset = offset + 73 + 20

            if p_front:     #前车牌点号红色
                imgcrop=img[30:100,110:295,:]
                imgcrop1 = imgcrop.sum(axis=2)
                imgcrop[imgcrop1<200]=[0,0,255]
                img[30:100,110:295]=imgcrop
            else:
                imgcrop=img[30:100,110:440,:]
                imgcrop1 = imgcrop.sum(axis=2)
                imgcrop[imgcrop1<200]=[0,0,255]
                img[30:100,110:440]=imgcrop
        else:
            raise NotImplementedError
        return img

    def _draw_bg(self, bg_type):
        if bg_type == White_Type.COMMON:
            bg = random.choice(self._bg_common)
        elif bg_type==White_Type.JINGCHA:
            bg = random.choice(self._bg_jingcha)  
        elif bg_type==White_Type.JUNDUI:
            bg = random.choice(self._bg_jundui)   
        elif bg_type==White_Type.JUNDUI_M:
            bg = random.choice(self._bg_jundui_m)   
        elif bg_type==White_Type.WUJIN:
            bg = random.choice(self._bgs_wujing)
        elif bg_type==White_Type.WUJIN_M:
            bg = random.choice(self._bgs_wujing_m)
        elif bg_type==White_Type.YINGJI:
            bg = random.choice(self._bgs_yingji)
        elif bg_type==White_Type.WUJIN_07:
            bg = random.choice(self._bgs_wujing_07)
        elif bg_type==White_Type.WUJIN_07_M:
            bg = random.choice(self._bgs_wujing_07_m)
        elif bg_type==White_Type.WUJIN_12:
            bg = random.choice(self._bgs_wujing_12)
        elif bg_type==White_Type.WUJIN_12_M:
            bg = random.choice(self._bgs_wujing_12_m)
        else:
            raise NotImplementedError
        return bg


if __name__ == "__main__":
    import argparse
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser(description="Generate a black plate.")
    parser.add_argument("plate", help="license plate number (default: 京A12345)", type=str, nargs="?", default="WJX30522")
    args = parser.parse_args()

    draw = Draw()
    plate = draw(args.plate, bg_type=5)  #bg_type=0，单行'警'牌，军牌、双行待添加
    plt.imshow(plate)
    plt.show()
