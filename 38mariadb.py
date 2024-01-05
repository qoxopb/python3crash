#마리아디비로 데이터 다루기 1 - select
# pymysql 모듈을 먼저 설치해야 함 - pip install pymysql

import pymysql


# 데이터베이스 서버 접속정보 정의
url = ''   #프로퍼티 -호스트 주소
userid = ''
passwd = ''
dbname = ''


# 디비 서버에 연결
conn = pymysql.connect(host=url, user=userid, password=passwd,
                       database=dbname, charset='utf8')

cursor = conn.cursor()

sql = ' select * from member '
cursor.execute(sql)

rows = cursor.fetchall()     # sql 실행 결과를 결과집합* 으로 모두 가져옴

cursor.close()
conn.close()

result = ''
for row in rows:
    result += f'{row[0]} {row[1]} {row[2]} {row[3]} \n} '

print(result)











