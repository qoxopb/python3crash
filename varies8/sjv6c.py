import json
import sys
from collections import OrderedDict
# sungjuks = {'response': {'body': {'totalCount': 999, 'items': []}}}
sjs = {'sungjuks':[]}



# 함수 정의
def show_menu(): # 메뉴 출력
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

def read_sungjuk():   #성적데이터 입력받음
    sj = OrderedDict()
    sj['name'] = input('이름: ')
    sj['kor'] = int(input('국어: '))
    sj['eng'] = int(input('영어: '))
    sj['mat'] = int(input('수학: '))
    return sj

def compute_sungjuk(sj):   #성적처리
    sj['tot'] = sj['kor'] + sj['eng'] + sj['mat']
    sj['avg'] = float(f"{sj['tot'] / 3:.1f}")
    sj['grd'] = '수' if sj['avg'] >= 90 else \
          '우' if sj['avg'] >= 80 else \
          '미' if sj['avg'] >= 70 else \
          '양' if sj['avg'] >= 60 else '가'
    return sj


def show_sungjuk():    #성적 데이터 출력
    print('성적데이터 조회')
    for sj in sjs['sungjuks']:
        print(f"이름: {sj['name']:s}, 국어: {sj['kor']}, "
              f"영어: {sj['eng']}, 수학: {sj['mat']}")


def save_sungjuk(sj):
    # 메모리 내에 생성된 json객체에 방금 생성한 성적데이터 저장
    sjs['sungjuks'].append(sj)
    # 메모리 내에 생성된 json객체의 모든 내용을 파일에 새롭게 저장
    with open('sungjuks.json', 'w', encoding='utf-8')as f:
       json.dump(sjs, f, ensure_ascii=False)




def addsungjuk():
    print('성적데이터 추가')
    sj = read_sungjuk()
    compute_sungjuk(sj)
    save_sungjuk(sj)                #성적데이터를 파일에 저장



# 프로그램 시작시 sungjuks.json 파일을 읽어 sjs변수에 초기화
def load_sungjuk():
    global sjs
    try:                    # 만일 작업중 오류가 발생하면
        with open('sungjuks.json', encoding='UTF-8')as f:
            sjs = json.load(f)
    except:
        pass                # 프로그램 실행 중단없이 다음코드 실행

def showone_sungjuk():
    return None


def modify_sungjuk():
    return None


def remove_sungjuk():
    return None


def exit_program():
    print('프로그램 종료')
    sys.exit(0)