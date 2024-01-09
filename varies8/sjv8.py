import sys
from varies8.SungJuk import SungJuk
from varies8.SungJukService import SungJukservice
from varies8.SungJukDAO import SungJukDAO


# 성적 데이터 추가 (입력-처리-저장)
def addsungjuk():
    """
    새로운 성적 데이터 추가 (입력 처리 저장)
    :return: 없음
    """
    print('성적데이터 추가')
    sj = SungJukservice.read_sungjuk()
    SungJukservice.compute_sunjuk(sj)

    rowcount = SungJukDAO.insert_sungjuk(sj)

    print(f'{rowcount}건의 성적데이터가 추가됨.')



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




# 성적 데이터 저장(sungjuk 테이블)
def save_sungjuk(sj):
    """
    성적 데이터 저장(sungjuk 테이블)
    :param sj: 입력받아 처리된 성적데이터(총점평균등급)
    :return: 없음
    """
    sql =' insert into sungjuk (name, kor, eng, mat, tot, avg, grd) ' \
         ' values (:1,:2,:3,:4, :5,:6,:7) '

    conn = oracledb.connect(
        user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(sql, sj)
    conn.commit()
    print(cursor.rowcount, '건의 성적데이터 추가됨.')

    cursor.close()
    conn.close()



# 모든 성적 데이터 출력(번호/이름/국/영/수/등록일)
def show_sungjuk():
    """
    성적조회 - 모든 성적 데이터 출력(번호/이름/국/영/수/등록일)
    :return: 없음
    """
    print('성적데이터 조회')
    rows = SungJukDAO.select_sungjuk()
    for row in rows:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {str(row[5])[:10]}')


#성적 상세조회
def showone_sungjuk():
    """
    성적조회 - 과목점수 + 총점평균등급
    :return: 없음
    """
    sjno = input('상세 조회할 학생 번호?:')

    row = SungJukDAO.selectone_sungjuk(sjno)

    print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]}')

    info = '찾는 데이터가 없습니다.'




# 성적데이터 수정
def modify_sungjuk():
    """
    성적데이터 수정
    :return:
    """
    sjno = input('수정할 학생 번호: ')
    # 튜플객체를 수정하기 위해 리스트객체로 변환
    sj = list(SungJukDAO.selectone_sungjuk(sjno))

    if sj[0]: # 만일, 수정데이터가 존재한다면
        sj[1] = (input(f'새 이름: {sj[1]}) : '))
        sj[2] = int(input(f'새 국어 점수: (기존점수:{sj[2]}) : '))
        sj[3] = int(input(f'새 영어 점수: (기존점수:{sj[3]}) : '))
        sj[4] = int(input(f'새 수학 점수: (기존점수:{sj[4]}) : '))
        # 조회한 결과를 클래스 타입으로 변경 후 다시 성적처리
        sj = SungJuk(sj[1], sj[2], sj[3], sj[4])
        SungJukservice.compute_sunjuk(sj)

        rowcnt = SungJukDAO.update_sungjuk(sj, sjno)
        print(f'{rowcnt} 건의 데이터가 수정되었습니다.')


    else:
        print('데이터가 존재하지 않습니다.')



# 성적데이터 삭제
def remove_sungjuk():
    """
    성적데이터 삭제
    :return:
    """
    sjno = input('삭제할 학생 번호: ')
    rowcnt = SungJukDAO.delete_sungjuk(sjno)
    print(f'{rowcnt} 건의 데이터가 삭제되었습니다.')




# 성적프로그램 종료
def exit_program():
    """
    성적처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """
    print('프로그램 종료')
    sys.exit(0)
