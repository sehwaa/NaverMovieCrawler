'''
Created on 2018. 5. 7.

@author: SEHWA
'''
#coding: utf-8

from Controller.Click import *
from Controller.Input import *
from ReadData.Parsing import *

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
    after_netizen_distribution = None
    after_netizen_favorite = None
    after_netizen_gender_participate = None
    after_netizen_gender_score = None
    after_netizen_age_score = None
    after_netizen_age_participate = None
    after_audience_star_score = None
    after_audience_participate= None
    after_audience_distribution = None
    after_audience_favorite = None
    after_audience_gender_participate = None
    after_audience_gender_score = None
    after_audience_age_score = None
    after_audience_age_participate = None
    
    #실행 및 DB에 삽입
    def executeModule(self, movie_name):
        
        #파싱 객체
        parse = Parsing(movie_name)
        #DB 연결 객체 (삽입)
        connDB = Connection_DB_Insert(movie_name)
        
        inputMovieName(movie_name)
        
        try:
            
            autoCompletementList(movie_name)
            
            #요약정보
            summary = parse.summary()
            #print(summary)
            
            #요약정보 데이터 저장
            self.genre = summary[0]
            self.runningTime = summary[1]
            self.openingDate = summary[2]
            self.nation = summary[3]
            self.director = summary[4]
            self.grade = summary[5]
            self.audience = summary[6]
            
            print("----------------------------------------------")
            print("장르 : " + str(self.genre))
            print("러닝타임 : " + str(self.runningTime))
            print("개봉일 : " + str(self.openingDate))
            print("국적 : " + str(self.nation))
            print("감독 : " + str(self.director))
            print("등급 : " + str(self.grade))
            print("누적 관객 수 : " + str(self.audience))
            print("----------------------------------------------")
            
            #데이터베이스 저장
            connDB.insert_Data_genre(self.genre)
            connDB.insert_Data_runningTime(self.runningTime)
            connDB.insert_Data_opening_date(self.openingDate)
            connDB.insert_Data_nation(self.nation)
            connDB.insert_Data_director(self.director)
            connDB.insert_Data_grade(self.grade)
            connDB.insert_Data_audience(self.audience)
            
            actorTab()
            
            #제작사 / 수입사 / 배급사 정보
            companys = parse.agency()
            #print(companys)
            
            #제작사 / 수입사 / 배급사 정보 데이터 저장
            self.producer = companys[0]
            self.importer = companys[1]
            self.distributor = companys[2]
            
            print("----------------------------------------------")
            print("제작사 : " + str(self.producer))
            print("수입사 : " + str(self.importer))
            print("배급사 : " + str(self.distributor))
            print("----------------------------------------------")
            
            #데이터베이스 저장
            connDB.insert_Data_producer(self.producer)
            connDB.insert_Data_importer(self.importer)
            connDB.insert_Data_distributor(self.distributor)
            
            scoreTab()
            beforeOpening()
            
            #개봉 전 평점
            before_score = parse.beforeOpeningscore()
            #print(before_score)
            
            #개봉 전 평점 정보 저장
            self.like = before_score[0]
            self.dislike = before_score[1]
            self.before_netizen_score = before_score[2]
            self.before_netizen_participate = before_score[3]
            
            print("----------------------------------------------")
            print("보고싶어요 : " + str(self.like))
            print("글쎄요 : " + str(self.dislike))
            print("개봉 전 평점 : " + str(self.before_netizen_score))
            print("개봉 전 참여자 수 : " + str(self.before_netizen_participate))
            print("----------------------------------------------")
            
            #데이터베이스 저장
            connDB.insert_Data_like(self.like)
            connDB.insert_Data_dislike(self.dislike)
            connDB.insert_Data_before_netizen_score(self.before_netizen_score)
            connDB.insert_Data_before_netizen_participate(self.before_netizen_participate)
            
            try:
                afterOpening()
                #개봉 후 네티즌 평점
                after_score_netizen = parse.afterNetizenOpeningscore()
                #print(after_score_netizen)
                
                #개봉 후 네티즌 평점 정보 저장
                self.after_netizen_star_score = after_score_netizen[0][0] #개봉 후 총 평점
                self.after_netizen_participate = after_score_netizen[0][1] #참여자 수
                self.after_netizen_distribution = after_score_netizen[1][0] #점수분포
                self.after_netizen_favorite = after_score_netizen[1][1] #선호하는 그룹
                
                print("----------------------------------------------")
                print("개봉 후 네티즌 총 평점 : " + str(self.after_netizen_star_score))
                print("개봉 후 네티즌 참여자 수 : " + str(self.after_netizen_participate))
                print("점수분포 : " + str(self.after_netizen_distribution))
                print("선호하는 그룹 : " +str(self.after_netizen_favorite))
                print("----------------------------------------------")
                
                #데이터베이스 저장
                connDB.insert_Data_after_netizen_score(self.after_netizen_star_score)
                connDB.insert_Data_after_netizen_participate(self.after_netizen_participate)
                connDB.insert_Data_after_netizen_distribution(self.after_netizen_distribution)
                connDB.insert_Data_after_netizen_favorite_group(self.after_netizen_favorite)
                        
                try:
                    netizenGenderAndAge()
                    #네티즌 - 남녀별 / 연령대별 평점
                    after_score_netizen_genderAndage = parse.afterNetizenOpeningscore_genderAndage()
                    #print(after_score_netizen_genderAndage)
                    
                    #네티즌 남녀별 / 연령대별 평점 정보 저장
                    self.after_netizen_gender_participate = after_score_netizen_genderAndage[0][0]
                    self.after_netizen_gender_score = after_score_netizen_genderAndage[0][1]
                    self.after_netizen_age_score = after_score_netizen_genderAndage[1][0]
                    self.after_netizen_age_participate = after_score_netizen_genderAndage[1][1]
                    
                    print("----------------------------------------------")
                    print("네티즌 남/녀 참여율 : " + str(self.after_netizen_gender_participate))
                    print("네티즌 남/녀 평점 : " + str(self.after_netizen_gender_score))
                    print("연령별 참여율 : " + str(self.after_netizen_age_participate))
                    print("연령별 평점 : " + str(self.after_netizen_age_score))
                    print("----------------------------------------------")
                    
                    #데이터베이스 저장
                    connDB.insert_Data_after_netizen_gender_participate_rate(self.after_netizen_gender_participate)
                    connDB.insert_Data_after_netizen_gender_score(self.after_netizen_gender_score)
                    connDB.insert_Data_after_netizen_age_participate(self.after_netizen_age_participate)
                    connDB.insert_Data_after_netizen_age_score(self.after_netizen_age_score)
                    
                    try:
                        audienceScore()
                        #개봉 후 관람객 평점
                        after_score_audience = parse.afterAudienceOpeningScore()
                        #print(after_score_audience)
                        
                        #개봉 후 관람객 평점 정보 데이터 저장
                        self.after_audience_star_score = after_score_audience[0][0]
                        self.after_audience_participate = after_score_audience[0][1]
                        self.after_audience_distribution = after_score_audience[1][0]
                        self.after_audience_favorite = after_score_audience[1][1]

                        print("----------------------------------------------")
                        print("관람객 개봉 후 총 평점 : " + str(self.after_audience_star_score))
                        print("관람객 개봉 후 참여자 수 : " + str(self.after_audience_participate))
                        print("점수분포 : " + str(self.after_audience_distribution))
                        print("선호하는 그룹 : " + str(self.after_audience_favorite))
                        print("----------------------------------------------")
                        
                        #데이터베이스 저장
                        connDB.insert_Data_after_audience_score(self.after_audience_star_score)
                        connDB.insert_Data_after_audience_participate(self.after_audience_participate)
                        connDB.insert_Data_after_audience_distribution(self.after_audience_distribution)
                        connDB.insert_Data_after_audience_favorite_group(self.after_audience_favorite)
                        
                        audienceGenderAndAge()
                        #관람객 - 남녀별 / 연령대별 평점
                        after_score_audience_genderAndage = parse.afterAudienceOpeningscore_genderAndage()
                        #print(after_score_audience_genderAndage)
                        
                        #관람객 남녀별 / 연령대별 평점 정보 저장
                        self.after_audience_gender_participate = after_score_audience_genderAndage[0][0]
                        self.after_audience_gender_score = after_score_audience_genderAndage[0][1]
                        self.after_audience_age_score = after_score_audience_genderAndage[1][0]
                        self.after_audience_age_participate = after_score_audience_genderAndage[1][1]
                        
                        print("----------------------------------------------")
                        print("관람객 남녀 참여율 : " + str(self.after_audience_gender_participate))
                        print("관람객 남녀 평점 : " + str(self.after_audience_gender_score))
                        print("연령별 참여율: " + str(self.after_audience_age_participate))
                        print("연령별 평점 : " + str(self.after_audience_age_score))
                        print("----------------------------------------------")
                        
                        #데이터베이스 저장
                        connDB.insert_Data_after_audience_gender_participate(self.after_audience_gender_participate)
                        connDB.insert_Data_after_audience_gender_score(self.after_audience_gender_score)  
                        connDB.insert_Data_after_audience_age_participate(self.after_audience_age_participate)
                        connDB.insert_Data_after_audience_age_score(self.after_audience_age_score)                     
                        
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