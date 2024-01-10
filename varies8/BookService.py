import sys
from varies8.Book import Book
from varies8.BookDAO import BookDAO



# 메뉴 출력
def show_menu():
    """
    메뉴 선택 출력 함수
    :return: 입력받은 메뉴번호
    """
    main_menu = '''
    -----------------------
    도서 관리 프로그램 V1
    -----------------------
    1. 도서 데이터 추가
    2. 도서 데이터 조회
    3. 도서 데이터 상세조회
    4. 도서 데이터 수정
    5. 도서 데이터 삭제
    0. 프로그램 종료
    -----------------------
    '''
    print(main_menu, end='')
    menu = input('=>메뉴를 선택하세요: ')
    return menu



# 도서 데이터 추가 (입력-처리-저장)
def input_book():
    bkname = input('도서명 : ')
    author = input('저자 : ')
    pubilisher = input('출판사 : ')
    pubdate = input('출간일 : ')
    retail = input('정가 : ')
    pctoff = input('할인율 : ')

    bk = Book(bkname, author, pubilisher, pubdate, retail, pctoff)
    bk.price = bk.retail * (1 - (bk.pctoff / 100))
    bk.milege = bk.retail * (bk.pctoff / 100)

    return bk


def new_book():
    """
    새로운 도서 데이터 추가 (입력 처리 저장)
    :return: 없음
    """
    print('도서데이터 추가')
    bk = input_book()

    rowcount = BookDAO.insert_book(bk)
    print(f'{rowcount}건의 도서데이터가 추가됨.')





# 모든 도서 데이터 출력
def read_book():
    """
    도서조회 - 모든 도서 데이터 출력(번호/도서명/저자/출판사/판매가)
    :return: 없음
    """
    print('도서데이터 조회')
    rows = BookDAO.select_book()
    for row in rows:
        print(f'{row[0]} {row[1][:10]} {row[2]} {row[3]} {str(row[4])}')


#도서 상세조회
def readone_book():
    """
    도서데이터 상세조회
    :return: 없음
    """
    bkno = input('상세 조회할 도서명 : ')

    row = BookDAO.selectone_book(bkno)

    print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]}')

    info = '찾는 데이터가 없습니다.'




# 도서데이터 수정
def modify_book():
    """
    도서데이터 수정
    :return:
    """
    bkno = input('수정할 도서 번호: ')
    # 튜플객체를 수정하기 위해 리스트객체로 변환
    bk = list(BookDAO.selectone_book(bkno))

    if bk[0]: # 만일, 수정데이터가 존재한다면
        bk[1] = (input(f'새 이름: {bk[1]}) : '))
        bk[2] = int(input(f'새 국어 점수: (기존점수:{bk[2]}) : '))
        bk[3] = int(input(f'새 영어 점수: (기존점수:{bk[3]}) : '))
        bk[4] = int(input(f'새 수학 점수: (기존점수:{bk[4]}) : '))
        # 조회한 결과를 클래스 타입으로 변경 후 다시 도서처리
        bk = Book(bk[1], bk[2], bk[3], bk[4])
        BookService.compute_sunjuk(bk)

        rowcnt = BookDAO.update_book(bk, bkno)
        print(f'{rowcnt} 건의 데이터가 수정되었습니다.')


    else:
        print('데이터가 존재하지 않습니다.')



# 도서데이터 삭제
def remove_book():
    """
    도서데이터 삭제
    :return:
    """
    bkno = input('삭제할 도서 번호: ')
    rowcnt = BookDAO.delete_book(bkno)
    print(f'{rowcnt} 건의 데이터가 삭제되었습니다.')




# 도서프로그램 종료
def exit_program():
    """
    도서처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """
    print('프로그램 종료')
    sys.exit(0)
