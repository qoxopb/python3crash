import sys
import oracledb

# 데이터베이스 연결정보

host = '3.35.54.151'
userid = 'bigdata'
passwd = 'bigdata'    #bigdata2023
sid = 'FREE'

dsn_tns = oracledb.makedsn(host, 1521, sid)

# sql = ' CREATE TABLE sungjuk ( '\
#     ' sjno   INT GENERATED AS IDENTITY, ' \
#     ' name   VARCHAR(10) not null, ' \
#     '  kor    INT  not null, ' \
#     '  eng    INT  not null, ' \
#     '  mat    INT  not null, ' \
#     '   tot    INT default 0, ' \
#     '   avg    decimal(5,1) default 0.0, ' \
#     '   grd    CHAR(3) default '가', ' \
#     '   regdate DATE DEFAULT sysdate '\
#     ' ) ' \
#     ' alter table sungjuk ' \
#     ' add constraint sj_pk primary key (sjno) '
#
# conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
# cursor = conn.cursor()
# cursor.execute(sql, sj)
# conn.commit()
# print(cursor.rowcount, '건의 성적데이터 추가됨.')
#
# cursor.close()
# conn.close()



# 메뉴 출력
def show_menu():
    """
    메뉴 선택 출력 함수
    :return: 입력받은 메뉴번호
    """
    main_menu = '''
    -----------------------
    성적처리프로그램 v7
    -----------------------
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    -----------------------
    '''
    print(main_menu, end='')
    menu = input('=>메뉴를 선택하세요: ')
    return menu

#성적데이터 입력받음
def read_sungjuk():
    """
    성적 입력받는 함수
    :return: 입력된 성적
    """
    sungjuk = input('이름과 성적을 입력하세요 (예: 홍길동 99 98 99) :')
    data = sungjuk.split()                 #구분자 공백일때는 () 사용가능

    name = data[0]
    kor = int(data[1])
    eng = int(data[2])
    mat = int(data[3])
    sj = [name, kor, eng, mat]      #입력받은 성적데이터를 리스트에 담음

    return sj


# 성적 처리(총점, 평균, 학점 계산)
def compute_sungjuk(sj):
    """
    총점평균등급 산출 함수
    :param sj: 입력된 성적데이터
    :return: 성적처리된 성적데이터(총점평균등급)
    """
    tot = sj[1] + sj[2] + sj[3]
    avg = float(f"{tot / 3:.1f}")
    grd = '수' if avg >= 90 else \
          '우' if avg >= 80 else \
          '미' if avg >= 70 else \
          '양' if avg >= 60 else '가'
    return [sj[0], sj[1], sj[2], sj[3], tot, avg, grd]


# 모든 성적 데이터 출력(번호/이름/국/영/수/등록일)
def show_sungjuk():
    """
    성적조회 - 모든 성적 데이터 출력(번호/이름/국/영/수/등록일)
    :return: 없음
    """
    print('성적데이터 조회')
    sql = ' select sjno, name, kor, eng, mat, regdate from sungjuk '\
         ' order by sjno desc '

    conn = oracledb.connect(
        user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(sql)

    for sjno, name, kor, eng, mat, regdate in cursor:
        print(sjno, name, kor, eng, mat, str(regdate)[:10])


    cursor.close()
    conn.close()



# 성적 데이터 저장(sungjuk 테이블)
def save_sungjuk(sj):
    """
    성적 데이터 저장(sungjuk 테이블)
    :param sj: 입력받아 처리된 성적데이터(총점평균등급)
    :return: 없음
    """
    sql =' insert into sungjuk (name, kor, eng, mat, tot, avg, grd) '\
        ' values (:1,:2,:3,:4, :5,:6,:7) '
        # ' values (:name,:kor,:eng,:mat, :tot,:avg,:grd) '
        # ' values (?,?,?,?, ?,?,?) ' # 오라클 x

    conn = oracledb.connect(
        user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(sql, sj)
    conn.commit()
    print(cursor.rowcount, '건의 성적데이터 추가됨.')

    cursor.close()
    conn.close()



# 성적 데이터 추가 (입력-처리-저장)
def addsungjuk():
    """
    새로운 성적 데이터 추가, sunguks.json에 저장
    :return: 없음
    """
    print('성적데이터 추가')
    sj = read_sungjuk()
    sj = compute_sungjuk(sj)
    save_sungjuk(sj)                #성적데이터를 파일에 저장






#성적 상세조회
def showone_sungjuk():
    """
    성적조회 - 과목점수 + 총점평균등급
    :return: 없음
    """
    sjno = input('상세 조회할 학생 번호?:')

    sql = ' select * from sungjuk where sjno = :1 '

    conn = oracledb.connect(
        user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql, [sjno])

    for sjno, name, kor, eng, mat, tot, avg, grd, regdate in cursor:
        print(sjno, name, kor, eng, mat, tot, avg, grd, regdate)


    cursor.close()
    conn.close()


    info = '찾는 데이터가 없습니다.'




# 성적 데이터 수정시 수정할 데이터 입력받기
def read_again(sjno):
    """
    성적 데이터 수정시 수정할 데이터 입력받는 함수
    :param sjno: 수정할 학생번호
    :return:  새롭게 생성된 성적데이터
    """

    sql = ' select name, kor, eng, mat from sungjuk where sjno = :1 '
    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(sql, [sjno])


    sj = [None, None, None, None]
    for name, kor, eng, mat in cursor:
        sj =[name, kor, eng, mat]

    cursor.close()
    conn.close()

    if sj[0]:
        sj[0] = (input(f'새 이름: {sj[0]}) : '))
        sj[1] = int(input(f'새 국어 점수: (기존점수:{sj[1]}) : '))
        sj[2] = int(input(f'새 영어 점수: (기존점수:{sj[2]}) : '))
        sj[3] = int(input(f'새 수학 점수: (기존점수:{sj[3]}) : '))
        sj = compute_sungjuk(sj)

    return sj


# 성적데이터 수정
def modify_sungjuk():
    """
    성적데이터 수정
    :return:
    """
    sjno = input('수정할 학생 번호: ')

    # 수정할 성적데이터를 입력받고 성적처리한 결과를 받아옴
    sj = read_again(sjno)

    if sj[0]:    #수정데이터를 찾았다면
        sql = ' update sungjuk set name=:1, kor=:2, eng =:3, mat =:4, tot =:5,  '\
               ' avg =:6, grd=:7, regdate = sysdate '\
               ' where sjno =:8 '
        sj.append(sjno)

        conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
        cursor = conn.cursor()

        cursor.execute(sql, sj)
        conn.commit()
        print(f'{cursor.rowcount} 건의 데이터가 수정되었습니다.')

        cursor.close()
        conn.close()

    else:
        print('찾는 데이터가 없습니다')



# 성적데이터 삭제
def remove_sungjuk():
    """
    성적데이터 삭제
    :return:
    """
    sjno = input('삭제할 학생 번호: ')
    sql = ' delete from sungjuk where sjno = :1 '
    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql, [sjno])
    conn.commit()
    print(f'{cursor.rowcount} 건의 데이터가 삭제되었습니다.')

    cursor.close()
    conn.close()





# 성적프로그램 종료
def exit_program():
    """
    성적처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """
    print('프로그램 종료')
    sys.exit(0)