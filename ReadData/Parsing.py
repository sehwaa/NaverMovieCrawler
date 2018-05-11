'''
Created on 2018. 5. 3.

@author: SEHWA
'''

#coding: utf-8

from Connection.Connection import driver
import selenium
from selenium.common.exceptions import NoSuchAttributeException,\
    NoSuchElementException
from Connection.Connection_DB import *

class Parsing:
    
    #생성자
    def __init__(self, movieName):
        self.movieName = movieName
        
    #[요약정보] 요약정보 파싱
    def summary(self):
        
        return_summary_list = []
        
        genre = None
        runningTime = None
        openingDate = None
        nation = None
        director = None
        grade = None
        accumulate_audience = None
        
        summary_text = driver.find_element_by_xpath("//dl[@class='info_spec']")
        #필요없는 데이터 제거(속도 저하 방지) 및 summary_text 전처리
        if summary_text.text.find("더보기") != -1 :
            summary_text_modify = summary_text.text.replace("\n더보기", "")
        else : 
            summary_list = summary_text.text.split('\n')
            
        if summary_text.text.find("누적관객누적관객 도움말") != -1 :
            summary_text_modify_2 = summary_text_modify.replace("\n누적관객누적관객 도움말", "") 
            summary_list = summary_text_modify_2.split('\n')
        else :
            summary_list = summary_text.text.split('\n')
        
        ###개요 정보
        ##전처리
        outline = summary_list[0]
        outline_modify = outline.replace(", ", ",")
        outline_modify_2 = outline_modify.replace(" .", ".")
        outline_modify_3 = outline_modify_2.replace(" 개봉", "개봉")
        outline_modify_4 = outline_modify_3.replace(" ,", ",")
        outline_list = outline_modify_4.split(' ')
        
        ##장르 / 국적 / 러닝타임 / 개봉날짜 구분
        for index in range(0, len(outline_list)):
            #장르 구분
            if outline_list[index].find("공포") != -1 :
                genre = outline_list[index]
                #print("장르 : " + genre)
                
            #러닝타임 구분
            elif outline_list[index].find("분") != -1 :
                runningTime = outline_list[index]
                #print("러닝타임 : " + runningTime.replace("분", ""))
                
            #개봉날짜 구분
            elif outline_list[index].find("개봉") != -1 :
                openingDate = outline_list[index]
                #print("개봉날짜 : " + openingDate.replace("개봉", ""))
                
            else :
                nation = outline_list[index]
                #print("국적 : " + nation)    
        
        #감독 구분
        director = summary_list[1]
        #print("감독 : " + director)
        
        #개요, 감독 정보 삭제(속도 저하 방지)
        del summary_list[0:1]
         
        ##등급 / 누적관객 수 구분
        for index in range(0, len(summary_list)):
            if summary_list[index].find("[국내]") != -1 or summary_list[index].find("[해외]") != -1 :
                grade = summary_list[index]
                #print("등급 : " + grade)
                
            elif summary_list[index].find("명") != -1 :
                accumulate_audience = summary_list[index]
                #print("누적관객 수 : " + accumulate_audience)

        return_summary_list.append(genre)
        return_summary_list.append(runningTime)
        return_summary_list.append(openingDate)
        return_summary_list.append(nation)
        return_summary_list.append(director)
        return_summary_list.append(grade)
        return_summary_list.append(accumulate_audience)
        
        return return_summary_list        
            
    #[배우/제작진] 제작사/수입사/배급사 파싱
    def agency(self):
        
        return_agency_list=[]
        
        producer = None
        importer = None
        distributor = None
        
        try:
            agency_name = driver.find_element_by_xpath("//dl[@class='agency_name']")
            agency_text = agency_name.text
            
            #제작사 / 수입사 / 배급사 정보 존재 유무 확인 (없으면 None)
            try:
                producer_text = driver.find_elements_by_class_name("agency_sub0")
                if producer_text == [] :
                    producer_text = None
            except NoSuchElementException:
                #print("제작사 없음")
                producer_text = None
            
            try:
                importer_text = driver.find_element_by_class_name("agency_sub1")
                if importer_text == []:
                    importer_text = None
            except NoSuchElementException:
                #print("수입사 없음")
                importer_text = None 
                
            try:
                distributor_text = driver.find_element_by_class_name("agency_sub2")
                if distributor_text == []:
                    distributor_text = None
            except NoSuchElementException:
                #print("배급사 없음")
                distributor_text = None
                
            #제작사 / 수입사 / 배급사 데이터 저장
            if producer_text is not None and importer_text is None and distributor_text is not None:
                producer = agency_text.split('\n')[0]
                distributor = agency_text.split('\n')[1]
                #print("제작사 : " + producer)
                #print("배급사: " + distributor)
            elif producer_text is not None and importer_text is not None and distributor_text is None:
                producer = agency_text.split('\n')[0]
                importer = agency_text.split('\n')[1]
                #print("제작사 : " + producer)
                #print("수입사 : " + importer)
            elif producer_text is None and importer_text is not None and distributor_text is not None:
                importer = agency_text.split('\n')[0]
                distributor = agency_text.split('\n')[1]
                #print("수입사 : " + importer)
                #print("배급사 : " + distributor)
            elif producer_text is not None and importer_text is not None and distributor_text is not None :
                producer = agency_text.split('\n')[0]
                importer = agency_text.split('\n')[1]
                distributor = agency_text.split('\n')[2]
                #print("제작사 : " + producer)
                #print("수입사 : " + importer)
                #print("배급사 : " + distributor)
            elif producer_text is not None and importer_text is None and distributor_text is None:
                producer = agency_text
                #print("제작사 : " + producer)
            elif producer_text is None and importer_text is not None and distributor_text is None:
                importer = agency_text
                #print("수입사 : " + importer)
            elif producer_text is None and importer_text is None and distributor_text is not None:
                distributor = agency_text
                #print("배급사 : " + distributor)
            else:
                print("정보 없음")
        except NoSuchElementException:
            print('정보 없음')
        
        return_agency_list.append(producer)
        return_agency_list.append(importer)
        return_agency_list.append(distributor)
        
        return return_agency_list
    
    #[평점] 개봉 전 평점 정보 파싱
    def beforeOpeningscore(self):
        return_before_score_list=[]
        try:
            #기대 지수
            expectateIndex = driver.find_element_by_class_name("exp_info")
            like = expectateIndex.text.split('\n')[0]
            dislike = expectateIndex.text.split('\n')[1]
            #print("보고싶어요 : " + like)
            #print("글쎄요 : " + dislike)
            return_before_score_list.append(like)
            return_before_score_list.append(dislike)
            
            #네티즌 평점
            star_score_text = driver.find_element_by_id("beforePointArea")
            star_score = star_score_text.text.split('\n')[3]
            before_participator = star_score_text.text.split('\n')[4]
            #print("개봉 전 네티즌 평점 : " + star_score)
            #print("참여자 수 : " + before_participator.replace("참여", ""))
            temp = before_participator.replace("참여 ","")
            return_before_score_list.append(star_score)
            return_before_score_list.append(temp.replace("명",""))
  
        except:
            #print("개봉 전 정보 없음")
            return_before_score_list.append("None")
            return_before_score_list.append("None")
            return_before_score_list.append("None")
            return_before_score_list.append("None")
        
        return return_before_score_list
            
    #[평점] 개봉 후 네티즌 평점 정보 파싱(총 평점, 점수 분포 정보)
    def afterNetizenOpeningscore(self):
        return_after_score_list=[]
        score=[]
        point=[]
        
        try:
            #네티즌 평점 정보 (총 평점 - 별점)
            netizen_score_all = driver.find_element_by_id("netizen_point_tab_inner")
            netizen_score = netizen_score_all.text.split('\n')[0]
            after_participator_netizen = netizen_score_all.text.split('\n')[1]
            
            #print("개봉 후 네티즌 평점 : " + netizen_score)
            #print("네티즌 평점 참여자 수 : " + after_participator_netizen)
            
            score.append(netizen_score)
            score.append(after_participator_netizen)
        except:
            #print("개봉 후 네티즌 평점 정보 없음")
            score.append("None")
                   
        try:
            #네티즌 점수 분포 (점수 분포 막대 그래프)
            netizen_score_graph_text = driver.find_element_by_id("netizen_point_graph")
            netizen_score_graph = netizen_score_graph_text.text.split("\n")
            
            print(netizen_score_graph)
            #점수 분포 리스트
            netizen_score_graph_list = []
            
            #index가 2로 안나누어 떨어지는 netizen_score_graph 요소만 netizen_score_graph_list에 삽입
            for index in range(0, len(netizen_score_graph)):
                if index % 2 != 0 :
                    netizen_score_graph_list.append(netizen_score_graph[index])
            
            #이 영화를 선호하는 연령대 텍스트 전처리
            if netizen_score_graph_list[-1].find("입니다") != -1 :
                netizen_score_favorite_group_text = netizen_score_graph_list[-1].replace("이 영화를 가장 좋아하는 그룹은 ", "")
                netizen_score_favorite_group = netizen_score_favorite_group_text.replace("입니다.", "")
                
                #리스트 마지막 요소 삭제(선호하는 연령대 데이터)
                del netizen_score_graph_list[-1]
            else :
                netizen_score_favorite_group = "None"
            
            #리스트 첫 번째 요소 삭제 (필요없는 데이터이므로 삭제)
            del netizen_score_graph_list[0]
            
            #점수 분포 텍스트 전처리 ('%' 삭제)
            for index in range(0, len(netizen_score_graph_list)):
                netizen_score_graph_list[index] = netizen_score_graph_list[index].replace("%", "")
            
            #print(netizen_score_graph_list)
            #print("선호하는 그룹(네티즌) : " +netizen_score_favorite_group)  
            
            point.append(netizen_score_graph_list)
            point.append(netizen_score_favorite_group)
        except:
            #print("네티즌 평점 막대 그래프 정보 없음")
            point.append("None")
            
        return_after_score_list.append(score)
        return_after_score_list.append(point)
        return return_after_score_list
    
    #[평점] 개봉 후 관람객 평점 정보 파싱 (총 평점, 점수 분포 정보)
    def afterAudienceOpeningScore(self):
        
        return_audience_score_list=[]
        score = []
        point = []
        
        try:
            #관람객 평점 정보 (총 평점 - 별점)
            audience_score_all = driver.find_element_by_id("actual_point_tab_inner")
            audience_score = audience_score_all.text.split('\n')[0]
            after_participator_audience = audience_score_all.text.split('\n')[1]
            
            #print("개봉 후 관람객 평점 : " + audience_score)
            #print("관람객 평점 참여자 수 : " + after_participator_audience)
            
            score.append(audience_score)
            score.append(after_participator_audience)
        except:
            #print("개봉 후 관람객 평점 정보 없음")
            score.append("None")
            
        try:
            #관람객 점수 분포 (점수 분포 막대 그래프)
            audience_score_graph_text = driver.find_element_by_id("actual_point_graph")
            audience_score_graph = audience_score_graph_text.text.split("\n")
            #점수 분포 리스트
            audience_score_graph_list = []
            
            #index가 2로 안나누어 떨어지는 netizen_score_graph 요소만 netizen_score_graph_list에 삽입
            for index in range(0, len(audience_score_graph)):
                if index % 2 != 0 :
                    audience_score_graph_list.append(audience_score_graph[index])
            
            #이 영화를 선호하는 연령대 텍스트 전처리
            if audience_score_graph_list[-1].find("입니다") != -1 :
                audience_score_favorite_group_text = audience_score_graph_list[-1].replace("이 영화를 가장 좋아하는 그룹은 ", "")
                audience_score_favorite_group = audience_score_favorite_group_text.replace("입니다.", "")    
            
                #리스트 마지막 요소 삭제(선호하는 연령대 데이터)
                del audience_score_graph_list[-1]
                
            else :
                audience_score_favorite_group = "None"           
            
            #리스트 첫 번째 요소 삭제 (필요없는 데이터이므로 삭제)
            del audience_score_graph_list[0]
            
            #점수 분포 텍스트 전처리 ('%' 제거)
            for index in range(0, len(audience_score_graph_list)):
                audience_score_graph_list[index] = audience_score_graph_list[index].replace("%", "")
            
            #print(audience_score_graph_list)
            #print("선호하는 그룹(관람객) : " + audience_score_favorite_group)  
            
            point.append(audience_score_graph_list)
            point.append(audience_score_favorite_group)
    
        except:
            #print("관람객 평점 막대 그래프 정보 없음")
            point.append("None")
            
        return_audience_score_list.append(score)
        return_audience_score_list.append(point)
        return return_audience_score_list
            
    #[평점] 개봉 후 네티즌 평점 정보 파싱(남녀별, 연령별)
    def afterNetizenOpeningscore_genderAndage(self):
        return_netizen_score_gender_age_list=[]
        gender_score=[]
        age_score=[]
        
        try:
            gender_score_text = driver.find_element_by_id("netizen_group_graph")
            gender_score_graph = gender_score_text.text.split('\n')
            
            del gender_score_graph[-1]
            
            #남녀 참여율 리스트
            gender_score_participation_rate = []
            #남녀 평점 리스트
            gender_score_star_score = []
            
            #연령별 참여율 리스트
            age_score_participation_rate = []
            #연령별 평점 리스트
            age_score_star_score = []   
                 
            ##파싱 정보 전처리
            
            #남/여 둘중에 참여율이 하나가 100%일 경우를 검사하는 메소드(인덱스가 2보다 작을 경우 둘 중 하나 100%)
            def return_participate_rate():
                for index in range(0, len(gender_score_graph)):
                    if gender_score_graph[index] == "참여율":
                        return index
                    
            #남/여 둘중에 참여율이 하나가 100%일 경우 성별을 알아내는 메소드
            def return_men_or_women_score_zero():
                for index in range(0, len(gender_score_graph)):
                    if gender_score_graph[index] == "평점 0.00":
                        return index + 1
                 
            #남/여 둘중에 참여율이 하나가 100%일 경우 연령별 평점 인덱스를 검사하는 메소드   
            def return_age():
                for index in range(0, len(gender_score_graph)):
                    if gender_score_graph[index] == "10대":
                        return index
                                        
            participate_rate_index = return_participate_rate()
            score_index = return_men_or_women_score_zero()
            
            #남녀 참여율 리스트 데이터 채우기
            if participate_rate_index < 2:
                if gender_score_graph[score_index] == "남자":
                    male_rate = "0"
                    female_rate = "100"
            
                    male_score = "0.00"
                    female_score = gender_score_graph[score_index+1].replace("평점 ","")
                
                elif gender_score_graph[score_index] == "여자":
                    female_rate = "0"
                    male_rate = "100"
                    
                    female_score = "0.00"
                    male_score = gender_score_graph[score_index-2].replace("평점 ","")
                    
                gender_score_participation_rate.append(male_rate) #남자 참여율
                gender_score_participation_rate.append(female_rate) #여자 참여율
                
                gender_score_star_score.append(male_score) #남자 평점
                gender_score_star_score.append(female_score) #여자 평점 

                #연령대 평점 임시 리스트
                age_score_star_score_temp = []
                
                age = return_age()
                for index in range(age, age+8):
                    if gender_score_graph[index].find("평점") != -1 :
                        age_score_star_score_temp.append(gender_score_graph[index].replace("평점 ", ""))
                        
                for index in range(0, len(age_score_star_score_temp)):
                    age_score_star_score.append(age_score_star_score_temp[index])
                #print(age_score_star_score)
                age_score.append(age_score_star_score)
                
                #참여율 개수 검사
                temp = 0
                
                for index in range(age+8, len(gender_score_graph)):
                    temp += 1
                    
                if temp == 1:
                    for index in range(age, age+8):
                        if gender_score_graph[index].find("평점 0.00") == -1 and gender_score_graph[index].find("대") == -1:
                            if index == age + 1:
                                age_score_participation_rate.append("100")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                            elif index == age + 3:
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("100")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                            elif index == age + 5:
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("100")
                                age_score_participation_rate.append("0")  
                            else:
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("100")  
                
                age_score.append(age_score_participation_rate)
            else :
                male_rate = gender_score_graph[0].replace("%", "") # '%' 제거
                female_rate = gender_score_graph[1].replace("%", "") # '%' 제거              
                
                male_score = gender_score_graph[3].replace("평점 ", "") #'평점' 제거
                female_score = gender_score_graph[5].replace("평점 ", "") #'평점' 제거
                
                gender_score_participation_rate.append(male_rate) #남자 참여율
                gender_score_participation_rate.append(female_rate) #여자 참여율
                                
                gender_score_star_score.append(male_score) #남자 평점
                gender_score_star_score.append(female_score) #여자 평점  
                
                #연령대 평점 임시 리스트
                age_score_star_score_temp = []
                
                #연령대 평점 리스트 데이터 채우기(10대, 20대, 30대, 40대 이상 순)
                for index in range(7, 15):
                    age_score_star_score_temp.append(gender_score_graph[index])
                #필요없는 데이터 제거
                for index in range(0, len(age_score_star_score_temp)):
                    if index % 2 != 0 :
                        age_score_star_score.append(age_score_star_score_temp[index].replace("평점 ", ""))#'평점' 제거          
            
                #print(age_score_star_score)
                age_score.append(age_score_star_score)
                
                #연령대 참여율 리스트 데이터 채우기(10대, 20대, 30대, 40대 이상 순)
                for index in range(15, 19):
                    age_score_participation_rate.append(gender_score_graph[index].replace("%", ""))#'%' 제거
                
                #print(age_score_participation_rate)
                age_score.append(age_score_participation_rate)                
            
