'''
Created on 2018. 5. 3.

@author: SEHWA
'''
#coding: utf-8

import pymysql

conn = pymysql.connect(host='localhost', user='root', port=3306, db='movie', charset='utf8')

#DB에서 데이터 읽기(영화 제목)
def read_Data():
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT movie_name FROM movie_list'
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            return result
    finally:
        conn.close()