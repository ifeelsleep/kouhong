# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:14:38 2020

@author: Eureka
"""
import json
import re
import os

path = "D:/yhh/Compressed/项目12 口红色号识别器/项目12 口红色号识别器/数据库/lipsticks/"
brand = "mac/"
brandpathli = []
dict_Brand = {"name": brand[:-1], "series": None}
dict_series = {"name": None, "lipsticks": None}
dict_name = {"color": "#ffffff", "id": "-1", "name": "none"}


def par_mac(str):
    dict_name = {"color": "#ffffff", "id": "-1", "name": "none"}
    matchObj_color = re.search(r'#\w{6}', str, re.M | re.I)
    if (matchObj_color != None):
        dict_name["color"] = matchObj_color.group().upper()
    #        print (matchObj_color.group())
    matchObj_id = re.search(r"\">\d{3}", str, re.M | re.I)
    if (matchObj_id != None):
        dict_name["id"] = matchObj_id.group()[2:]
    #        print (matchObj_id.group()[2:])
    matchObj_name = re.search(r">\d{0,}[ ]?([A-Z][a-z]*[,]?[ ]?[!?]?){1,}", str, re.M | re.I)
    if (matchObj_name != None):
        dict_name["name"] = matchObj_name.group()[1:]
    #        print (matchObj_name.group()[1:])
    #    print(dict_name)
    return dict_name


#    else:
#        print ("No name")

def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        print("children", child)
        brandpathli.append(child)


def readFile(filename):
    fopen = open(filename, 'r')  # r 代表read
    list_series = []  # 文件中每一行的内容
    for eachLine in fopen:
        #        print( "读取到得内容如下：",eachLine)
        dict_name = par_mac(eachLine)
        if (dict_name["color"] == "#ffffff"):
            continue
        list_series.append(dict_name)
    fopen.close()
    #    print("list_series!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1",list_series)
    return list_series  # 返回每个系列的所有口红


if __name__ == '__main__':
    #    filePath = path+brand+subpath
    filePathC = path + brand
    eachFile(filePathC)

    list_brand = []
    for i in brandpathli:
        dict_series = {"name": None, "lipsticks": None}
        list_series = readFile(i)  # 每个系列的所有口红
        #        print(dict_name)
        brandname = i.split('/')[-1].split('.')[0]
        #        print("mainpring",brandname)
        dict_series["name"] = brandname
        dict_series["lipsticks"] = list_series
        """获得{系列名，口红色号}字典"""
        list_brand.append(dict_series)
        print("dict_series********************************************", list_brand)
    dict_Brand["series"] = list_brand
    #        dict_Brand["brands"][1]["series"]

    file = open('D:/homework/大三下信息系统设计/json/' + brand.split('/')[0] + '.json', 'w', encoding='utf-8')
    json = json.dump(dict_Brand, file)
    print(json)
    file.close()
