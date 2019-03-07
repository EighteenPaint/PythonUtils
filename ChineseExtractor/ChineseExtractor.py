# -*- coding:utf-8 -*-
'''
Created by Administrator on 2019/3/4 0004.
'''
import re
import sys

reload(sys)
sys.setdefaultencoding("utf8")


def translateZh(str):
    line = str.strip().decode('utf-8', 'ignore')  # 处理前进行相关的处理，包括转换成Unicode等
    p2 = re.compile(ur'[^\u4e00-\u9fa5,\d]')  # 中文的编码范围是：\u4e00到\u9fa5
    zh = " ".join(p2.split(line)).strip()
    zh = ",".join(zh.split())
    outStr = zh  # 经过相关处理后得到中文的文本
    return outStr
def translateEn(str):
    line = str.strip().decode('utf-8', 'ignore')
    uncn = re.compile(ur'[\w+,\u0020，\']')
    zh =re.compile(ur'[^\u4e00-\u9fa5]')
    if len("".join(zh.split(line)).strip()) is not 0:
        return None
    en = "".join(uncn.findall(str))
    # print(en)
    return en
if __name__ == '__main__':
    f = open(u'2019年3月7日.txt', 'r')
    s = f.readlines()

    f.flush()
    f.close()
    strEn = ""
    strZh = ""
    for fileLine in s:
        result = translateEn(fileLine);
        if(result):
            strEn += result
            strEn+= "."
    print strEn
    for fileLine in s:
        result = translateZh(fileLine);
        if (result):
            strZh += result
            strZh += "。"
    print strZh
