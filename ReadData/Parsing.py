'''
Created on 2018. 5. 3.

@author: SEHWA
'''
#coding: utf-8

from Connection.Connection import driver
import selenium
from selenium.common.exceptions import NoSuchAttributeException,\
    NoSuchElementException

#[배우/제작진] 제작사/수입사/배급사 파싱
def agency():
    try:
        agency_name = driver.find_element_by_xpath("//dl[@class='agency_name']")
        agency_text = agency_name.text
        
        try:
            producer_test = driver.find_elements_by_class_name("agency_sub0")
            if producer_test == [] :
                producer_test = None
        except NoSuchElementException:
            print("제작사 없음")
            producer_test = None
        
        try:
            importer_test = driver.find_element_by_class_name("agency_sub1")
            if importer_test == []:
                importer_test = None
        except NoSuchElementException:
            print("수입사 없음")
            importer_test = None 
            
        try:
            distributor_test = driver.find_element_by_class_name("agency_sub2")
            if distributor_test == []:
                distributor_test = None
        except NoSuchElementException:
            print("배급사 없음")
            distributor_test = None
            
        if producer_test is not None and importer_test is not None and distributor_test is not None :
            producer = agency_text.split('\n')[0]
            importer = agency_text.split('\n')[1]
            distributor = agency_text.split('\n')[2]
            print("제작사 : " + producer)
            print("수입사 : " + importer)
            print("배급사 : " + distributor)
        elif producer_test is not None and importer_test is not None and distributor_test is None:
            producer = agency_text.split('\n')[0]
            importer = agency_text.split('\n')[1]
            print("제작사 : " + producer)
            print("수입사 : " + importer)
        elif producer_test is not None and importer_test is None and distributor_test is not None:
            producer = agency_text.split('\n')[0]
            distributor = agency_text.split('\n')[1]
            print("제작사 : " + producer)
            print("배급사: " + distributor)
        elif producer_test is None and importer_test is not None and distributor_test is not None:
            importer = agency_text.split('\n')[0]
            distributor = agency_text.split('\n')[1]
            print("수입사 : " + importer)
            print("배급사 : " + distributor)
        elif producer_test is not None and importer_test is None and distributor_test is None:
            producer = agency_text
            print("제작사 : " + producer)
        elif producer_test is None and importer_test is not None and distributor_test is None:
            importer = agency_text
            print("수입사 : " + importer)
        elif producer_test is None and importer_test is None and distributor_test is not None:
            distributor = agency_text
            print("배급사 : " + distributor)
        else:
            print("정보 없음")
    except NoSuchElementException:
        agency_name = None
        print('정보 없음')
    
#[평점] 개봉 전 평점 정보 파싱
def beforeOpeningscore():
    try:
        #기대 지수
        expectateIndex = driver.find_element_by_class_name("exp_info")
        like = expectateIndex.text.split('\n')[0]
        dislike = expectateIndex.text.split('\n')[1]
        print("보고싶어요 : " + like)
        print("글쎄요 : " + dislike)
        
        #네티즌 평점
        star_score_text = driver.find_element_by_id("beforePointArea")
        star_score = star_score_text.text.split('\n')[3]
        participator = star_score_text.text.split('\n')[4]
        print("개봉 전 평점 : " + star_score)
        print("참여자 수 : " + participator.replace("참여", ""))
    except:
        print("국내 개봉 되지 않은 영화입니다")
    