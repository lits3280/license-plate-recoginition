# coding=utf-8
"""
@Author:lts
@Time:2024/3/6 17:49
@description:
"""

s='''
"皖": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_皖.jpg"), dtype=np.uint8), -1),
        "闽": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_闽.jpg"), dtype=np.uint8), -1),
        "赣": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_赣.jpg"), dtype=np.uint8), -1),
        "鲁": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_鲁.jpg"), dtype=np.uint8), -1),
        "豫": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_豫.jpg"), dtype=np.uint8), -1),
        "鄂": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_鄂.jpg"), dtype=np.uint8), -1),
        "湘": cv2.imdecode(np.fromfile(os.path.join(os.path.dirname(__file__), "res/ne/220_湘.jpg"), dtype=np.uint8), -1),
'''
import re

# s='"9": cv2.imread(os.path.join(os.path.dirname(__file__), "res/ne/140_9.jpg"))"'
regex='cv2\.imread\((os\.path\.join\(os\.path\.dirname\(__file__\), ".*?"\))\)'
# m=re.findall(regex,s)
iter=re.finditer(regex,s)
for item in iter:
    item_text=item.group(0)
    img_path=item.group(1)
    # cv2.imdecode(np.fromfile(chinese_path, dtype=np.uint8), -1)
    # print(item.group(0))
    # print(item.group(1))
    s=s.replace(item_text,f' cv2.imdecode(np.fromfile({img_path}, dtype=np.uint8), -1)')

print(s)