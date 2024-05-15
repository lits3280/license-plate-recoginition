# coding=utf-8
"""
@Author:lts
@Time:2024/3/28 14:24
@description:
"""

from data.random_plate import Draw_cfg

my_draw = Draw_cfg([None])
# plate = my_draw._create_jundui_plateno(type='en')

for i in range(20):
    plate = my_draw._create_jundui_plateno(type='ch')
    # plate = my_draw._create_jundui_plateno(type=None)
    print(plate)