# 성적처리 프로그램 V2b
# 1. 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균 계산 및 출력
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함
# 2. 반복문을 이용하면 코드를 간단히 작성 가능!
names = ['김일번', '김이번', '김삼번']
kors = [98, 76, 50]
engs = [67, 84, 91]
maths = [91, 85, 75]
tots = []
avgs = []

# 성적처리
for i in range(len(names)):
    tots.append(kors[i] + engs[i] + maths[i])
    avgs.append(tots[i] / 3)

# 결과출력     - 소수점반올림 .nf (소수점자리수 n)
for i in range(len(names)):
    print(f'이름: {names[i]:s}, 국어: {kors[i]}, 영어: {engs[i]}, 수학: {maths[i]}')
    print(f'총점{tots[i]:d}, 평균{avgs[i]:.1f}')





# 3. 데이터 입력시 input함수 이용
# 입력 데이터 선언
names = []
kors = []
engs = []
maths = []
tots = []
avgs = []

# 성적 데이터 입력
for i in range(3):
    print(f'{i+1}번째 학생데이터 입력')
    names.append(input('이름: '))
    kors.append(int(input('국어: ')))
    engs.append(int(input('영어: ')))
    maths.append(int(input('수학: ')))


# 성적처리
for i in range(len(names)):
    tots.append(kors[i] + engs[i] + maths[i])
    avgs.append(tots[i] / 3)

# 결과출력     - 소수점반올림 .nf (소수점자리수 n)
for i in range(len(names)):
    print(f'이름: {names[i]:s}, 국어: {kors[i]}, 영어: {engs[i]}, 수학: {maths[i]}')
    print(f'총점{tots[i]:d}, 평균{avgs[i]:.1f}')





















