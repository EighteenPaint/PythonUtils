# -*- coding:utf-8 -*-
'''
Created by Administrator on 2018/12/13 0013.
'''
import urllib
import urlparse

import urllib2

data = {}
data['type'] = 'movie'
data['source'] = 'index'
# data['tag'] = u'z'.encode("UTF-8")
url = "https://movie.douban.com/j/search_tags?type=%(type)s&source=%(source)s" % data
print url
page = urllib2.urlopen(url)
page_data = page.read()
print page_data
