# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:22:16 2020

@author: Eureka
"""

import face_recognition

image = face_recognition.load_image_file("D:/homework/大三下信息系统设计/tyjteat/4.jpg")
face_locations = face_recognition.face_locations(image)
print(len(face_locations))