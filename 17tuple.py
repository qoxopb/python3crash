# 튜플 (24 - 4p)
# 튜플 자료형
# 순차적 데이터를 관리하는 자료형(순서가 존재)
# 리스트와 동일하지만, 변경 불가능 특성을 지님
# => 생성은 가능 / 추가,수정,삭제는 불가능
# 튜플 객체 생성은 ()를 사용
## 선언은 () , 조회는 []

tuple1 = ()      #빈 튜플
tuple2 = (1,2,3,4,5)
tuple3 = ('a', 'b', 'c', 'd', 'e')
tuple4 = (1, 'a', 'b', 123, 'd', 3.14)

print(tuple4)

# 튜플 추가/수정/삭제 해보기
tuple1.append(10)           #튜플에 추가/수정/삭제 미지원
tuple2[4] = 10
tuple3.remove(3)

# 튜플 합치기 : + 만 지원
print(tuple2 + tuple3)
tuple2.extend(tuple3)     #미지원


# 만약, 튜플의 요소를 변경해야 한다면?
# 튜플을 리스트로 변환한 후 요소를 변경하고
# 다시 리스트를 튜플로 변환하면 됨
# 튜플을 리스트로 변환 : list(대상)
# 리스트를 튜플로 변환 : tuple(대상)
tuple1 = list(tuple1)
tuple1.append('A')
tuple1.append('B')
tuple1 = tuple(tuple1)
print(tuple1)

# 리스트/튜플 요소의 인덱스 알아내기 : index(값)
tuple4.index(3.14)
tuple4.index('d')


# 튜플 정렬 : sorted()
## 정렬 반환값은 리스트로 저장됨!




# 예제(24 - 20p)
numbers =(10, 20, 30, 40, 50, 60)
print(numbers[1 : 1+2])
print(numbers[:2])
print(numbers[1 : 4])
print(numbers[3 : len(numbers)-1])





# 난수 생성하기
# random이라는 모듈이 필요
# random()    : 0~1사이 임의의 부동소수점 숫자 출력
# randint(x,y) : x~y사이 임의의 정수 출력
# randrange(s,e,l) : 시작부터 끝 사이 임의의 숫자 출력

import random as rnd

rnd.seed(2312271045)
print(rnd.random())
print(rnd.randint(1, 10))     # 1~ 10 사이 난수 생성
print(rnd.randrange(1, 10))      # 1~9사이 난수 생성

# 1부터 100 사이 3의 배수를 난수로 출력
print(rnd.randrange(3, 100, 3))


# 1 ~ 45 사이 임의의 정수 6개를 추출해서
# 리스트와 튜플에 저장하는 코드를 작성하세요
num1 = []
num2 = ()

num2 = list(num2)
for _ in range (6):
    num1.append(rnd.randint(1, 45))
    num2.append(rnd.randint(1, 45))
num2 = tuple(num2)

print(num1)
print(num2)



# 1 ~ 45 사이 임의의 정수 6개를 추출해서
# 리스트와 튜플에 저장하는 코드를 작성하세요
# 단, 중복값은 제외하여 저장


num1 = []
cnt = 0      #몇번만에 값이 생겼는지 확인
while len(num1) < 6:           #for vs while
    cnt += 1
    num = rnd.randint(1, 45)
    if num not in num1:
        num1.append(num)
print(num1, cnt)


