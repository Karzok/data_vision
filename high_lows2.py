# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/8/14 9:44'
import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    dates = []
    lows = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

        current_date = datetime.strptime(row[2], "%Y/%m/%d")
        dates.append(current_date)

        low = int(row[6])
        lows.append(low)

# 根据数据绘制图像
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures-2018", fontsize=24)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()