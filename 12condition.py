# (22 - 84p)
# if문
# 특정 조건을 만족하면 지정한 문장(들) 을 실행하는 조건문
# if 조건식 :
# 수행할 문장(들)


# 속도위반 체크 프로그램
# 기준속도: 50.km/
speed = int(inp('현재 속도'))
if speed >= 50:
    print('속도위반')



# (22 - 89p) 파이썬의 코드 블록
#  특정한 동작을 위한 코드를 한 곳에 모아둔 것
# 이러한 코드들은 반드시 같은 들여쓰기 내에 존재해야 함

# 조건식이 True인 경우 무조건 코드블록을 실행
if True: print('Hello, World!')


# if ~ else 문
# if문은 조건이 참일때만 지정한 코드를 실행하는 데 비해
# if ~ else 문은 조건이 참일때와 거짓일때 각각 지정한 코드를
# 실행한다는 것이 다름
# if 조건식:
#   수행할 문장1
# else:
#   수행할 문장2


# 자동 온도 조절 프로그램 (22 - 104p)
# 기계 온도 감지하여 팬을 자동으로 구동
# 기계 온도 입력
temp = int(input('기계 온도를 입력하세요.'))
if temp < 40:
    print('팬 가동')
else:
    print('팬 중지')


# 입력받은 정수를 3으로 나누고 소수점첫자리 반올림 정수 출력(22 - 105p)
num = int(input('양의 정수를 입력하시오'))
res = num / 3

if(res -int(res)) >= 0.5:
    res = int(res) + 1
else:
    res = int(res)

print(num, res)



# if ~ elif  (22 - 107p)
# 중첩 if문
# if문 속에 또 다른 if문을 포함시켜 작성하는 조건문
# 조건문을 중첩할때는 들여쓰기에 유의해야 함
# 다양한 조건에 따라 결과를 처리하고 싶을때 사용     -복잡함

# 평균이 73.5라 할때 조건에 따라
# 수/우/미/양/가 학점을
# 출력하는 조건문을 작성하세요
avg = 73.5
if avg >= 90: print('수')
else:
    if avg >= 80:
    else:
         print('우')
        if avg >= 70:
            print('미')
          if avg >= 60:
            print('우')'가'



# 다중 if문
# 중첩 if문을 작성하는 경우 조건이 많으면 다소 복잡함
# 이러한 중첩 if문을 단순하게 작성할 수 있는 조건문

# if 조건식1:
#     실행할문장1
# elif 조건식2:
#     실행할문장2
# else:
#     실행할문장3

avg = 85.5

if avg >= 90:
    print('수')
elif avg >= 80:
    print('우')
elif avg >= 70:
    print('미')
elif avg >= 60:
    print('양')
else:
    print('가')


if avg >= 90: print('수')
elif avg >= 80: print('우')
elif avg >= 70: print('미')
elif avg >= 60: print('양')
else: print('가')                        # 단순반복일 경우 한줄에 붙일수있음




# 자동주문 프로그램  (22 - 112p)
# 1번 한국어, 2번 영어, 3번 중국어, 그 외 번호 : 영어
check = int(input('Select number. 1.대한민국  2.USA  3.中國'))
if check == 1: print('주문?')
elif check == 2: print('Would you like to order?')
elif check == 3: print('您想订购吗？')
else: print('Would you like to order?')

### 해설
intro = '''
good morning...
Select number.
'''
print(intro, end='')
menu = input('1.대한민국  2.USA  3.中國')
if menu == 1: print('주문?')
elif menu == 2: print('Would you like to order?')
elif menu == 3: print('您想订购吗？')
else: print('Would you like to order?')




# bmi 지수 프로그램 (22 - 114p)
# 몸무게 / (키/100) **2
weight = float(input('몸무게: '))
height = float(input('키: '))
bmi = weight / (height / 100) ** 2
print(bmi)
if bmi <= 18.5: print('저체중')
elif 18.5 < bmi <= 23: print('정상')
elif 23 < bmi <= 25: print('비만전단계')
elif 25 < bmi <= 25: print('')
elif 25 < bmi: print('비만')
else: print('비만')


if bmi >= 35: result = '초고도비만'
elif bmi >= 30: result = '고도비만'
elif bmi >= 25: result = '비만'
elif bmi >= 23: result = '과체중'
elif bmi >= 18.5: result = '정상체중'
else: result = '저체중'
print(f'{weight}, {height}, {bmi:.0f}, {result}')





# 누진세    (22 - 121p)
# 리스트로 표를 만든다음에 n번째값 삽입으로 해야하나?
elec = int(input('전기 사용량을 입력하세요.'))

if elec <= 200:
    lchar = 910
    unit = 99.3
    char = elec * unit + lchar
elif 201 < elec <= 400:
    lchar = 1600
    unit = 187.9
    char = elec * unit + lchar
elif 400 < elec:
    lchar = 7300
    unit = 280.6
    char = elec * unit + lchar

print(f'사용량: {elec}kwh \n'
      f'기본요금: {lchar}원 \n'
      f'단가: {unit}원 \n'
      f'전기 요금: {char}원')


##해설
# 누진세 적용 전기요금 계산
# 전기요금 = 사용량 * 단가 + 기본요금
usage = int(input('전기 사용량은?'))
price = 99.3
basic = 910

if usage > 400:
    price = 280.6
    basic = 7300
elif usage >200:
    price = 187.9
    basic = 910

pay = usage * price + basic

print(f'사용량: {usage}kwh \n'
      f'기본요금: {basic}원 \n'
      f'단가: {price}원 \n'
      f'전기 요금: {pay}원')



# 현재년도가 각각 1992, 2000, 2020(윤)과
# 1900, 2100(윤x)에 대해 윤년여부를 출력하는
# 조건식을 작성하세요
# 윤년 1: 4로 나눠 나머지가 0이고
#       100으로 나눠 나머지가 0이 아니면
# 윤년 2: 400으로 나눠 나머지가 0
# elif문에서 마지막 else 문을 초기 변수로 선언하면 else 생략 가능

year = int(input('년도를 입력하세요(YYYY)'))
isLeap = '윤년이 아닙니다.'
cond1 = (year % 4 == 0) and (year % 100 !=0)
cond2 = year % 400 == 0

if cond1 or cond2:
    print('윤년입니다.')

print(f'{year}년은 {isLeap}')
























