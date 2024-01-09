# 성적처리 프로그램 7
# 1. 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균, 학점 계산 및 출력
# 학점 기준  : 수우미양가
# 성적 입력, 조회, 상세조회, 수정, 삭제 기능 구현
# 각 가능은 메뉴식으로 구현 - 기능별 메뉴 선택 시 명령 수행
# 성적 데이터는 데이터베이스 테이블에 저장

import varies8.sjv7 as sjv7


while True:
    # 프로그램 주 실행부
    menu = sjv7.show_menu()

    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1': sjv7.addsungjuk()
    elif menu == '2': sjv7.show_sungjuk()
    elif menu == '3': sjv7.showone_sungjuk()
    elif menu == '4': sjv7.modify_sungjuk()
    elif menu == '5': sjv7.remove_sungjuk()
    elif menu == '0': sjv7.exit_program()
    else:
        print('메뉴를 잘못 선택하셨습니다.')










# # 성적 데이터 입력
#
# name = input('이름: ')
# kor = int(input('국어: '))
# eng = int(input('영어: '))
# math = int(input('수학: '))
#
#
# names.append(name)
# kors.append(kor)
# engs.append(eng)
# maths.append(math)
#
#
#
#
# # 성적처리
# for i in range(len(names)):
#     tots.append(kors[i] + engs[i] + maths[i])
#     avgs.append(tots[i] / 3)
#     avg = avgs[len(avgs)-1]
#     grd = '수' if avg >= 90 else \
#            '우' if avg >= 80 else \
#            '미' if avg >= 70 else \
#            '양' if avg >= 60 else '가'
#
#
#
#     # 결과출력     - 소수점반올림 .nf (소수점자리수 n)
# for i in range(len(names)):
#     print(f'이름: {names[i]:s}, 국어: {kors[i]}, 영어: {engs[i]}, 수학: {maths[i]}')
#     print(f'총점{tots[i]:d}, 평균{avgs[i]:.1f}, 학점{grds[i]}')





















