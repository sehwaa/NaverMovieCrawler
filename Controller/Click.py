'''
Created on 2018. 5. 3.

@author: SEHWA
'''
#coding: utf-8

from Connection.Connection import driver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

#검색 버튼 클릭
def submitBtn():
    driver.find_element_by_class_name("btn_srch").click()

#자동 완성 리스트 클릭
def autoCompletementList(movieName):
    driver.implicitly_wait(5)
    element = driver.find_element_by_xpath("//li[@data-title='"+movieName+"']")
    element.click()

#'주요 정보'탭 클릭
def mainInformationTab():
    driver.find_element_by_xpath("//a[@title='주요정보']").click()
    
#'배우/제작진'탭 클릭
def actorTab():
    driver.find_element_by_xpath("//a[@title='배우/제작진']").click()
    
#'평점'탭 클릭
def scoreTab():
    driver.find_element_by_xpath("//a[@title='평점']").click()
    
#'평점'탭 클릭후 - '개봉 전 평점' 메뉴 클릭
def beforeOpening():
    driver.find_element_by_id("beforePointTab").click()
    
#'평점'탭 클릭후 - '개봉 후 평점' 메뉴 클릭
def afterOpening():
    driver.find_element_by_id("afterPointTab").click()

#'개봉 후 평점'메뉴 클릭 후 '남녀별/연령별' 메뉴 클릭
def netizenGenderAndAge():
    driver.find_element_by_xpath("//a[@id='netizen_group']").click()
    
#'개봉 후 평점'메뉴 클릭 후 '관람객 평점' 탭 클릭
def audienceScore():
    driver.find_element_by_xpath("//div[@class='title_area grade_tit']").click()
    
#'관람객 평점' 탭 클릭 후 '남녀별/연령별' 메뉴 클릭
def audienceGenderAndAge():
    driver.find_element_by_xpath("//a[@id='actual_group']").click()
    
#성인 인증시 로그인
def adultLogin():
    _id = driver.find_element_by_id("id")
    _id.send_keys("####") #개인정보 문제로 블락
    _pwd = driver.find_element_by_id("pw")
    _pwd.send_keys("####") #개인정보 문제로 블락
    driver.find_element_by_xpath("//input[@type='submit']").click()