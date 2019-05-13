# -*- coding:utf-8 -*-
'''
Created by Administrator on 2018/12/10 0010.
通过读取文件获取下载的URL
'''
import urllib
import re
import sys
with open(u"mobi.txt",'r') as f:
    reg = r'<a href="(https://.*?)".*?>(.*?\.mobi)'
    imgre = re.compile(reg)
    for i in f:
        imglist = re.findall(imgre,i)
        if len(imglist) > 0:
            url = imglist[0][0]
            name = imglist[0][1].decode(encoding="utf-8")
            print url,name
            print 'downloading ',name
            urllib.urlretrieve(url, name)
