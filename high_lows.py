# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/8/13 10:39'
import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    dates = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

# 根据数据绘制图像
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# 设置图形的格式
plt.title("Daily high temperatures, July-2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
