# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/8/13 9:24'
from random import randint


class Die():
    """创建一个表示骰子的类"""

    def __init__(self, num_sides=6):
        """6面骰子"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面之间的随机值"""
        return randint(1, self.num_sides)
