# 성적처리 프로그램 V2b
# 1. 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균, 학점 계산 및 출력
# 학점 기준  : 수우미양가



# 3. 데이터 입력시 input함수 이용
# 입력 데이터 선언
names = []
kors = []
engs = []
maths = []
tots = []
avgs = []
grds = []



# 성적 데이터 입력

name = input('이름: ')
kor = int(input('국어: '))
eng = int(input('영어: '))
math = int(input('수학: '))


names.append(name)
kors.append(kor)
engs.append(eng)
maths.append(math)


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
    avg = avgs[len(avgs)-1]
    grd = '수' if avg >= 90 else \
           '우' if avg >= 80 else \
           '미' if avg >= 70 else \
           '양' if avg >= 60 else '가'



    # 결과출력     - 소수점반올림 .nf (소수점자리수 n)
for i in range(len(names)):
    print(f'이름: {names[i]:s}, 국어: {kors[i]}, 영어: {engs[i]}, 수학: {maths[i]}')
    print(f'총점{tots[i]:d}, 평균{avgs[i]:.1f}, 학점{grds[i]}')





















