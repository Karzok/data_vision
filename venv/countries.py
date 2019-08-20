# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/8/15 9:20'
from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
