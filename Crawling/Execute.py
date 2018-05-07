'''
Created on 2018. 5. 7.

@author: SEHWA
'''
#coding: utf-8

from Controller.Click import *
from Controller.Input import *
from ReadData.Parsing import *
from Connection.Connection_DB import *

class Execute:
    
    genre = None
    runningTime = None
    openingDate = None
    nation = None
    director = None
    grade = None
    audience = None
    producer = None
    importer = None
    distributor = None
    like = None
    dislike = None
    before_netizen_score = None
    before_netizen_participate = None
    after_netizen_star_score = None
    after_netizen_participate = None
    after_netizen_distribution_1 = None
    after_netizen_distribution_2 = None
    after_netizen_distribution_3 = None
    after_netizen_distribution_4 = None
    after_netizen_distribution_5 = None
    after_netizen_distribution_6 = None
    after_netizen_distribution_7 = None
    after_netizen_distribution_8 = None
    after_netizen_distribution_9 = None
    after_netizen_distribution_10 = None
    after_netizen_favorite = None
    after_netizen_gender_participate_male = None
    after_netizen_gender_participate_female = None
    after_netizen_gender_score_male = None
    after_netizen_gender_score_female = None
    after_netizen_age_score_10 = None
    after_netizen_age_score_20 = None
    after_netizen_age_score_30 = None
    after_netizen_age_score_40 = None
    after_netizen_age_participate_10 = None
    after_netizen_age_participate_20 = None
    after_netizen_age_participate_30 = None
    after_netizen_age_participate_40 = None
    after_audience_star_score = None
    after_audience_participate= None
    after_audience_distribution_1 = None
    after_audience_distribution_2 = None
    after_audience_distribution_3 = None
    after_audience_distribution_4 = None
    after_audience_distribution_5 = None
    after_audience_distribution_6 = None
    after_audience_distribution_7 = None
    after_audience_distribution_8 = None
    after_audience_distribution_9 = None
    after_audience_distribution_10 = None
    after_audience_favorite = None
    after_audience_gender_participate_male = None
    after_audience_gender_participate_female = None
    after_audience_gender_score_male = None
    after_audience_gender_score_female = None
    after_audience_age_score_10 = None
    after_audience_age_score_20 = None
    after_audience_age_score_30 = None
    after_audience_age_score_40 = None
    after_audience_age_participate_10 = None
    after_audience_age_participate_20 = None
    after_audience_age_participate_30 = None
    after_audience_age_participate_40 = None
    
    #실행 및 DB 삽입
    def executeModule(self, movie_name):
        
        #파싱 객체
        parse = Parsing(movie_name)
        
        #데이터 베이스 연결 객체(삽입)
        connDBInsert = Connection_DB_Insert(movie_name)
        
        inputMovieName(movie_name)
        
        try:
            
            autoCompletementList(movie_name)
            
            #요약정보
            summary = parse.summary()
            print(summary)
            
            actorTab()
            
            #제작사 / 수입사 / 배급사 정보
            companys = parse.agency()
            print(companys)
            
            scoreTab()
            beforeOpening()
            
            #개봉 전 평점
            before_score = parse.beforeOpeningscore()
            print(before_score)
            
            try:
                afterOpening()
                #개봉 후 네티즌 평점
                after_score_netizen = parse.afterNetizenOpeningscore()
                print(after_score_netizen)
                        
                try:
                    netizenGenderAndAge()
                    #네티즌 - 남녀별 / 연령대별 평점
                    after_score_netizen_genderAndage = parse.afterNetizenOpeningscore_genderAndage()
                    print(after_score_netizen_genderAndage)
                    try:
                        audienceScore()
                        #개봉 후 관람객 평점
                        after_score_audience = parse.afterAudienceOpeningScore()
                        print(after_score_audience)
                        audienceGenderAndAge()
                        #관람객 - 남녀별 / 연령대별 평점
                        after_score_audience_genderAndage = parse.afterAudienceOpeningscore_genderAndage()
                        print(after_score_audience_genderAndage)
                    except Exception as ex:
                        clear()
                        print(ex)
                        pass
                except Exception as ex:
                    clear()
                    print(ex)
                    pass
            except Exception as ex:
                clear()
                print(ex)
                pass
        except Exception as ex:
            clear()
            print(ex)
            pass