#             print(male_rate)
#             print(female_rate)
#             print(male_score)
#             print(female_score)
#              
#             print(gender_score_participation_rate)
#             print(gender_score_star_score)
             
            gender_score.append(gender_score_participation_rate)
            gender_score.append(gender_score_star_score)
            
#            print(gender_score)
    
        except:
            #print("남녀별, 연령별 평점 정보 없음")
            gender_score.append("None")
            age_score.append("None")
            
        return_netizen_score_gender_age_list.append(gender_score)
        return_netizen_score_gender_age_list.append(age_score)
        
        return return_netizen_score_gender_age_list
            
    #[평점] 개봉 후 관람객 평점 정보 파싱(남녀별, 연령별)
    def afterAudienceOpeningscore_genderAndage(self):
        
        return_audience_score_gender_age_list=[]
        gender_score=[]
        age_score=[]
        
        try:
            gender_score_text = driver.find_element_by_id("actual_group_graph")
            gender_score_graph = gender_score_text.text.split('\n')
    
            #남녀 참여율 리스트
            gender_score_participation_rate = []
            #남녀 평점 리스트
            gender_score_star_score = []
            
            #연령별 참여율 리스트
            age_score_participation_rate = []
            #연령별 평점 리스트
            age_score_star_score = []
            
            ##파싱 정보 전처리
            #남/여 둘중에 참여율이 하나가 100%일 경우를 검사하는 메소드(인덱스가 2보다 작을 경우 둘 중 하나 100%)
            def return_participate_rate():
                for index in range(0, len(gender_score_graph)):
                    if gender_score_graph[index] == "참여율":
                        return index
                    
            #남/여 둘중에 참여율이 하나가 100%일 경우 성별을 알아내는 메소드
            def return_men_or_women_score_zero():
                for index in range(0, len(gender_score_graph)):
                    if gender_score_graph[index] == "평점 0.00":
                        return index + 1
                 
            #남/여 둘중에 참여율이 하나가 100%일 경우 연령별 평점 인덱스를 검사하는 메소드   
            def return_age():
                for index in range(0, len(gender_score_graph)):
                    if gender_score_graph[index] == "10대":
                        return index
                                        
            participate_rate_index = return_participate_rate()
            score_index = return_men_or_women_score_zero()
            
            #남녀 참여율 리스트 데이터 채우기
            if participate_rate_index < 2:
                if gender_score_graph[score_index] == "남자":
                    male_rate = "0"
                    female_rate = "100"
            
                    male_score = "0.00"
                    female_score = gender_score_graph[score_index+1].replace("평점 ","")
                
                elif gender_score_graph[score_index] == "여자":
                    female_rate = "0"
                    male_rate = "100"
                    
                    female_score = "0.00"
                    male_score = gender_score_graph[score_index-2].replace("평점 ","")
                    
                gender_score_participation_rate.append(male_rate) #남자 참여율
                gender_score_participation_rate.append(female_rate) #여자 참여율
                
                gender_score_star_score.append(male_score) #남자 평점
                gender_score_star_score.append(female_score) #여자 평점 

                #연령대 평점 임시 리스트
                age_score_star_score_temp = []
                
                age = return_age()
                for index in range(age, age+8):
                    if gender_score_graph[index].find("평점") != -1 :
                        age_score_star_score_temp.append(gender_score_graph[index].replace("평점 ", ""))
                        
                for index in range(0, len(age_score_star_score_temp)):
                    age_score_star_score.append(age_score_star_score_temp[index])
                #print(age_score_star_score)
                age_score.append(age_score_star_score)
                
                #참여율 개수 검사
                temp = 0
                
                for index in range(age+8, len(gender_score_graph)):
                    temp += 1
                    
                if temp == 1:
                    for index in range(age, age+8):
                        if gender_score_graph[index].find("평점 0.00") == -1 and gender_score_graph[index].find("대") == -1:
                            if index == age + 1:
                                age_score_participation_rate.append("100")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                            elif index == age + 3:
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("100")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                            elif index == age + 5:
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("100")
                                age_score_participation_rate.append("0")  
                            else:
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("0")
                                age_score_participation_rate.append("100")  
                
                age_score.append(age_score_participation_rate)
            else :
                male_rate = gender_score_graph[0].replace("%", "") # '%' 제거
                female_rate = gender_score_graph[1].replace("%", "") # '%' 제거              
                
                male_score = gender_score_graph[3].replace("평점 ", "") #'평점' 제거
                female_score = gender_score_graph[5].replace("평점 ", "") #'평점' 제거
                
                gender_score_participation_rate.append(male_rate) #남자 참여율
                gender_score_participation_rate.append(female_rate) #여자 참여율
                                
                gender_score_star_score.append(male_score) #남자 평점
                gender_score_star_score.append(female_score) #여자 평점  
                
                #연령대 평점 임시 리스트
                age_score_star_score_temp = []
                
                #연령대 평점 리스트 데이터 채우기(10대, 20대, 30대, 40대 이상 순)
                for index in range(7, 15):
                    age_score_star_score_temp.append(gender_score_graph[index])
                #필요없는 데이터 제거
                for index in range(0, len(age_score_star_score_temp)):
                    if index % 2 != 0 :
                        age_score_star_score.append(age_score_star_score_temp[index].replace("평점 ", ""))#'평점' 제거          
            
                #print(age_score_star_score)
                age_score.append(age_score_star_score)
                
                #연령대 참여율 리스트 데이터 채우기(10대, 20대, 30대, 40대 이상 순)
                for index in range(15, 19):
                    age_score_participation_rate.append(gender_score_graph[index].replace("%", ""))#'%' 제거
                
                #print(age_score_participation_rate)
                age_score.append(age_score_participation_rate)                
            
            #print(male_rate)
            #print(female_rate)
            #print(male_score)
            #print(female_score)
              
            #print(gender_score_participation_rate)
            #print(gender_score_star_score)
             
            gender_score.append(gender_score_participation_rate)
            gender_score.append(gender_score_star_score)
            
            #print(gender_score)
    
        except:
            #print("남녀별, 연령별 평점 정보 없음")
            gender_score.append("None")
            age_score.append("None")
        
        return_audience_score_gender_age_list.append(gender_score)
        return_audience_score_gender_age_list.append(age_score)
        
        return return_audience_score_gender_age_list