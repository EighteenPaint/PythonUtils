# -*- coding:utf-8 -*-
#This is a tool to crawler geoJson for BPH
#各个省市地区json下载地址http://www.ourd3js.com/wordpress/638/#more-638
import urllib2
from CityData import cityDataDict
url_pre = 'http://echarts.baidu.com/echarts2/doc/example/geoJson/china-main-city/'
if __name__ == '__main__':
    try:
        for item in cityDataDict:
            url = url_pre + cityDataDict[item] + '.json'
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            jsonData = response.read()
            file_name = item + '.json'
            jsonFile = open( file_name.decode('utf-8'),'wb')
            jsonFile.write(jsonData)
            print file_name
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason