# coding=utf-8
"""
@Author:lts
@Time:2024/4/12 17:50
@description:
"""

# class Demo:
#
#     def __init__(self, value) -> None:
#         self.name = value
#
#     def __str__(self) -> str:
#         return 'name=' + str(self.name)


data_map = {"a": 1, "b": 1}

data_map2 = {"a2": data_map['a']}

# del(data_map['a'])
del data_map['a']
print(data_map)
print(data_map2)


def del_list():
    a = [1, 2, 3]
    b = a  # 创建了一个引用指向 a
    del a  # 删除了对 a 的引用
    print(b)  # 仍然可以通过 b 访问到原来的列表 [1, 2, 3]


def del_map():
    # map中删除
    data_map = {"a": 1, "b": 1}
    del data_map['a']
    print(data_map)
