# -*- coding:utf-8 -*-
#生成所有城市的URL
from CityData import cityDataDict

if __name__ == '__main__':
    for name in cityDataDict:
        print '"' + str(name) + '":"<%=basePath %>Skin/Blue/js/cityJson/' + name + '.json",'