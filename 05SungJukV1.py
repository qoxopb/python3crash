# 성적처리 프로그램 V1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균 계산 및 출력
name = '김철수'
kor = 60
eng = 90
math = 80

# 성적처리
tot = kor + eng + math
avg = tot / 3

# 결과출력      - 소수점반올림 .nf (소수점자리수 n)
print(f'이름: {name:s}, 국어: {kor}, 영어: {eng}, 수학: {math}')
print(f'총점{tot:d}, 평균{avg:.1f}')
