# 반복문
# 특정 문장/코드를 지정한 횟수/조건에 의해 반복 실행하는 문장

# 간단한 메세지 한번 출력
print('오늘 날씨 추워요!')

# 간단한 메세지 여러번 출력
print('오늘 날씨 추워요!')
print('오늘 날씨 추워요!')
print('오늘 날씨 추워요!')

# 반복문 사용 시
# 반복용이성과 수정용이성 제공

# 파이썬의 반복문
# for : 지정한 횟수만큼 반복
# while : 지정한 조건에 의해 반복

# for문
# for 변수 in range(시작값, 종료값, 값 사이의 간격)
#   반복할 문장       (들여쓰기)
# 반복횟수는 range(시작값, 종료값)으로 유추가능
# 즉, 횟수는 종료값 - 시작값 - 1 로 계산됨
# range함수는 시작값과 종료값-1 사이의 연속된 정수들을 반환함







# 1부터 10까지 정수 출력
print(1,2,3,4,5,6,7,8,9,10)
print(list(range(1,10+1)))

# 1부터 10까지 홀수 출력
print(list(range(1,10,2)))

# 이터러블iterable 개체
# 값을 차례대로 꺼내볼 수 있는 객체를 의미
# 보통 리스트, 튜플, 딕셔너리 등의 개체를 의미
# 반복문에 자주 사용
for i in range(10):
=> for i in (1.2.3.4.5.6.7.8.9.10)


# 반복문 이용해 날씨 소감 출력
for i range(1,4):
    print(print('오늘 날씨 추워요!'))

# 1부터 10까지 모든 정수 출력
for i in range (1, 10+1):    #  1,2,3,...,9,10
    print(i, end=',')                   # range의 개별 값이 i에 찍힘

# 1부터 100까지 모든 정수의 합
sum = 0      #합계 저장할 변수 생성

for i in range (1, 100+1):
    sum = sum + i
    print(sum)

# 1~N까지의 합을 구하는 공식 : 가우스 덧셈공식
# => (N * (N+1)) / 2
tot = (100 * (100 + 1)) / 2
print(tot)

# N ~ NN 의 합을 구하는 공식은?


# 구구단 중 특정 단을 입력받아 출력  (23 - 17p)
# 예를 들어 7단
# '7 * 1 = 7'
# '7 * 2 = 14'
# '7 * 3 = 21'
# '7 * 4 = 28'
# ...
# '7 * 9 = 63'
dan = int(input('몇단?'))
print(f'{dan} x i = {dan*i}')

for i in range (1,9+1):
    print(f'{dan} x {i} = {dan * i}')


# 2 ~ 8 사이 짝수 출력
print(list(range(2,8+1,2)))

for i in range (2,8+1,2):
    print(i = end=' ')



# 음수 출력하기
print(list(range(-10,0+1)))
print(list(range(10, 0+1, -1)))     #간격을 음수로 설정 가능

# 시작값이 없는 range 함수
# 이럴 경우 시작값은 자동으로 0부터 시작
print(list(range(1,10)))
print(list(range(10)))


# 이터러블에 문자열을 넣으면 아이템에는
# 문자열의 첫 문자부터 끝 문자가 순차적으로 저장됨
# 결과적으로 실행문은 문자 개수만큼 반복 실행됨
for c in 'Hello':
    print(c, end=' ')

# 이터러블에 리스트를 넣으면 아이템에는
# 리스트를 구성하는 요소들이 순차적으로 저장됨
# 결과적으로 실행문은 리스트의 요소수만큼 반복실행
menus = ['라면', '돈까스', '짜장면', '냉면', '정식']

for i in range(len(menus)):
    print(menus[i])

for menu in menus:
    print(menu)



# pass 키워드
# 반복문 사용시 코드만 작성해 놓고
# 실행문은 나중에 추가하고 싶을 경우
# pass 키워드 사용
for i in range(1,100):
    pass                     # 반복할 내용은 나중에 작성


# 반복 수행시 이터러블 객체가 필요없는 경우
# 변수명 대신 _ 사용하기도 함
for _ in range(10):
    print('Hello, World!')




# 중첩반복문
# 두 개이상의 반복문을 이용해서 반복실행을 할수도 있음
# 보통 2개의 반복문을 중첩해서 사용하는 경우가 많음
# 이 경우 바깥쪽 반복문은 행을,
# 안쪽 반복문은 열을 반복하는데 사용함
# 총 반복횟수는 (바깥쪽 반복문 횟수) * (안쪽 반복문 횟수)임

    # *
    # **
    # ***
    # ****
    # ***** 모양 출력하기

for i in range(1,5+1):             # 행
    for j in range(1,5+1):         # 열
        print('*', end='')
    print()                        #줄바꿈 (새로운 행 만듦)
##안쪽 행(* 5개) 만족 시 줄바꿈 후 다른행 실행






# 2단부터 9단까지의 구구단을 출력하는
# 중첩반복문 작성
    for i in range(2, 9+1):
        for j in range(1, 9+1):
            # 아래로 끝없이 출력
            print(f'{i} x {j} = {i * j}')
        print()

    for i in range(2, 9+1):
        for j in range(1, 9+1):
            # 줄바꿈 없이 출력하되
            #9개의 단을 출력하고 줄바꿈 추가
            print(f'{i} x {j} = {i * j}', end=' ')
        print()

    for i in range(2, 9+1):
        for j in range(1, 9+1):
            # 단 세로출력이 아닌 가로출력으로
            # 균일한 출력을 위해 숫자 자릿수 맞추기 - 자릿수 지정(숫자 오른쪽정렬 문자 왼쪽정렬)
            print(f'{j} x {i} = {i * j:2d}', end='   ')
        print()



    for i in range(2, 9 + 1):
        #2단부터 5단까지 ,6단부터 9단까지
        for j in range(2, 5+ 1):
            print(f'{j} x {i} = {i * j:2d}', end='   ')
        print()

    for i in range(1, 9 + 1):
        #2단부터 5단까지 ,6단부터 9단까지
        for j in range(6, 9+ 1):
            print(f'{j} x {i} = {i * j:2d}', end='   ')
        print()






# employees.csv를 이용해서 사원정보를 입력하면
# list에 각각 저장하는 코드를 작성하세요
# 사번empno, 이름fname, 성lname, 이메일email,
# 입사일hdate, 직책jobid, 급여sal, 부서번호deptid

    empnos = []
    fnames = []
    lnames = []
    emails = []
    hdates = []
    jobids = []
    sals = []
    deptids = []

# 데이터 작업 (list append와 분리 권장)
empno = input('사번: ')
fname = input('이름: ')
lname = input('성: ')
email = input('메일: ')
hdate = input('입사일: ')
jobid = input('직책: ')
sal = input('급여: ')
deptid = input('부서번호: ')

empnos.append(empno)
fnames.append(fname)
lnames.append(lname)
emails.append(email)
hdates.append(hdate)
jobids.append(jobid)
sals.append(sal)
deptids.append(deptid)

for i in range(len(empnos)):
    print(f'{empnos[i]} {fnames[i]} {lnames[i]} '
          f'{emails[i]} {hdates[i]} {jobids[i]} '
            f'{sals[i]} {deptids[i]}')

























































