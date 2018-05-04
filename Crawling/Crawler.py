'''
Created on 2018. 5. 4.

@author: SEHWA
'''

#coding: utf-8

from Controller.Click import *
from Controller.Input import *
from ReadData.Parsing import *
from Connection.Connection_DB import read_Data

def executeModule(movie_name):
    inputMovieName(movie_name)
    autoCompletementList(movie_name)
    summary()
    actorTab()
    agency()
    scoreTab()
    beforeOpening()
    beforeOpeningscore()
    afterOpening()
    afterNetizenOpeningscore()
    netizenGenderAndAge()
    afterNetizenOpeningscore_genderAndage()
    audienceScore()
    afterAudienceOpeningScore()
    audienceGenderAndAge()
    afterAudienceOpeningscore_genderAndage()
        
if __name__ == "__main__" :

    #DB에서 영화리스트 읽어옴
    movie_list_response = read_Data()
    #프로그램에서 사용할 영화 리스트
    movie_list = []
    
    #튜플형에서 리스트형으로 바꿔줌
    for index in range(0, len(movie_list_response)):
        movie_name_text = str(movie_list_response[index]).replace("('","")
        movie_name = movie_name_text.replace("',)","")
        movie_list.append(movie_name)
    
    for index in range(0, len(movie_list)):
        executeModule(movie_list[index])