'''
Created on 2018. 5. 3.

@author: SEHWA
'''
#coding: utf-8

from Connection.Connection import driver

#영화 검색란에 영화 검색하기
def inputMovieName(movieName):
    driver.find_element_by_id('ipt_tx_srch').send_keys(movieName)