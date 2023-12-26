# while 문 (23 - 31p)
# 조건을 만족할때까지 반복 실행
# 변수 = 초기값
# while 조건식:
#   반복할문장
#   변수증가/감소

# 1 ~ 10 까지 모든 정수 출력
# for i in range (1,10+1):
#   print(i, end=' ')
i = 1                     # 반복 초기값
while i <= 10:            # 반복 종료조건
    print(i, end=' ')
    i = i + 1             #반복 증감



# 1~50까지 모든 정수 중 홀수만 출력
i = 1
while i <= 50:
    if i % 2 != 0: print(i, end=' ')             # 2로 나눠 나머지가 0이 아닌 수
    i = i + 1


# 1~50까지 모든 정수 중 7의 배수만 출력
i = 1
while i <= 50:
    if i % 7 == 0: print(i, end=' ')             # 7로 나눠 나머지가 0이 아닌 수
    i = i + 1

# 1~200까지 모든 정수의 합 출력
i = 1
sum = 0
while i <= 200:
    sum = sum + i
    i = i + 1


# 1~100까지 모든 정수 중 3과 8의 공배수와 최소공배수 출력
i = 1
mincm = 0
while i <= 100:
    if i % 3 == 0 and i % 8 == 0:
        print(i, end = ' ')
        if mincm == 0: mincm = i         # 최소공배수 저장
    i = i + 1

print(f'공배수: {mincm}')


# 반복문 내 실행중지 : break
# for, while문 내에서 반복흐름을 벗어나기 위해 사용

# 1~10000 까지의 정수 합 출력
# 단, 정수 합이 12345보다 크면 계산 중단
i = 1
sum = 0
while i <= 10000:
    if sum > 12345:
    break
    sum = sum + i
    i = i + 1

print(sum)
i = 1
sum = 0
while i <= 10000:
    if sum > 12345:
    break
    sum = sum + i
    i = i + 1


#반복문 내 반복 건드리기 : continue
# 반복문 내에서 반복흐름을 일시적으로 넘기기 위해 사용


# 1~100 까지의 정수 합 출력
# 단, 3의 배수나 7의 배수는 제외하고 계산
i = 1
sum = 0

for i in range(1, 100+1):
    if i % 3 == 0 and i % 7 == 0: continue   #조건 미충족시 다음행
    sum = sum + i

print(sum)



i = 0
sum = 0

while i < 100:
    i = i + 1
    if i % 3 == 0 and i % 7 == 0: continue
    sum = sum + 1

print(sum)



# 실전예제(23 - 57p)
# 1~99 사이 3/6/9 있으면 짝! 출력
for i in range(1, 99+1):
    if '3' in str(i): print('짝!', end=' ')
    if '6' in str(i): print('짝!', end=' ')
    if '9' in str(i): print('짝!', end=' ')
    print()

## 숫자추가, 예외 수정
for i in range(1, 99+1):
    j = ''
    if '3' in str(i): j += '짝!'
    if '6' in str(i): j += '짝!'
    if '9' in str(i): j += '짝!'
    if i ==33 or i==66 or i == 99: j += '짝!'
    print(f'{i} {j}')


### 1~9: 3/6/9. 3의 배수 여부 확인
### 10~99: 각각 문자가 3의 배수(3/6/9)인지 확인
for i in range(1, 99+1):
    if i <=9:      #1~9사이의 3/6/9
        if i % 3 == 0: print(i, '짝!')
        else: print(i)
    else:         #10~99 사이의 3/6/9
        print(i, end='')

        num1 = int(str(i)[0])
        num2 = int(str(i)[1])

        if num1 % 3 == 0: print('짝!', end='')
        if num2 != 0 and num2 % 3 == 0: print('짝!', end='')
         print()





# 오전9시 ~ 오후6시까지 열차 교차시간 알아내기
trainA = 10
trainB = 25
trainC = 30

for m in range(1, 540+1):      #?운행시간 총 9시간 총 540분
    if m % 10 == 0:
        if m % trainA == 0 and m % trainB == 0:                    # 9시 + 운행시간 이므로 +9해줌
        print(f'{9+ m // 60:02d}시 {m % 60:02d}분 A-B')            # 분단위를 60으로 나눈 몫이 시간 나머지가 분 + :02d 자릿수맞추기

    if m % trainB == 0 and m % trainC == 0:
        print(f'{9+ m // 60:02d}시 {m % 60:02d}분 B-C')

    if m % trainA == 0 and m % trainC == 0:
        print(f'{9+ m // 60:02d}시 {m % 60:02d}분 A-C')

    if m % trainA == 0 and m % trainB == 0 and m % trainC == 0:
        print(f'{9+ m // 60:02d}시 {m % 60:02d}분 A-B-C')


# 관리자 로그인 기능
passwd = 'hanbitac'
for i in range (1,5+1):
    passwd = input('관리자 암호를 입력하세요.')
    if passwd == 'hanbitac':
        print('로그인 되었습니다.')
        exit()
    else: print('암호를 다시 확인하세요')
else: print('로그인 실패')
    exit()



## 해설
logincnt = 1
passwd = 'hanbitac'
while True:                #반복횟수규정 없이 조건부합여부로 연속조건설정가능
    if logincnt > 5:
        print('로그인 실패! 횟수 초과')
        break

    pwd = input('관리자 암호를 입력하세요')
    if passwd != pwd:
        print('암호를 다시 확인하세요')
        logincnt += 1
    else:
        print('로그인 되었습니다')
        break

