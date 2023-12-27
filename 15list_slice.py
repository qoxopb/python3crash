# 슬라이싱slicing (23 - 106p)
# 연속적인 객체들(리스트, 튜플, 문자열) 에 범위를 지정하고
# 부분적으로 객체를 선택해 가져오는 방법 및 표기법
# 리스트 객체에서 필요 항목만 뽑아 사용
# 객체명[시작:끝-1:스텝]

# 다음코드에서 생년월일 추출
jumin = '123456-1234567'
print(jumin[0:6])
print(jumin[:6])       #시작 생략하면 자동으로 0번부터

# 생년월일과 - 를 제외한 나머지 추출
print(jumin[7:14])
print(jumin[7:])       #끝 생략하면 리스트의 맨 마지막 문자까지

# 코드에서 짝수/홀수 위치의 문자 추출
print(jumin[0:14:2])    #홀수 위치 문자 추출
print(jumin[0::2])
print(jumin[::2])
print(jumin[1:14:2])     #짝수 위치 문자 추출
print(jumin[1::2])

# 역순으로 추출:  step을 -(음수)로 설정, 처음 끝 반전(생략갸능)
print(jumin[14:0:-1])
print(jumin[14::-1])
print(jumin[::-1])


# (23 - 108p) 확인문제
#역순출력
print(alphabet[:])
print(alphabet[::-1])
#요구사항에 따라 출력
print(alphabet[2:5+1])
#...


# (14example) 33. 숫자 6자리를 입력하면 신용카드의 종류와 은행정보(슬라이싱 사용)
cardnum = input('카드번호는?')

if cardnum[:2] == '35':
    if cardnum == '356317': cardname = 'JCB카드 NH농협카드'
    elif cardnum == '356901': cardname = 'JCB카드 신한카드'
    elif cardnum == '356912': cardname = 'JCB카드 국민카드'
elif cardnum[:1] == '4':
    if cardnum == '404825': cardname = '비자카드 비씨카드'
    elif cardnum == '438676': cardname = '비자카드 신한카드'
    elif cardnum == '457973': cardname = '비자카드 국민은행'
elif cardnum[:1] == '5':
    if cardnum == '515594': cardname = '마스타카드 신한카드'
    elif cardnum == '524353': cardname = '마스타카드 외환카드'
    elif cardnum == '540926': cardname = '마스타카드 국민은행'

print(f'{cardnum} {cardname}')



# 리스트 합치기: extend, +
 a = [1, 2, 3]
 b = [4, 5, 6]
 c = ['7', '8', '9']

a.extend(b)        # a = a + b
print(a)

b.extend(c)
print(b)


# 리스트의 모든 요소 존재 파악:  in/not in 연산자
todo = ['cleaning', 'shopping', 'study', 'exercise', 'game']

print('drive' in todo)
print('shopping' in todo)            #T/F 로 찾는 값 유무 확인가능

# 리스트의 모든 요소 존재 순회
for item in todo:
    print(item, end=' ')

# 리스트의 모든 요소 존재 순회 : enumerate(항목 인덱스도 출력 가능 - idx)
for idx, item in enumerate(todo):
    print(idx, item)

# 리스트의 모든 요소 제거 : clear
print(todo)
todo.clear()
print(todo)



#혈액 보관 시스템 (23 - 111p)
bloods = []
a, b, ab, o = 0, 0, 0, 0

for idx in range(1, 10+1):
    print(f'혈액형을 입력하세요. A B AB O {idx}/10')
    blood = input('A, B, AB, O : ')
    bloods.append(blood)

for bd in bloods:                 #리스트 내에서 개별요소 검색 후 각 변수에 1씩 더해준다
    if bd == 'A': a += 1
    if bd == 'B': b += 1
    if bd == 'AB': ab += 1
    if bd == 'O': o += 1

print(f'''
------------------
혈액형 : 개수
-----------------
A형 : {a}
B형 : {b}
O형 : {o}
AB형 : {ab}

''')


# 리스트의 항목별 빈도 계산 : count(값)
bloods.count('A')
bloods.count('B')
bloods.count('O')
bloods.count('AB')

