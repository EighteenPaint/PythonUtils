# -*- coding:utf-8 -*-
'''
Created by Administrator on 2019/3/29 0029.
'''
import re
res = r'(.*?)</p>'
imgre = re.compile(res)
file_name = "XZQH.html"
if __name__ == '__main__':
    array = []
    with open(file_name,'r') as f:
        for i in f:
            imglist = re.findall(imgre,i)
            if len(imglist) > 0:
                for str in imglist:
                    array.append(str.strip())
    print "length",len(array)
    print "group",len(array)/4
    for index in range(len(array)/4):
        start = index*4
        print "INSERT INTO  t_jq_dict (`code`,`name`,`type_code`) VALUES ('{}', '{} {} {}',19);".format(array[start],array[start+1],array[start+2],array[start+3])

