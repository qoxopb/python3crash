# 오라클디비로 데이터 다루기 1 - select
# cx_Oracle 모듈을 먼저 설치해야 함 - pip install cx_Oracle

# 1) Oracle instant client 버전에 따라 VS 재배포 패키지 설치
# 2) Oracle instant client를 다운로드 하고 C:/java에 압축해제
# 3) Oracle instant client를 시스템의 PATH환경변수에 등록
# 4) IntelliJ 다시 시작

# For Instant Client 21 install VS 2019 or later.
# For Instant Client 19 install VS 2017.
# https://oracle.com/kr/database/technologies/instant-client/winx64-64-downloads.html

# inteliJ에서 csv 파일 가져오기 시 (오라클)
# 텍스트 컬럼은 자동으로  CLOB 타입으로 설정
# CLOB가 꼭 필요한 컬럼 외 나머지는 VARCHAR타입으로 변경해 사용


import cx_Oracle

host = ''
userid = ''
passwd = ''
sid = ''

# 디비 서버에 연결
dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)

cursor = conn.cursor()

sql = 'select first_name, last_name from employees_2'
cursor.execute(sql)

for fname, lname in cursor:
    print(fname, lname)

cursor.close()
conn.close()




# 국가별 메달별 획득수 조회
dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)
cursor = conn.cursor()
# CLOB 컬럼을 select에 사용 시 to_char 함수 필요 (성능저하유발)
# 전체타입 VARCHAR 로 변경해야함
sql = ' select Country, Medal, count(Country) Cnt '\
        ' from SUMMERMEDALS2 group by Country, Medal '\
        ' order by Cnt desc '
cursor.execute(sql)

for Country, Medal, Cnt in cursor:
    print(Country, Medal, Cnt)

cursor.close()
conn.close()


# 사원이름, 성, 직책, 연봉, 부서명 조회


# 승선위치별(embarked) 성별(sex) 생존자 (survived) 수 조회
dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)
cursor = conn.cursor()

sql = ' select EMBARK_TOWN, SEX, count(ALIVE) alives from TITANIC2 '\
      " where ALIVE = 'yes' group by EMBARK_TOWN, SEX "\
      ' order by EMBARK_TOWN, SEX '
cursor.execute(sql)

for embark, sex, alives in cursor:
    print(embark, sex, alives)


cursor.close()
conn.close()


# 승선위치별(embarked) 성별+연령별(who) 생존자 (survived) 수 조회
dsn_tns = cx_Oracle.makedsn(host, 1521, sid)
conn = cx_Oracle.connect(userid, passwd, dsn_tns)
cursor = conn.cursor()

sql = ' select EMBARK_TOWN, WHO, count(WHO) alives from TITANIC2 '\
      ' group by EMBARK_TOWN, WHO order by EMBARK_TOWN, WHO '
cursor.execute(sql)

for embark, who, alives in cursor:
    print(embark, who, alives)


cursor.close()
conn.close()

cursor.close()
conn.close()








