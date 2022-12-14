# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:08:30 2020

@author: Eureka
"""

import numpy as np
from collections import Counter
from PIL import Image,ImageDraw
import face_recognition
import colorsys
import json


class my_face_recognition(object):
    def __init__(self):
        self.imgPath = ''
        self.imgDir = ''
        self.img = None
        self.resultImg = None
        self.resultImgName = ''
        self.register_lps=[]
        self.register_rgb=[]
        self.errdet='DEAL'
    def showImg(self, img_type='original'):
        if img_type =='original':
            Image.open(self.imgPath)#绘制图片
    def operates_(self,input_path):
        self.imgPath=input_path#展示图片

    def AI(self):
        self.load_pic()
        self.get=self.get_dominant_color(self.resultImg)
        print("the extracted RGB value of the color is {0}".format(self.get))
        #operate the data#
        self.data_operate()
    def errordetect(self):#错误处理
        image = face_recognition.load_image_file(self.imgPath)
        face_locations = face_recognition.face_locations(image)
        if(len(face_locations)!=1):
            if(len(face_locations)==0):
                print("noface")
                self.errdet="more/less than one face in the pic"
                return "can't find people"
                self.errdet="more/less than one face in the pic"
            return "more/less than one face in the pic"
        else:
            return "DEAL"
    def load_pic(self):
        
        self.errdet=self.errordetect()
        image = face_recognition.load_image_file(self.imgPath)
        # Find all the faces in the image
#        print(type(image))
        face_locations = face_recognition.face_locations(image)
#        print(face_locations)
        # Or maybe find the facial features in the image
        face_landmarks_list = face_recognition.face_landmarks(image)
#        print(face_landmarks_list)
        pos = face_locations[0]
        pil_image =Image.open(self.imgPath)
#        print(type(pil_image),pil_image.size)
        cropped_face = pil_image.crop((pos[3], pos[0], pos[1], pos[2])) # (left, upper, right, lower) 左上，右下
#        Image._show(cropped_face)
#        print(type(cropped_face),cropped_face.size)
        pil_image = Image.fromarray(image)
        a=pil_image.size
#        print(a,type(a))
        blank_mouse = Image.new('RGB', (a[0],a[1]), (0, 0, 0))
        for face_landmarks in face_landmarks_list:
            d = ImageDraw.Draw(blank_mouse, 'RGBA')
            # Gloss the lips
            d.polygon(face_landmarks['top_lip'], fill=(255,255,255,255))
            d.polygon(face_landmarks['bottom_lip'], fill=(255, 255,255, 255))
            d.line(face_landmarks['top_lip'], fill=(255, 255,255, 255), width=1)
            d.line(face_landmarks['bottom_lip'], fill=(225, 255, 255,255), width=1)
            #blank_mouse.show()
        blank_mouse=blank_mouse.crop((pos[3], pos[0], pos[1], pos[2])) # (left, upper, right, lower) 左上，右下
#        Image._show(blank_mouse)
        self.resultImg=self.masklayer(cropped_face,blank_mouse)

    def masklayer(self,origin,mask):
        mask1=np.array(mask)
#        print(mask1.shape)
        origin1=np.array(origin)
#        print(origin1.shape)
        for i in range(len(mask1)):
            for j in range(len(mask1[i])):
   #          print(mask1[i][j][1])
                if (mask1[i][j][1]>=128):#lip
                    pass
                else:#others
                    origin1[i][j]=[0,0,0]
        new_png = Image.fromarray(origin1)
#        new_png.show()
    #new_png.save('C:/Users/MCY/Desktop/test7.JPG')
        return new_png

    def get_dominant_color(self,image):
    #颜色模式转换，以便输出rgb颜色值
        image = image.convert('RGB')
     
    #生成缩略图，减少计算量，减小cpu压力
        image.thumbnail((200, 200))
        max_score = 0
        dominant_color = 0
        for count,(r,g,b) in image.getcolors(image.size[0]*image.size[1]):
            if (r<100) :
                continue
        # 转为HSV标准
            saturation = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)[1]
            y = min(abs(r*2104+g*4130+b*802+4096+131072)>>13,235)
            y = (y-16.0)/(235-16)
  
        #忽略高亮色
            if y > 0.9:
                continue
            score = (saturation+0.1)*count
            if score > max_score:
                max_score = score
                dominant_color = (r,g,b)
        return dominant_color
        ##write the temp data to file##
                
#operate the data #
##save the brand&series&color id&color name to sum_list##
##covert the color #D62352 to RGB_array##
##caculate the RGB difference to RGB_temp and write the value to file##
    
    def RGBhex_2RGB(self,rgb_hex):
#     print(rgb_hex)
        RGB=[0,0,0]
        temp_num=0
        for i in range(len(rgb_hex)):
            temp_num=0
            temp=rgb_hex[i]
            if(i!=0):
            #将字母转换为ASCII表中位置
                if(temp>='A'and temp<='F'):
                    temp_num=ord(temp)-55
                #将ABCDEF转换为10_15间的数字
                else:
                #将字符数字转换为0_9间的数字
                    temp_num=ord(temp)-48
                if(i%2==1):
                #根据位置乘进制
                    RGB[int((i/2)-0.5)]=RGB[int((i/2)-0.5)]+16*temp_num
                else:
                    RGB[int((i/2)-0.5)]=RGB[int((i/2)-0.5)]+temp_num
#     print(RGB)
        return RGB
                    
    def data_operate(self):
        target_color=self.get
        if(self.errdet=="more/less than one face in the pic"):
            self.errdet="WE CAN'T DEAl WITH IT"
            return 0
        if(self.errdet=="can't find people"):
            self.errdet="WE CAN'T DEAl WITH IT"
            return 0
        sum_all=0
        with open('lipstick.json', 'r', encoding='utf-8') as f:
            js2dic = json.load(f)
        #读取json
            brands_n=len(js2dic['brands'])
            print(brands_n)
            series_n=0
            for brands_i in range(brands_n):
                series_n=len(js2dic['brands'][brands_i]['series'])
                print("{0} has {1} series".format((js2dic['brands'][brands_i]['name']),series_n))
                for series_i in range(series_n):
                    color_num=len(js2dic['brands'][brands_i]['series'][series_i]['lipsticks'])
                    sum_all=color_num+sum_all
            #计算颜色总数
                print(sum_all)
            catalog=np.zeros((sum_all,4), dtype=(str,20))
            catalog_color=np.zeros((sum_all,3), dtype=int)
#         根据颜色数分配空间
       
        #catalog分为四部分：品牌名称，唇膏名称，色号id，色号值
        #将信息存入表格
            sum_i=0
            for brands_i in range(brands_n):
                series_n=len(js2dic['brands'][brands_i]['series'])
                print("brand_name",js2dic['brands'][brands_i]['name'])
                catalog[sum_i][0]=js2dic['brands'][brands_i]['name']
                for series_i in range(series_n):
                    color_num=len(js2dic['brands'][brands_i]['series'][series_i]['lipsticks'])
                    for color_i in range(color_num):
                        catalog[sum_i][0]=js2dic['brands'][brands_i]['name']
                        catalog[sum_i][1]=js2dic['brands'][brands_i]['series'][series_i]['name']
                        catalog[sum_i][2]=js2dic['brands'][brands_i]['series'][series_i]['lipsticks'][color_i]['name']
                        catalog[sum_i][3]=js2dic['brands'][brands_i]['series'][series_i]['lipsticks'][color_i]['id']
                        catalog_color[sum_i]=self.RGBhex_2RGB(js2dic['brands'][brands_i]['series'][series_i]['lipsticks'][color_i]['color'])
                        sum_i+=1
#                     print(sum_i)
            print(catalog.shape)
            RGB_distance=np.zeros((sum_all,1), dtype=float)
            for i in range(sum_all):
            #计算相似度，target是此前通过domain得到的值
                RGB_distance[i]=abs(target_color[0]-catalog_color[i][0])+abs((target_color[1]-catalog_color[i][1])*1/5)+abs(target_color[2]-catalog_color[i][2])
            RGB_distance.tolist()
            result=sorted(range(len(RGB_distance)), key=lambda k: RGB_distance[k])
#         获得颜色最像的三只口红的（以颜色的相近度为规则排序，返回位置数据）
            print("颜色最像的三只口红及其颜色")
            for i in range(3):
                loc=result[i]
                color_show=tuple(catalog_color[loc])
                print("catalog index",catalog[loc],color_show)
                self.register_lps.append(catalog[loc])
                self.register_rgb.append(color_show)