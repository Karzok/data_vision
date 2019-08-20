# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/8/12 10:06'

import matplotlib.pyplot as plt

from Random_walk import RamdonWalk

while True:
    # 创建一个RandomWalk的实例，并将其包含的点都绘制出来
    rw = RamdonWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none',  s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=10)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=10)

    # 隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
