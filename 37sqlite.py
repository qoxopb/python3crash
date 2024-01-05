# 파이썬으로 sqlite 다루기 2 - insert
# 입력한 회원정보를 member 테이블에 저장

import sqlite3

# 회원정보 입력받기
userid = input('아이디: ')
passwd = input('비밀번호: ')
name = input('이름: ')
email = input('이메일: ')

#db 연결 객체 생성
conn = sqlite3.connect('db/bigdata.db')
curser = conn.cursor()

#sql 작성  - 아래방식은 비추 - SQL injection 공격 위험
# sql = (' insert into member values (' +userid+ ' , ' +passwd+ ', ' +name+ ', ' +email+ '') ')

# sql = ' insert into member values '\
#       f" ('{userid}','{passwd}','{name}','{email}') "

# 매개변수 placeholder(?) 를 이용해 실제 값 지정
sql = ' insert into member values (?, ?, ?, ?) '
params = (userid, passwd, name, email)     #튜플로 값 지정

# placeholder, params 를 이용해 sql 실행
curser.execute(sql, params)
conn.commit() # 테이블에 값을 저장하기 위해 반드시 commit 호출
print(curser.rowcount, '행이 추가됨.')

curser.close()
conn.close()


# 파이썬으로 sqlite 다루기 3 - update
# 수정할 회원정보 입력받기
userid = input('수정할 아이디: ')
passwd = input('수정할 비밀번호: ')
name = input('수정할 이름: ')
email = input('수정할 이메일: ')

conn = sqlite3.connect('db/bigdata.db')
curser = conn.cursor()

# 매개변수 named parameter placeholder (:이름)를 이용해 실제 값 지정
sql = ' update member set passwd = :pwd ,name = :name, email = :email '\
      ' where userid = :uid '
# named parameter palceholder 사용하는 경우
# 실제값은 dict형으로 정의해야 함
params = {'uid': userid, 'pwd': passwd, 'name': name, 'email': email}

# placeholder, params 를 이용해 sql 실행
curser.execute(sql, params)
conn.commit()        # 테이블의 값 수정시에도 commit 호출 필수.
print(curser.rowcount, '행이 수정됨.')

curser.close()
conn.close()



# 파이썬으로 sqlite 다루기 4 - delete
userid = input('삭제할 아이디: ')

conn = sqlite3.connect('db/bigdata.db')
curser = conn.cursor()

sql = ' delete from member where userid = ? '
params = (userid, )

curser.execute(sql, params)
conn.commit()
print(curser.rowcount, '행이 삭제됨.')

curser.close()
conn.close()


