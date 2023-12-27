# 딕서너리
# 이름key과 값value으로 구성된 연관배열의 일종
# 자료구조 선언 시 {}를 사용하고
# 이름과 값은 : 으로 구분해서 정의함
# 다른 언어의 JSON과 유사한 구조
# 데이터분석시 주로 사용하는 자료구조 : mongodb
# 키를 통해 자료를 찾는 해쉬테이블을 이용하므로 검색속도가 빠름


# 중간고사 성적을 dict로 선언
mids = {'C/C++': 'A', 'Java': 'B+', '네트워킹': 'C',
        '보안': 'A+', '해킹': 'F', '시스템': 'C+'}

print(mids)

# 회원정보를 dict로 선언
# key : 이름, 아이디, 비번, 이메일, 주소, 성적(국영수)
member = {'name': '김이름', 'userid': 'name',
          'passwd': 'dkagh', 'email': 'name@gmail.com',
          'address': '지구', 'sungjuk': [70, 59, 97]}

print(member)


# 딕셔너리 다루기
# 조회 : 변수명[키], 변수명..get(키)
print(member['name'])
print(member['userid'])
print(member['sungjuk'])     #국어
print(member['sungjuk'][0])     #국어

print(member.get('name'))
print(member.get('userid'))
print(member.get('sungjuk'))
print(member.get('sungjuk')[1])

## 존재하지 않는 키 지정 시
member['zipcode']         # 오류
member.get('zipcode')     #None (값이 없어서 실행해도 변화없음)


# 새 항목 추가 : 변수명[새로운키] = 새로운값
member['zipcode'] = '12345'
print(member)


# 기존 항목 변경: 변수명[키] = 변경할값
member['zipcode'] = '98765'
member['address'] = '서울시 광진구 자양동'
print(member)

# 기존 항목 삭제: del 변수명[키], 변수명.pop(키)
del member['zipcode']
member.pop('address')
print(member)
##존재하지 않는 키 삭제 시
del member['blood']         # 오류발생
member.pop('blood')     # 오류발생
member.pop('blood', None)     # None

# 항목 수 조회: len
print(len(member))

# dict의 모든 키/값 조회 : keys, values
print(member.keys())
print(member.values())

# dict 전체 항목 출력
# 출력 형식은 '키 = 값'
for key in member.keys():
    print(f'{key} = {member[key]}')



# 예제 -중간고사성적관리 (24 - 33p)
#1
scores = {'C/C++': 'A', 'Java': 'B+', '모바일': 'C',
        '보안': 'A+', '해킹': 'F', '시스템': 'C+'}
#2
print(scores['Java'], scores['시스템'])
#3
scores['파이썬'] = 'A'
scores['OS'] = 'A'
print(scores)
#4
scores['Java'] = 'A'
scores['시스템'] = 'A'
#5
for key in scores.keys():
    print(f'{key} = {scores[key]}')



# 예제 -채점프로그램 (24 - 37p)
que = ('3+2', '5/2의 몫', '10-2', '10^2*2', '1-(10/4의 나머지)', '2^4', '4/2')
ans = (5, 2, 8, 200, -1, 16, 2)

totScor = 0
cor = 0
err = 0

for i in range(0, 7):
    print(f'문제: {que[i]}')
    usrAns = int(input('정답을 입력하세요.'))
    if i in (1, 3, 4):
        if usrAns == ans[i]:
            scor += 5
            cor +=1
    elif usrAns == ans[i]:
        scor += 3
        cor +=1
    else:
        err += 1

print(f'''
------------------------
정답 개수: {cor}
오답 개수: {err}
Total score: {totScor}
------------------------
''')


#해설
quizs = (('3 + 2 (3점)', 5, 3), ('5 ÷ 2의 몫 (5점)', 2, 5), ('10-2 (3점)', 8, 3),
         ('10^2*2 (5점)', 200, 5), ('1-(10 ÷ 4의 나머지) (5점)', -1, 5), ('2^4 (3점)', 16, 3),
         ('4 ÷ 2 (3점)', 2, 3))

trueCount = 0
falseCount = 0
totalscore = 0

for idx, q in enumerate(quizs):                  #문제 답 입력
    print(f'문제 {idx+1}/7: ', q[0])
    answer = int(input('정답을 입력하세요.'))

    if answer == q[1]:                           # 채점
        trueCount += 1
        totalscore += q[2]
    else: falseCount += 1


print(f'''
------------------------
정답 개수: {trueCount}
오답 개수: {falseCount}
Total score: {totalscore}
------------------------
''')





# 예제 -회원가입프로그램 V1  (24 - 38p)
users = {}

while True:
    menu = input('1. 회원가입, 2. 프로그램 종료')
    if menu == '1':
        userid = input('아이디를 입력하세요.')
        passwd = input('암호를 입력하세요.')
        users[userid] = passwd
    elif menu == '2':
        print('-----------')
        print('아이디 : 암호')
        print('-----------')
        for k in users.keys():
            print(f'{k} : {users[k]}')
        print('-----------')
        break
    else:
        print('잘못 입력하셨습니다.')


## 회원가입프로그램 V2
users = {'response': {'body': {'totalCount': 999, 'items': []}}}

print(users['response']['body']['totalCoount'])
print(users['response']['body']['items'])        #딕셔너리 중첩시 [] 여러번으로 값 출력한다.


###두명의 회원정보 키값 뽑아서 밸류 조회
print(users['response']['body']['items'].append({'uid':'abc', 'pwd':'123'}))
print(users['response']['body']['items'].append({'uid':'xyz', 'pwd':'987'}))
print(users['response']['body']['items'])

for item in users ['response']['body']['items']:
    for key in item.keys():
        Print(key, item[key])



while True:
    menu = input('1. 회원가입, 2. 프로그램 종료')

    if menu == '1':
        userid = input('아이디를 입력하세요.')
        passwd = input('암호를 입력하세요.')
        user = {}
        user['userid'] = userid
        user['passwd'] = passwd
        users['response']['body']['items'].append(user)
    elif menu == '2':
        print('-----------')
        print('아이디 : 암호')
        print('-----------')
        for item in users['response']['body']['items']:
            for k in item.keys():
                print(f'{k} : {item[k]}')

        print('-----------')
        break
    else:
        print('잘못 입력하셨습니다.')





