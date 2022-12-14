# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:30:53 2020

@author: Eureka
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:54:33 2020

@author: Eureka
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:14:38 2020

@author: Eureka
"""
import json
import re
import os

path = "D:/yhh/Compressed/项目12 口红色号识别器/项目12 口红色号识别器/数据库/lipsticks/"
brand = "YSL/"
brandpathli = []
dict_Brand = {"name": brand[:-1], "series": None}
dict_series = {"name": None, "lipsticks": None}
dict_name = {"color": "#ffffff", "id": "-1", "name": "none"}


def par_mac(str):
    print("par_mac")
    dict_name = {"color": "#ffffff", "id": "-1", "name": "none"}
    print("try")
    matchObj_color = re.search(r'#\w{6}', str, re.M | re.I)
    if (matchObj_color != None):
        dict_name["color"] = matchObj_color.group()
        print(matchObj_color.group())
    matchObj_id = re.search(r"[°#]\d{1,3}", str, re.M | re.I)
    if (matchObj_id != None):
        dict_name["id"] = matchObj_id.group()
        print(matchObj_id.group())
    matchObj_name = re.search(r"[\u4e00-\u9fa5]*", str, re.M | re.I)
    if (matchObj_name != None):
        dict_name["name"] = matchObj_name.group()
        print(matchObj_name.group())
    else:
        print("No name")
    #    print(dict_name)
    #    except Exception:
    #        print("errror",Exception)
    #        pass
    #    finally:
    return dict_name


def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        print("children", child)
        brandpathli.append(child)


def readFile(filename):
    fopen = open(filename, 'r', encoding='UTF-8')  # r 代表read#, encoding='UTF-8'
    list_series = []  # 文件中每一行的内容
    for eachLine in fopen:
        print("读取到得内容如下：", eachLine)
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
    for i in brandpathli:
        readFile(i)
