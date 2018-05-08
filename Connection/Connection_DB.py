'''
Created on 2018. 5. 3.

@author: SEHWA
'''
#coding: utf-8

import pymysql

class Connection_DB_Read:
    
    #DB에서 데이터 읽기(영화 제목)
    def read_Data(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'SELECT movie_name FROM movie_list'
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
            
class Connection_DB_Insert:
    
    movieName = ""
    
    #생성자
    def __init__(self, movieName):
        self.movieName = movieName  
        
    #DB에 데이터 삽입하기 (장르)
    def insert_Data_genre(self,genre):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET movie_genre ="'+genre+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
            
    #DB에 데이터 삽입하기 (국적)
    def insert_Data_nation(self,nation):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET movie_nation="'+nation+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (러닝 타임)
    def insert_Data_runningTime(self, runningTime):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET movie_runningTime="'+runningTime+'"'+'WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉날짜)
    def insert_Data_opening_date(self,openingDate):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET movie_opening_date="'+openingDate+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)    
        finally:
            conn.close()
            
    #DB에 데이터 삽입하기 (감독)
    def insert_Data_director(self,director):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET movie_director="'+director+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
            
    #DB에 데이터 삽입하기 (등급)
    def insert_Data_grade(self,grade):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET movie_grade="'+grade+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (누적관객 수)
    def insert_Data_audience(self,audience):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET movie_audience="'+audience+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (제작사)
    def insert_Data_producer(self,producer):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET movie_producer="'+producer+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (수입사)
    def insert_Data_importer(self,importer):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET movie_importer="'+importer+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (배급사)
    def insert_Data_distributor(self,distributor):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET movie_distributor="'+distributor+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (기대지수 - 보고싶어요)
    def insert_Data_like(self,like):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET before_like="'+like+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (기대지수 - 글쎄요)
    def insert_Data_dislike(self,dislike):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET before_dislike="'+dislike+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 전 - 네티즌 평점)
    def insert_Data_before_netizen_score(self,score):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET before_netizen_score="'+score+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 전 - 네티즌 평점 참여자수)
    def insert_Data_before_netizen_participate(self,participate):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET before_netizen_participate="'+participate+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 네티즌 평점)
    def insert_Data_after_netizen_score(self,score):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET after_netizen_score="'+score+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 네티즌 평점 참여자 수)
    def insert_Data_after_netizen_participate(self,participate):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET after_netizen_participate="'+participate+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 네티즌 평점 전체 분포)
    def insert_Data_after_netizen_distribution(self,distribution):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                for index in range(0, len(distribution)):
                    point = index + 1
                    sql = 'UPDATE movie_list SET after_netizen_distribution_'+str(point)+'="'+distribution[index]+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                    cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 네티즌 선호하는 그룹)
    def insert_Data_after_netizen_favorite_group(self,favorite):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET after_netizen_favorite_group="'+favorite+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 네티즌 남/여 참여율)
    def insert_Data_after_netizen_gender_participate_rate(self,participate):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                for index in range(0, len(participate)):
                    sql = 'UPDATE movie_list SET after_netizen_gender_participate_'+str(index)+'="'+participate[index]+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                    cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 네티즌 남/여 평점)
    def insert_Data_after_netizen_gender_score(self,score):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                for index in range(0, len(score)):
                    sql = 'UPDATE movie_list SET after_netizen_gender_score_'+str(index)+'="'+score[index]+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                    cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 네티즌 연령별 평점)
    def insert_Data_after_netizen_age_score(self, score):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                for index in range(0, len(score)):
                    age = (index + 1)*10
                    sql = 'UPDATE movie_list SET after_netizen_age_score_'+str(age)+'="'+score[index]+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                    cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 네티즌 연령별 참여율)
    def insert_Data_after_netizen_age_participate(self, participate):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                for index in range(0, len(participate)):
                    age = (index + 1) * 10
                    sql = 'UPDATE movie_list SET after_netizen_age_participate_'+str(age)+'="'+participate[index]+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                    cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)   
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 관람객 평점)
    def insert_Data_after_audience_score(self, score):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET after_audience_score="'+score+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 관람객 평점 참여자 수)
    def insert_Data_after_audience_participate(self, participate):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET after_audience_participate="'+participate+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 관람객 평점 전체 분포)
    def insert_Data_after_audience_distribution(self, distribution):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                for index in range(0, len(distribution)):
                    point = index + 1
                    sql = 'UPDATE movie_list SET after_audience_distribution_'+str(point)+'="'+distribution[index]+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                    cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)  
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 관람객 선호하는 그룹)
    def insert_Data_after_audience_favorite_group(self, favorite):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                sql = 'UPDATE movie_list SET after_audience_favorite_group="'+favorite+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 관람객 남/여 참여율)
    def insert_Data_after_audience_gender_participate(self, score):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                for index in range(0, len(score)):
                    sql = 'UPDATE movie_list SET after_audience_gender_participate_'+str(index)+'="'+score[index]+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                    cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 관람객 남/여 평점)
    def insert_Data_after_audience_gender_score(self, score):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                for index in range(0, len(score)):
                    sql = 'UPDATE movie_list SET after_audience_gender_score_'+str(index)+'="'+score[index]+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                    cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 관람객 연령별 평점)
    def insert_Data_after_audience_age_score(self, score):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                for index in range(0, len(score)):
                    age = (index + 1)*10
                    sql = 'UPDATE movie_list SET after_audience_age_score_'+str(age)+'="'+score[index]+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                    cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
                    
    #DB에 데이터 삽입하기 (개봉 후 - 관람객 연령별 참여율)
    def insert_Data_after_audience_age_participate(self, participate):
        try:
            conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')
            with conn.cursor() as cursor:
                for index in range(0, len(participate)):
                    age = (index+1) * 10
                    print(index)
                    print(participate[index])
                    sql = 'UPDATE movie_list SET after_audience_age_participate_'+str(age)+'="'+participate[index]+'"'+' WHERE movie_name="' +self.movieName + '\n"'
                    cursor.execute(sql)
            conn.commit()
        except Exception as ex:
            print(ex)  
        finally:
            conn.close() 