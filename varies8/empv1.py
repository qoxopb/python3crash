import sys
emps = []


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


def load_employees():
    print('프로그램을 초기화합니다')
    print('초기화 완료')


def add_employee():   #데이터 입력받음
    print('사원정보를 등록합니다')
    em = {}
    em['employee_id'] = int(input('사번: '))
    em['first_name'] = input('성: ')
    em['last_name'] = input('이름: ')
    em['email'] = input('이메일: ')
    em['hire_date'] = int(input('입사일: '))
    em['job_id'] = input('직책: ')
    em['salary'] = int(input('급여: '))
    em['dapartment_id'] = int(input('부서번호: '))
    return em


def read_employee():
    print('모든 사원정보를 조회합니다')


def readone_employee():
    print('특정사원의 상세정보를 조회합니다')


def modify_employee():
    print('특정사원의 정보를 수정합니다')


def remove_employee():
    print('특정사원의 정보를 제거합니다')


def exit_program():
    print('프로그램을 종료합니다')
    sys.exit(0)




























