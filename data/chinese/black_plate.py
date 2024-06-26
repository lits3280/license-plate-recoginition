import os
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import random

from enum import Enum
class Black_Type(Enum):
    COMMON = 0
    SHI = 1
    LIN = 2

def load_font():
    return {
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
        "澳": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_澳.jpg"), dtype=np.uint8), -1),
        "港": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_港.jpg"), dtype=np.uint8), -1),
        # "学":  cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_学.jpg"), dtype=np.uint8), -1),
        # "警":  cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_警.jpg"), dtype=np.uint8), -1),
        "使": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_使.jpg"), dtype=np.uint8), -1),
        "领": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/140_领.jpg"), dtype=np.uint8), -1),
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

class Draw:
    def __init__(self):
        self.lplen = [7,]
        self._font = load_font()
        self._bg = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), f"res/black/black_{imgnum}.png")), (440, 140)) for imgnum in np.arange(2)
            ]
        self._bg_s = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), "res/black/black_s_0.png")), (440, 140))
            ]
        self._bg_l = [
            cv2.resize(cv2.imread(os.path.join(os.path.dirname(__file__), "res/black/black_l_0.png")), (440, 140))
            ]
    def __call__(self, plate, bg_type=Black_Type.COMMON):
        if len(plate) not in self.lplen:
            print("ERROR: Invalid length")
            return None
        bg = self._draw_bg(bg_type)
        fg = self._draw_fg(plate, bg_type)
        return cv2.cvtColor(cv2.bitwise_or(fg, bg), cv2.COLOR_BGR2RGB)

    def _draw_char(self, ch,):
        return 255-cv2.resize(self._font[ch], (45, 90))

    def _draw_fg(self, plate, bg_type):
        img = np.array(Image.new("RGB", (440, 140), (0, 0, 0)))
        if bg_type==Black_Type.COMMON:
            if (plate[0]=='使') | (plate[-1]=='领'):
                raise NotImplementedError
            offset = 15
            img[25:115, offset:offset+45] = self._draw_char(plate[0])
            offset = offset + 45 + 12
            img[25:115, offset:offset+45] = self._draw_char(plate[1])
            offset = offset + 45 + 34
            for i in range(2, len(plate)):
                img[25:115, offset:offset+45] = self._draw_char(plate[i])
                offset = offset + 45 + 12
        elif bg_type==Black_Type.SHI:
            if (plate[0]!='使'):
                raise NotImplementedError
            offset = 15 + 45 + 12
            for i in range(1, 4):
                img[25:115, offset:offset+45] = self._draw_char(plate[i])
                offset = offset + 45 + 12
            offset = offset + 22
            for i in range(4, len(plate)):
                img[25:115, offset:offset+45] = self._draw_char(plate[i])
                offset = offset + 45 + 12
        elif bg_type==Black_Type.LIN:
            if (plate[-1]!='领'):
                raise NotImplementedError
            offset = 15
            img[25:115, offset:offset+45] = self._draw_char(plate[0])
            offset = offset + 45 + 12
            img[25:115, offset:offset+45] = self._draw_char(plate[1])
            offset = offset + 45 + 34
            for i in range(2, len(plate)-1):
                img[25:115, offset:offset+45] = self._draw_char(plate[i])
                offset = offset + 45 + 12
        else:
            raise NotImplementedError
        return img

    def _draw_bg(self, bg_type):
        if bg_type==Black_Type.COMMON:
            bg = random.choice(self._bg)
        elif bg_type==Black_Type.SHI:
            bg = random.choice(self._bg_s)
        elif bg_type==Black_Type.LIN:
            bg = random.choice(self._bg_l)
        else:
            raise NotImplementedError
        return bg

if __name__ == "__main__":
    # import argparse
    # import matplotlib.pyplot as plt
    # parser = argparse.ArgumentParser(description="Generate a black plate.")
    # parser.add_argument("plate", help="license plate number (default: 京A12345)", type=str, nargs="?", default="粤A1234澳")
    # args = parser.parse_args()
    # draw = Draw()
    # plate = draw(args.plate, bg_type=0)  #bg_type=0 普通黑牌，bg_type=1 "使"开头车牌，bg_type=2 "领"结尾车牌，
    # plt.imshow(plate)
    # plt.show()
    import cv2, os
    import numpy as np

    print(os.path.join(os.path.dirname(__file__), "res/ne/220_粤.jpg"))
    img = cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_粤.jpg"), dtype=np.uint8), -1)

    cv2.imshow('xx', img)

    cv2.waitKey()
