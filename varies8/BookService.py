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
    retail = int(input('정가 : '))
    pctoff = int(input('할인율 : '))

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
    print(bk)

    rowcount = BookDAO.insert_book(bk)
    print(f'{rowcount}건의 도서데이터가 추가됨.')





# 모든 도서 데이터 출력
def read_book():
    """
    도서조회 - 모든 도서 데이터 출력(번호/도서명/저자/출판사/판매가)
    :return: 없음
    """
    print('도서데이터 조회')
    result = ''

    rows = BookDAO.select_book()
    for row in rows:
        result += f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]:,}\n'

    print(result)



#도서 상세조회
def readone_book():
    """
    도서데이터 상세조회
    :return: 없음
    """
    bkname = input('상세 조회할 도서명 : ')

    row = BookDAO.selectone_book(bkname)
    if row:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} '
              f'{row[5]:,} {row[6]:,} {row[7]}% {row[8]:,} {row[9]}')
    else:
        print('데이터가 없습니다.')


# 도서 데이터 추가 (입력-처리-저장)
def reinput_book(obk):
    bkname = input(f'도서명 : {obk[1]}')
    author = input(f'저자 : {obk[2]}')
    pubilisher = input(f'출판사 : {obk[3]}')
    pubdate = input(f'출간일 : {obk[4]}')
    retail = int(input(f'정가 : {obk[5]}'))
    pctoff = int(input(f'할인율 : {obk[7]}'))

    bk = Book(bkname, author, pubilisher, pubdate, retail, pctoff)

    bk.price = bk.retail * (1 - (bk.pctoff / 100))
    bk.milege = bk.retail * (bk.pctoff / 100)
    bk.bkno = obk[0]

    return bk



# 도서데이터 수정
def modify_book():
    """
    도서데이터 수정
    :return:
    """
    bkname = input('수정할 도서명: ')
    # 튜플객체를 수정하기 위해 리스트객체로 변환
    row = BookDAO.selectone_book(bkname)
    if row:
        bk = reinput_book(row)
        rowcnt = BookDAO.update_book(bk)
        print(f'{rowcnt} 건의 데이터가 수정되었습니다.')
    else:
        print('수정할 데이터가 존재하지 않습니다.')



# 도서데이터 삭제
def remove_book():
    """
    도서데이터 삭제
    :return:
    """
    bkno = input('삭제할 도서 번호: ')

    rowcount = BookDAO.delete_book(bkno)
    print(f'{rowcount}건의 도서데이터가 추가됨.')



# 도서프로그램 종료
def exit_program():
    """
    도서처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """
    print('프로그램 종료')
    sys.exit(0)
