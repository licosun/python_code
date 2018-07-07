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
"""

#list=['appKey', 'secretKey', 'token', 'userName', 'password', 'isVerify', 'verifyCode', 'loginType', 'terminalType']
#print(sorted(list))
"""
# !/usr/bin/env python3
# _*_ coding: UTF-8 _*_

import asyncio
import random

from selenium import webdriver
import time


async def open_web(sum):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    req_url = "https://u.uat.7atour.com/usercenter/login?return=https%3A%2F%2Fwww.uat.7atour.com%2F"
    browser = webdriver.Chrome()
    #browser.maximize_window()
    # 开始请求
    browser.get(req_url)
    # 延时
    
    time.sleep(1)
    num = 0
    while num < sum:
        browser.find_element_by_id("username").clear()
        browser.find_element_by_id("username").send_keys("15902029720")
        time.sleep(1)
        browser.find_element_by_id("password").clear()
        browser.find_element_by_id("password").send_keys("123456addd")
        time.sleep(1)
        #print(num + 1)
        if num >= 3:
            browser.find_element_by_id("verifyCode").clear()
            browser.find_element_by_id("verifyCode").send_keys("wwii")
            time.sleep(1)
            browser.find_element_by_xpath("//*[@id='login']/div/ul/li/div/div[2]/div/button").click()
        else:
            browser.find_element_by_xpath("//*[@id='login']/div/ul/li/div/div[2]/div/button").click()
        num += 1
    
    browser.close()
    # 关闭所有已经打开的窗口
    browser.quit()
    print("协程：{}， 执行完毕。 用时：{} 秒".format(sum, process_time))

async def MyCoroutine(id):
	process_time = random.randint(1, 5)
	await asyncio.sleep(process_time)
	print("协程：{}， 执行完毕。 用时：{} 秒".format(id, process_time))

async  def main(id):
	tasks = [asyncio.ensure_future(open_web(sum))for sum in range(9)]
	await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
try:
	loop.run_until_complete(main(5))
finally:
    loop.close()

"""
from bs4 import BeautifulSoup
import requests, sys

"""
类说明：下载《笔趣阁》网小说《一念永恒》
Parameters:
 无
Returns:
 无
Modify:
  2018-07-03
"""
"""
class downloader(object):

	def __init__(self):
		self.server = 'http://www.biqukan.com'
		self.target = 'http://www.biqukan.com/1_1094'
		self.names = []
		self.urls = []
		self.nums = 0
	
	函数说明：获取下载链接
	Parameters:
     无
    Returns:
     无
    Modify:
       2018-07-03
	
	def get_download_url(self):
		req = requests.get(url = self.target)
		html = req.text
		div_bf = BeautifulSoup(html, "html.parser")
		div = div_bf.find_all('div', class_ = 'listmain')
		a_bf = BeautifulSoup(str(div[0]))
		a = a_bf.find_all('a')
		self.nums = len(a[15:])   #剔除不必要的章节，并统计章节数
		for each in a[15:]:
			self.names.append(each.string)
			self.urls.append(self.server + each.get('href'))

	
		函数说明：获取章节内容
		Parameters:
	      target - 下载链接（string）
	    Returns:
	      texts - 章节内容（string）
	    Modify:
	       2018-07-03
	
	def get_contents(self, target):
		req = requests.get(url = target)
		html = req.text
		bf = BeautifulSoup(html, "html.parser")
		texts = bf.find_all('div', class_ = 'showtxt')
		texts = texts[0].text.replace('\xa0'* 8, '\n\n')
		return texts

	
			函数说明：将爬取的内容写入文件
			Parameters:
		      name - 章节名称（string）
		      path - 当前路径下，小说保存名称（string）
		      text - 章节内容（string）
		    Returns:
		       无
		    Modify:
		       2018-07-03
	

	def write(self, name, path, text):
		write_flag = True
		with open(path, 'a', encoding = 'utf-8') as f:
			f.write(name + '\n')
			f.writelines(text)
			f.write('\n\n')

if __name__ == '__main__':
	dl = downloader()
	dl.get_download_url()
	print(dl.get_download_url())
	#print(" 《一念永恒》开始下载：")
	for i in range(dl.nums):
		dl.write(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
		sys.stdout.write("    已下载：%.3f%%" % float(i/dl.nums*100) + '\r')
		sys.stdout.flush()
	print(' 《一念永恒》 下载完成！！')
"""
# -*- coding: utf-8 -*-
"""
遍历某路径下所有文件夹，获得特定文件夹下所有文件
很暴力，真的遍历了所有的文件夹
20180124
@author: 墨大宝

import os,re

TARGETPATH = r'D:\MODIS_DATA'
records = []
for currentDir, _, includedFiles in os.walk(TARGETPATH):
    #if not currentDir.endswith(r'_BAD'): continue
	if not re.compile(r'_BAD'):continue

    else:
        records.append(currentDir)# 将以“_BAD”结尾的文件夹名加入records
        records.extend(includedFiles)  # 将该文件夹内的文件名列表扩展到records

# 将records写入.txt
print(records)
txtFile = open(os.path.join(TARGETPATH, '02_04.txt'), 'w')
txtFile.write(os.linesep.join(records))
txtFile.close()

# 将排序后的records写入.txt
with open(os.path.join(TARGETPATH, '02_04_BAD_SORTED.txt'), 'w') as txtFile:
    txtFile.write('\n'.join(sorted(records)))
"""
'''
import os
import sys
import re

#根据文件夹 截取文件名称
def getFileList(path ):
   for root, dirs, names  in os.walk(path):
       pattern = re.compile(r'_BAD')#将正则表达式设置成pattern对象
       for filename in names:
           if pattern.search(filename): #判断filename中是否包含XX，如果包含，则返回true
               print(filename)  #打印



if __name__ == '__main__':
    path =r'D:\MODIS_DATA'

    getFileList(path)
'''

d = {"remote_addr": "121.8.243.139", "request": "GET /css/common__f13e01879d.css HTTP/1.1",
	 "geoip": {"country_name": "China", "country_code2": "CN", "city_name": "Guangzhou", "region_name": "Guangdong"},
	 "offset": 142255, "body_bytes_sent": "8811", "prospector": {"type": "log"}, "request_method": "GET",
	 "source": "/opt/log/nginx/www.test1_access.log",
	 "http_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
	 "tags": ["www_test1", "beats_input_codec_json_applied"], "remote_user": "-", "request_time": "0.021",
	 "@timestamp": "2018-07-05T08:27:18.972Z", "http_x_forwarded_for": "-", "@version": "1",
	 "beat": {"name": "dev-nginx", "hostname": "dev-nginx", "version": "6.2.2"}, "host": "dev-nginx",
	 "http_referrer": "http://www.test1.7atour.com/macaohkset/list", "time": "05/Jul/2018:11:32:56 +0800",
	 "status": "200"}

lt = []  # 定义一个列表接收解析数据

s = d.get('status')  # 获取状态用于判断是否需要

if s == "200":  # 判断数据是否需要解析
	# print(d.values())
	for y in d:
		if type(d[y]) == dict:  # 判断json内嵌为字典则取值
			for k in d[y]:
				lt.append(d[y][k])

		elif type(d[y]) == list:  # 判断json内嵌为列表则取值
			for i in d[y]:
				lt.append(i)

		else:
			lt.append(d[y])

else:
	print("d[geoip]")

print(lt)
