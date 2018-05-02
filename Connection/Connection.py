'''
Created on 2018. 5. 3.

@author: SEHWA
'''
#coding: utf-8

from selenium import webdriver

#ChromeDriver로 접속, 자원 로딩시간 3초
driver = webdriver.Chrome('E:/ChromeDriver/chromedriver')
driver.implicitly_wait(3)

#웹페이지 불러오기
driver.get('https://movie.naver.com/')