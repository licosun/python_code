#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/9 12:58
# @Author  : lixiaobo
# @Site    : 
# @File    : photo.py
# @Software: PyCharm
# @license: (C) Copyright 2018-2027, By lixiaobo.

import requests
from bs4 import BeautifulSoup

url = 'http://desk.zol.com.cn/pc/'
#url = 'http://www.mzitu.com'
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
html = requests.get(url,headers = header )

soup = BeautifulSoup(html.text,'html.parser')

#all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')
all = soup.find_all('li',class_ = 'photo-list-padding')
#print(all)
for a in all:
    #title = a.get_text() #提取文本
    #links = a.find(name = 'a').get('href')
    print(a)

"""

list = [1, 2, 3, 4, 5]
print("(1)取五个数的和；\n(2)取五个数的平均数；\n(x)退出；\n")

while True:
    s = input("input your choice:")
    sum = 0
    x = s.isdigit()
    y = s.isalpha()

    if x == True:
        if int(s) ==1:
            for i in list:
                sum += i
            print(sum)

        elif int(s) == 2:
            for i in list:
                sum += i
            print(sum/5)

    elif y == True:
        if s == "x":
            print("退出")
            break

