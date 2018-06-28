#! usr/bin/env
# _*_coding:utf-8_*_
import os

'''
for i in range(21):
    if i%3 == 0:
        if i%5 == 0:
            i = str('appleorange')
        else:
            i = str('apple')
    elif i%5 == 0:
        i = str('orange')
    print(i)
'''
#print( [ 'apple'[i %3*5::] +'orange'[i %5*6::] or i for i in range(1,21)])
'''
a,b = 0,1
while b < 10:
    print(b)
    a,b = b, a + b

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          ]
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
        print(transposed_row)
'''
    #transposed.append(transposed_row)

'''
import os
import sys
import random



count = 0
for a in range(9):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    if ((a != 4) & (b != 4) & (c != 4) & (d != 4) & (e != 4)):
                        count += 1
print(count)


# !/usr/bin/env python
x = input("input your word:")
i = 0
while i < len(x):
    print(x[i])
    i += 1
'''

from selenium import webdriver
import time


def open_web(sum):
    req_url = "https://u.uat.7atour.com/usercenter/login?return=https%3A%2F%2Fwww.uat.7atour.com%2F"
    # 打开浏览器
    browser = webdriver.Chrome()
    browser.maximize_window()
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
        print(num + 1)
        if num >= 3:
            browser.find_element_by_id("verifyCode").clear()
            browser.find_element_by_id("verifyCode").send_keys("wwii")
            time.sleep(1)
            browser.find_element_by_xpath("//*[@id='login']/div/ul/li/div/div[2]/div/button").click()
        else:
            browser.find_element_by_xpath("//*[@id='login']/div/ul/li/div/div[2]/div/button").click()
        num += 1
    # 关闭当前窗口
    browser.close()
    # 关闭所有已经打开的窗口
    browser.quit()


if __name__ == "__main__":
    #count = input("输入需要循环登录的次数：")
    count = 4
    open_web(count)
