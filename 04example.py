# 1
#  가변/고정폰트
# 프로그래밍 언어 실습시 고정폭 폰트 사용
print('☆     ☆       ☆      ☆☆☆☆      ☆☆☆☆       ☆     ☆       /////')
print('☆     ☆     ☆  ☆    ☆     ☆     ☆     ☆     ☆     ☆      | o o |')
print('☆☆☆☆☆   ☆     ☆   ☆☆☆☆      ☆☆☆☆        ☆  ☆      ( |  ^  | )')
print('☆     ☆   ☆☆☆☆☆   ☆     ☆     ☆     ☆        ☆          | [_] |')
print('☆     ☆   ☆     ☆   ☆       ☆   ☆       ☆      ☆           ______')

# 3
# 변수 : 영문으로 시작, 공백불가(_ 로 대체)
rate1 = 1
long = 4
TimeLimit = 5
numberOfWindows = 6


# 학생 테이블의 각 컬럼 데이터도
# 변수로 선언하고 값으로 초기화
STDID = 1
HAKBUN = 201350050
STDNAME = '김태희'
ADDR = '경기도 고양시'
BIRTH = '1985-03-22'
DEPTID = 1
PROFID = 4
REGDATE = '2023-12-20 14:43:15'

print(STDID, HAKBUN, STDNAME, ADDR, BIRTH)
print(DEPTID, PROFID, REGDATE)

# 4
x, y, z = 1, 2, 3
s0, v0, t, g = 4, 5, 6, 9.8

print(3 * x, 3 * x + y, (x+y) / 7, (3 * x + y) / (z + 2))
print(s0 + v0 * t + (1 / 2) * g * t ** 2)

# 5.다음 문장의 실행결과는 무엇인지 서술하여라.
print(1 / 3, ( 1 / 3 ) * 3)        # 부동소수점 연산의 허점이 원인
print(7 / 3, 7 % 3, 7 // 3)
result = 2
result = /2      #result = result / 2
print(result)

# 6
x, y, m, n = 2.5, 1.5, 18, 4
print(x + n  * y - (x-n) * y)
print(m / n + m % n)
print(5 * x - n / 5)
print(1 - (1 - (1-1- ( n))))

# 7
# 파이썬 논리연산자
# 순서 : not > and > or


# (자바) and ||   or &&   not !
print(3 + 4.5 * 2 + 27 / 8)
print(true | false & 3 < 4 | ! (bool!l ㅠdㅇ이 == 7))
print(true | (3 < 5 & 6 >= 2))
print(!true > 'A')
print(7 % 4 + 3 - 2 / 6 * 'Z')
print('D' + 1 + 'M' % 2 / 3)
print(5.0 / 3 + 3 / 3)
print(53 % 21 < 45 / 18)
print((4 < 6) | True & False F false & (2 > 3))
print(7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))

# 9. 각 부울 표현식에 대한 값을 계산하여라. 자바는 단축식 평가
# short-circuit evaluation을 사용한다는 점에 주의하여라.
print(True & False & True | True)
print(True | true and true and false)
print((True and False) | (true and not False) | (false and notFalse))
print((2 < 3) | (5 > 2) and not (4 == 4) | 9 != 4)
print(6 == 9 | 5 < 6 & 8 < 4 | 4 > 3)

# 10
print(27 / 13 + 4)
print(27 / 13 + 4.0)
print(42.7 % 3 + 18)
print(23 / 5 + 23 / 5.0)

print(2.0 + bool('a'))       # 문자와 숫자 간 산술연산 불가
print(2 + bool('a'))

print('a' + 'b')

print(bool('a') / bool('b'))     # 문자끼리 산술연산 불가
print(float(bool('a') / bool('b')))

# 논리식과 산술식이 결합된 수식에서는
# 논리식의 결과가 True 라면 값이 출력
# 논리식의 결과가 False 라면 False가 출력
print((3 < 4) and 5 / 8)
print((3 > 4) and 5 / 8)
print('a' and not 'b')


# 11
# 이름과 몸무게, 나이를 변수로 선언하고 자신의 것을 값으로 초기화하는
# 프로그램을 작성하여라 (MyInfo)
name = '홍길동'
weight = 32.5
age = 19
print(name, weight, age)




# 12
# 생년월일을 이용해서 나이를 계산하는 프로그램을 작성하여라. (MyAge
# 세는나이 : 출생 시 1살, 해가 지나면 +1
# 연 나이 : 출생 시 0살, 생일이 지나면 +1
# 만 나이 : 현재년도 - 출생년도
birthYear = 2005
currentYear = 2023
age = currentYear - BirthYear
print('연나이 : ', age)


# 13
# 구구단 중 7단을 출력하는 프로그램을 작성하여라. (GuGu7Dan)
print('7 * 1 = 7')
print('7 * 2 = 14')
print('7 * 3 = 21')
print('7 * 4 = 28')
print('7 * 5 = 35')
print('7 * 6 = 42')
print('7 * 7 = 49')
print('7 * 8 = 56')
print('7 * 9 = 63')

# f-string
dan = 7
print(f'{dan} x 1 = {dan * 1}')
print(f'{dan} x 2 = {dan * 2}')
print(f'{dan} x 3 = {dan * 3}')
print(f'{dan} x 4 = {dan * 4}')
print(f'{dan} x 5 = {dan * 5}')
print(f'{dan} x 6 = {dan * 6}')
print(f'{dan} x 7 = {dan * 7}')
print(f'{dan} x 8 = {dan * 8}')
print(f'{dan} x 9 = {dan * 9}')
# % 서식
print('%d x 1 = %d' % (dan, dan * 1))
# .format
print('{} x 1 = {}'.format(dan, dan * 1))



































