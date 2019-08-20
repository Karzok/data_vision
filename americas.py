# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/8/15 9:44'
import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'North, Central, South America'
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')


