'''
Created on 2018. 5. 4.

@author: SEHWA
'''

#coding: utf-8

from Controller.Click import *
from Controller.Input import *
from ReadData.Parsing import *
from Connection.Connection_DB import *
from Crawling.Execute import *
        
if __name__ == "__main__" :
    
    #데이터베이스 연동 객체 (영화 목록 읽어 오기)
    connDBRead = Connection_DB_Read()
     
    #DB에서 영화리스트 읽어옴
    movie_list_response = connDBRead.read_Data()
    #프로그램에서 사용할 영화 리스트
    movie_list = []
     
    #튜플형에서 리스트형으로 바꿔줌
    for index in range(0, len(movie_list_response)):
        movie_name_text = str(movie_list_response[index]).replace("('","")
        movie_name = movie_name_text.replace("',)","")
        movie_list.append(movie_name.replace("\\n", ""))
       
    for index in range(0, len(movie_list)):
        execute_module = Execute()
        execute_module.executeModule(movie_list[index])