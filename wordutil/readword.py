# -*- coding:utf-8 -*-
'''
Created by Administrator on 2018/3/22 0022.
'''
import sys

sourcefileds = []
sourceCode = []
if __name__ == '__main__':
    from docx import Document
    doc = Document("F:\AppCache\PythonUtils\wordutil\sy.docx")#type:docx.table._Row
    flag = False #字段命中标记
    operatorcount = 0#
    for line in open("JavaEntityFiled.filed"):
        sourcefileds.append(line.strip("\n"))
    for filed in sourcefileds:
        sourceCode.append("private String " + filed + ";")
    for tables in doc.tables:
        for row in tables.rows:
            for cell in row.cells:
               if( flag ):
                   flag = False #命中处理后设为False
                   sourceCode[index] += "//" + cell.text if (cell.text not in sourceCode[index]) else ""
                   break
               if cell.text in sourcefileds:
                   index = sourcefileds.index(cell.text)
                   flag = True
                   continue
               else:
                   flag = False
                   break
all = 0
unhit = 0
unhitarr=[]
for var in sourceCode:
    all += 1
    if "//" not in var:
        unhit+=1
        unhitarr.append(sourcefileds[all - 1])
    print var.encode("utf-8",'ignore')
print u"共有数据" + str(all) + u"条"
print u"未匹配数据" + str(unhit) + u"条"
print u'未匹配数据为:' + str(unhitarr)