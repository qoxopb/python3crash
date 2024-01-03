import sys
emps = []


def load_employees():
    print('프로그램을 초기화합니다')
    global emps
    dicts = []

    with open('employees.csv') as f:
        datas = f.readlines()

    for data in datas:
        item = data.strip().split(',')
        d = {'empno':item[0], 'fname':item[1], 'lname':item[2], 'email':item[3], 'hdate':item[4],
            'jobid':item[5], 'sal':item[6], 'deptid':item[7]}
        dicts.append(d)

    emps = dicts
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
    with open('employees.csv', 'a') as f:
        f.write(row)
    emps.append(emp)


def add_employee():   #데이터 입력받음
    print('사원정보를 등록합니다')
    emp = input_employee()
    save_employee(emp)



def read_employee():
    print('모든 사원정보를 조회합니다')
    result = ''
    for emp in emps:
        result += (f"{emp['empno']}\t{emp['fname']}\t{emp['jobid']}\t{emp['deptid']}\n")
    print(result)



def readone_employee():
    print('특정사원의 상세정보를 조회합니다')


def modify_employee():
    print('특정사원의 정보를 수정합니다')


def remove_employee():
    print('특정사원의 정보를 제거합니다')


def exit_program():
    print('프로그램을 종료합니다')
    sys.exit(0)




























