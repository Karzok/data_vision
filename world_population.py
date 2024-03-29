# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/8/15 9:06'
import json
import pygal_maps_world.maps

from country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'C:\Workspace\data_vision\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(country_name + ":" + str(population))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            print("ERROR - " + country_name)
# 根据人口数量把所有国家都分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm = pygal_maps_world.maps.World()
wm.title = "World Population in 2010, by Country"
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('population_world.svg')
