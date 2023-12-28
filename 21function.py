# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드 집합체
# 보통 여러 곳에 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 여러 곳에 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# (어떤 입력값을 주면) 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움

# 코드의 이식성이나 재사용성이 높아짐- 개발속도향상

# 다른 사람과의 협업시 코드가 섞이지 않게 하기 위한
# 목적도 있음 - 모듈


# 함수 정의
# def 함수명(매개변수):
#     함수몸체(코드들)
print('반목문')     #반복
# print('반목문')     #개선된 반ㅂㄱ
print('반목문')

for _ in range(3):
    print('반목문')
# 이러한 반복문을 여러번 사용해야 한다면?
# 또 만약, '미워요' 대신 '싫어요' 나 좋아요' 로 바꿔야 한다면?

# 함수의 유형
# 입력값 x   반환값 x
# 입력값 x   반환값 o   !!
# 입력값 o   반환값 x
# 입력값 o   반환값 o   !!!


# 함수 정의
# def 함수명(매개변수):
#     함수몸체(코드들)
print('반목문')     #반복
# print('반목문')
for _ in range(3):
    print('반목문')  #반복 개선


def saymsg1():              # 입력값x, 함수내에서 출력처리(반환값x)
    for _ in range(3):     #개선된 반복
        print('반목문')

saymsg1()


# 함수 호출
# 함수명 (), 함수명(입력값)

def saymsg2():
    for _ in range(3):
        print('반목문')
# 함수 호출
# 함수명 (), 함수명(입력값)

saymsg2()



def saymsg3(msg):
    for _ in range(3):
        return f'선생님 {msg}'

saymsg3('미워요')




# 온도센서예제(25 - 17p)
def SenserOn():
    print('온도센서 작동을 시작한다')
def SenserOff():
    print('온도센서 작동을 중지한다')



# 노트북예제(25 - 21p)
def cmToinch():
    a = int(input('길이를 입력하세요.(cm)'))
    b =  a / 2.54
    print(f'{a}cm = {b:.2f}inch')
cmToinch()

# 해설
length = int(input('길이를 입력하세요.(cm)'))
# 1cm = 0.393701
print(f'{length} cm= {length * 0.393701:.4f} inch')

def notebooksize():
    length = int(input('길이를 입력하세요.(cm)'))
    cm2inch = length * 0.393701
    print(f'{length} cm= {cm2inch:.4f} inch')

notebooksize()

##return 사용
def notebooksize3():                            # return으로 출력부만 외부돌출가능. 수정용이함
   print('길이를 입력하세요.(cm)', end ='')
   length = int(input())
   cm2inch = length * 0.393701
   return length, cm2inch

length, cm2inch = notebooksize3()
print(f'{length} cm= {cm2inch:.4f} inch')
print(f'{length} 센티미터= {cm2inch:.4f} 인치')




# 이동거리계산 (25 - 22p)
def movedist():
    time = int(input('이동 시간을 입력하세요'))
    speed = int(input('이동 속도를 입력하세요'))
    dist = time * speed
    print(f'이동 거리는 {dist:.1f} km 입니다.')

movedist()

##return 사용
def movedist2():                                 # return으로 출력부만 외부돌출가능. 수정용이함
    time = int(input('이동 시간을 입력하세요'))
    speed = int(input('이동 속도를 입력하세요'))
    dist = time * speed
    return dist

dist = movedist2()
print(f'이동 거리는 {dist:.1f} km 입니다.')


# 함수의 유형
# 입력값 x   반환값 x
# 입력값 x   반환값 o   !!
# 입력값 o   반환값 x
# 입력값 o   반환값 o   !!!

# 함수 정의
# def 함수명(매개변수):
#     함수몸체(코드들)


# return
# return으로 출력부만 외부돌출가능. 수정용이함

def saymsg4(msg):                   # 입력값o, 처리결과반환 (반환값o)
    text = ''                     # 개선된 반복
    for _ in range(3):
       text += f'선생님 {msg}\n'
    return text                      # 결과를 처리하지 않고 넘김

print(saymsg4('미워요'))




# 계산기 예제( 25 - 30p)
# return 사용 ( 행번호 옆에 ^로 토글 조작)
def readData():
    op1 = int(input('숫자를 입력하세요.'))
    op2 = input('연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈')
    op3 = int(input('숫자를 입력하세요.'))
    return op1, op2, op3

def computeNumber(op1, op2, op3):                   #op1 2 3은 인수로 전달
    result = 0
    if op2 == '1':
        result = op1 + op3
        op2 = '덧셈'
    elif op2 == '2':
        result = op1 - op3
        op2 = '뺄셈'
    elif op2 == '3':
        result = op1 * op3
        op2 = '곱셈'
    elif op2 == '4':
        result = op1 / op3
        op2 = '나눗셈'
    return op2, result

def calculator():
    #데이터 입력부
    op1, op2, op3 = readData()

    #데이터 계산
    op2, result = computeNumber(op1, op2, op3)          #op1 2 3은 인수로 전달

    #처리 결과 넘김
    return op2, result

op2, result = calculator()
print(f'{op2}결과: {result:.1f}')




# 함수에 값 전달하기 (25 - 41p)
# 매개변수parameter : 함수 정의시 함수에서 사용할 변수 정의
# 매개변수는 함수 호출시 전달받은 인수로 초기화되어 사용된다.
# 인수argument : 함수 호출시 매개변수에 전달할 실제 값



# 단위 환산 프로그램 (25 - 64p)
mm = int(input('길이(mm) 입력'))

cm = mm * 0.1
m = mm * 0.001
inch = mm * 0.03937
ft = mm * 0.003281



print(f'''
{mm}mm -> {cm}cm
{mm}mm -> {m}m
{mm}mm -> {inch}inch
{mm}mm -> {ft}ft
''')



def readMM():
    mm = int(input('길이(mm) 입력'))
    return mm


def convertAll(mm):
    cm = mm * 0.1
    m = mm * 0.001
    inch = mm * 0.03937
    ft = mm * 0.003281
    return mm, cm, m, inch, ft


def convertunit():
    mm = readMM()
    return convertAll(mm)


mm, cm, m, inch, ft = convertunit()
print(f'''
{mm}mm -> {cm}cm
{mm}mm -> {m}m
{mm}mm -> {inch}inch
{mm}mm -> {ft}ft
''')













