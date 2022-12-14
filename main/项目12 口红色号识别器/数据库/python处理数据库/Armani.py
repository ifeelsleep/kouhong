# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:19:56 2020

@author: Eureka
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:51:35 2020

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
brand = "Armani/"
brandpathli = []

dict_Brand = {"name": brand[:-1], "series": None}
dict_series = {"name": None, "lipsticks": None}
dict_name = {"color": "#ffffff", "id": "-1", "name": "none"}
"""
这是现在主要出问题的部分，它不能有效的获得字符串中的中文字符和色号
"""


def par_mac(str):
    print("par_mac")
    dict_name = {"color": "#ffffff", "id": "-1", "name": "none"}
    #    try:
    if (1):
        print("try")
        matchObj_color = re.search(r'#\w{6}', str, re.M | re.I)
        if (matchObj_color != None):
            dict_name["color"] = matchObj_color.group().upper()
            print(matchObj_color.group())
        matchObj_id = re.search(r" \d{3}", str, re.M | re.I)
        if (matchObj_id != None):
            dict_name["id"] = matchObj_id.group().split(' ')[-1]
            print(matchObj_id.group().split(' ')[-1])
        matchObj_id = re.search(r"data-colorid=\"[_]{0,1}\w{3}.{0,3}[_]{0,1}[new]{0,1}\"", str, re.M | re.I)
        if (matchObj_id != None):
            temp = matchObj_id.group().split('\"')[-2].split('_')
            for index in temp:
                print(index)
                if (re.search(r"\d{3}", index, re.M | re.I) is not None):
                    print("indexis", index)
                    dict_name["id"] = index
        matchObj_name = re.search(r">.{0,}\d{3}.{0,}[\u4e00-\u9fa5]{0,}\w{0,}</op", str, re.M | re.I)
        if (matchObj_name != None):
            #            dict_name["name"]=matchObj_name.group()
            temp = matchObj_name.group().split("<")[-2].split(' ')
            for index in temp:
                print(index)
                if (re.search(r"[A-Z]{1,}|[a-z]{1,}|[\u4e00-\u9fa5]{1,}", index, re.M | re.I) is not None):
                    if (index == "热卖色" or index == "（HOT）" or index == "新品" or index == "new" or (
                            re.search(r"\d{3}", index, re.M | re.I) is not None)):
                        continue
                    print("indexis", index)
                    dict_name["name"] = index
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
        print("children", child)  # 文件夹中所有文件的文件名
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
    #        print("dict_series********************************************",list_brand)
    dict_Brand["series"] = list_brand
    #        dict_Brand["brands"][1]["series"]

    file = open('D:/homework/大三下信息系统设计/json/' + brand.split('/')[0] + '.json', 'w', encoding='utf-8')
    json = json.dump(dict_Brand, file)
    print(json)
    file.close()
