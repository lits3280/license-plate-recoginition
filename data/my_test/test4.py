# coding=utf-8
"""
@Author:lts
@Time:2024/3/15 16:05
@description:
"""
import random
import numpy as np
class Demo :
    def __init__(self) -> None:
        self._provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新"]
        self._alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self._ads = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self._check = ["D", "F"]
        self._checknum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self._emergency = ["X", "S"]

    def random_alpha_num(self,alpha_p=0.5,size=4):
        s_list=[]
        for i in range(0,size):
            s = random.choice(self._alphabets) if random.random() <= alpha_p else random.choice(self._checknum)
            s_list.append([s])
        return s_list


nums=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

d=Demo()
counter=0
for i in range(200 ):
    # counter+=d.random_plate_common()
    c=d.random_alpha_num(alpha_p=0.4)
    # if c in nums:
    #     counter +=1
    print(c)
print(f'counter={counter}')