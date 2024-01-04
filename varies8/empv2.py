import sys
import json
import sys
from collections import OrderedDict

emps = {'response': {'body': {'totalCount': 0, 'items': []}}}
items = []

def load_employees():
    print('프로그램을 초기화합니다')
    global emps
    global items

    try:                    # 만일 작업중 오류가 발생하면
        with open('employees.json', encoding='UTF-8')as f:
            emps = json.load(f)
            items = emps['response']['body']['items']
    except:
        # 프로그램 실행 중단없이 다음코드 실행
        items = emps['response']['body']['items']

    print('초기화 완료')


def show_menu():
    main_menu = '''
    -----------------------
    사원관리프로그램 v1
    -----------------------
    1. 사원정보 추가
    2. 사원정보 조회
    3. 사원정보 상세조회
    4. 사원정보 수정
    5. 사원정보 삭제
    0. 프로그램 종료
    -----------------------
    '''
    print(main_menu, end='')
    menu = input('=>메뉴를 선택하세요: ')
    return menu


def input_employee():
    emp = {}
    emp['empno'] = input('사번: ')
    emp['fname'] = input('이름: ')
    emp['lname'] = input('성: ')
    emp['email'] = input('이메일: ')
    emp['hdate'] = int(input('입사일: '))
    emp['jobid'] = input('직책: ')
    emp['sal'] = int(input('급여: '))
    emp['deptid'] = int(input('부서번호: '))
    return emp


def save_employee(emp):
    row = (f"{emp['empno']}, {emp['fname']}, {emp['lname']}, {emp['email']}, "
           f"{emp['hdate']}, {emp['jobid']}, {emp['sal']}, {emp['deptid']}\n")
    with open('employees.json', 'a') as f:
        f.write(row)
    items.append(emp)


def add_employee():   #데이터 입력받음
    print('사원정보를 등록합니다')
    emp = input_employee()
    save_employee(emp)



def read_employee():
    print('모든 사원정보를 조회합니다')
    result = ''
    for emp in items:
        result += (f"{emp['empno']}\t{emp['fname']}\t{emp['jobid']}\t{emp['deptid']}\n")
    print(result)



def readone_employee():
    print('특정사원의 상세정보를 조회합니다')
    empno = input('상세조회할 사원번호는?')

    info = ('찾는 데이터가 없습니다.')
    for emp in items:
        if emp['empno'] == empno:
            info = (f"{emp['empno']}, {emp['fname']}, {emp['lname']}, {emp['email']}, "
                    f"{emp['hdate']}, {emp['jobid']}, {emp['sal']}, {emp['deptid']}\n")
            break

    print(info)



def read_again(data, empno):
    emp = OrderedDict()
    emp['fname'] = int(input(f'새 이름: (기존:{data["fname"]}'))
    emp['email'] = int(input(f'새 이메일: (기존:{data["email"]}'))
    emp['jobid'] = int(input(f'새 직책: (기존:{data["jobid"]}'))
    emp['sal'] = int(input(f'새 급여: (기존:{data["sal"]}'))
    emp['deptid'] = int(input(f'새 부서번호: (기존:{data["deptid"]}'))
    return data



def flush_employee():
    with open('employees.json', 'w',) as f:
        json.dump(emps, f, ensure_ascii=False)


def modify_employee():
    print('특정사원의 정보를 수정합니다')
    empno = input('수정할 사원의 사원번호는?')

    data = None
    idx = None
    for i, emp in enumerate(items):
        if emp['empno'] == empno:
            data = emp
            idx = i

    if data:
        data = read_again(data, empno)
        items[idx] = data
        flush_employee()

    else:
        print('찾는 데이터가 없습니다.')





def remove_employee():
    print('특정사원의 정보를 제거합니다')
    empno = input('삭제할 사원의 사번')

    data = None
    for emp in items:
        if emp['empno'] == empno:
            data = emp
            break

    if data:
        confirm = input('정말 삭제하시겠습니까? (yes/no): ')
        if confirm == 'yes':
            items.remove(data)
            emps['response']['body']['totalCount'] -= 1
            print(f'{empno}의 데이터가 삭제되었습니다.')
            flush_employee()
        else:
            print('삭제가 취소되었습니다.')




def exit_program():
    print('프로그램을 종료합니다')
    sys.exit(0)




























