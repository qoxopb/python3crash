import json
import sys
from collections import OrderedDict
# sungjuks = {'response': {'body': {'totalCount': 999, 'items': []}}}

sjs = {}
items = []
totalCount = 0



def show_menu():
    """
    메뉴 선택 출력 함수
    :return:
    """
    main_menu = '''
    -----------------------
    성적처리프로그램 v6c
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

    sj = OrderedDict()
    sj['name'] = data[0]
    sj['kor'] = int(data[1])
    sj['eng'] = int(data[2])
    sj['mat'] = int(data[3])
    return sj


# 성적 처리(총점, 평균, 학점 계산)
def compute_sungjuk(sj):
    """
    총점평균등급 산출 함수
    :param sj: 입력받은 성적
    :return: 총점평균등급
    """
    sj['tot'] = sj['kor'] + sj['eng'] + sj['mat']
    sj['avg'] = float(f"{sj['tot'] / 3:.1f}")
    sj['grd'] = '수' if sj['avg'] >= 90 else \
          '우' if sj['avg'] >= 80 else \
          '미' if sj['avg'] >= 70 else \
          '양' if sj['avg'] >= 60 else '가'
    return sj

# 메뉴 출력
def show_sungjuk():
    """
    성적조회 - 과목 점수
    :return: 없음
    """
    print('성적데이터 조회')
    for sj in items:
        print(f"이름: {sj['name']:s}, 국어: {sj['kor']}, "
              f"영어: {sj['eng']}, 수학: {sj['mat']}")


# 성적 데이터 저장(sunguks.json)
def save_sungjuk(sj):
    """
    입력받은 성적과 계산한 총점평균등급을 sunguks.json 에 저장
    :param sj: 총점평균등급
    :return: 없음
    """
    global sjs

    # 메모리 내에 생성된 json객체에 방금 생성한 성적데이터 저장
    items.append(sj)
    sjs['response']['body']['totalCount'] += 1
    # 메모리 내에 생성된 json객체의 모든 내용을 파일에 새롭게 저장
    with open('sungjuks.json', 'w', encoding='utf-8')as f:
       json.dump(sjs, f, ensure_ascii=False)



# 성적 데이터 추가 (입력-처리-저장)
def addsungjuk():
    """
    새로운 성적 데이터 추가, sunguks.json에 저장
    :return: 없음
    """
    print('성적데이터 추가')
    sj = read_sungjuk()
    compute_sungjuk(sj)
    save_sungjuk(sj)                #성적데이터를 파일에 저장



# 프로그램 시작시 sungjuks.json 파일을 읽어 sjs변수에 초기화
def load_sungjuk():
    """
    기존 성적을 이름으로 조회
    :return: 없음
    """
    global sjs
    global items
    global totalCount
    try:                    # 만일 작업중 오류가 발생하면
        with open('sungjuks.json', encoding='UTF-8')as f:
            sjs = json.load(f)
            items = sjs['response']['body']['items']
            totalCount = sjs['response']['body']['totalCount']
    except:
         # 프로그램 실행 중단없이 다음코드 실행
        items = sjs['response']['body']['items']
        totalCount = sjs['response']['body']['totalCount']



#성적 상세조회
def showone_sungjuk():
    """
    성적조회 - 과목점수 + 총점평균등급
    :return: 없음
    """
    name = input('상세 조회할 학생이름은?')

    info = '데이터가 없습니다.'
    for sj in items:
        if sj['name'] == name:
            info = f"{sj['name']} {sj['kor']} {sj['eng']} {sj['mat']} " \
                   f"{sj['tot']} {sj['avg']} {sj['grd']}"
            break  # 찾고나면 검색 작업 중단

    print(info)


# 성적 데이터 수정시 수정할 데이터 입력받기
def read_again(data, name):
    """
    성적 데이터 수정시 수정할 데이터 입력받는 함수
    :param data: 기존에 저장된 성적데이터
    :param name: 수정할 데이터의 이름
    :return:  새롭게 생성된 성적데이터
    """
    kor = int(input(f'새 국어 점수: (기존점수:{data["kor"]}'))
    eng = int(input(f'새 영어 점수: (기존점수:{data["eng"]}'))
    mat = int(input(f'새 수학 점수: (기존점수:{data["mat"]}'))

    data = OrderedDict()
    data['name'] = name
    data['kor'] = kor
    data['eng'] = eng
    data['mat'] = mat

    return data


# 성적 데이터 수정/삭제 시 변경사항 파일에 반영
def flush_sungjuk():
    """
    성적 데이터 수정/삭제 시 변경사항 파일에 반영
    :return:
    """
     with open('sungjuks.json', 'w', encoding='utf-8') as f:
        json.dump(sjs, f, ensure_ascii=False)



# 성적데이터 수정
def modify_sungjuk():
    """
    성적데이터 수정
    :return:
    """
    name = input('수정할 학생 이름: ')
    # 수정할 학생 데이터를 이름으로 찾기
    data = None
    idx = None
    for i, sj in enumerate(items):
        if sj['name'] == name:
            data = sj
            idx = i

    # 수정할 학생 데이터를 찾았다면
    # 새로운 값을 입력받고, 다시 성적 처리함
    if data:
        data = read_again(data, name)
        compute_sungjuk(data)

        # 리스트의 기존 데이터를 버리고 새로운 데이터로 재설정
        items[idx] = data

        # 변경사항을 json 파일에 반영
        flush_sungjuk()
    else:
        print('데이터가 없습니다')



# 성적데이터 삭제
def remove_sungjuk():
    """
    성적데이터 삭제
    :return:
    """
    name = input('삭제할 학생 이름: ')

    # 삭제할 데이터를 찾음
    data = None
    for sj in items:
        if sj['name'] == name:
            data = sj
            break

    # 삭제할 데이터를 찾았다면
    if data:
        confirm = input('정말 삭제하시겠습니까? (yes/no): ')
        if confirm == 'yes':
            items.remove(data)
            sjs['response']['body']['totalCount'] -= 1
            print(f'{name}의 데이터가 삭제되었습니다.')
            flush_sungjuk()
        else:
            print(f'삭제가 취소되었습니다.')



# 성적프로그램 종료
def exit_program():
    """
    성적처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """
    print('프로그램 종료')
    sys.exit(0)