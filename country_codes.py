# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/8/15 9:26'
from pygal_maps_world.maps import COUNTRIES


def get_country_code(country_name):
    """根据指定的国家， 返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有 返回none
    return None
