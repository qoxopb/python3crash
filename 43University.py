
# (자바기초.docx)
# 76 77번




#76
class Student:
    def __init__(self, hakbun, name, addr, birth, dept, prof):
        self.hakbun = hakbun
        self.name = name
        self.addr = addr
        self.birth = birth
        self.dept = dept
        self.prof = prof
    def __str__(self):
        info = f'{self.hakbun} {self.name} {self.addr} {self.birth} '\
               f'{self.dept} {self.prof} '
        return info


class Professor:
    def __init__(self, name, major, tech, dept):
        self.name = name
        self.major = major
        self.tech = tech
        self.dept = dept
    def __str__(self):
        info = f'{self.name} {self.major} {self.tech} {self.dept}'
        return info


class Subject:
    def __init__(self, sjno, sjname, sjdesc, sjsect, sjprof):
        self.sjno = sjno
        self.sjname = sjname
        self.sjdesc = sjdesc
        self.sjsect = sjsect
        self.sjprof = sjprof
    def __str__(self):
        info = f'{self.sjno} {self.sjname} {self.sjdesc} {self.sjsect} {self.sjprof}'
        return info


class Department:
    def __init__(self, dname, phone, dpos, chief):
        self.dname = dname
        self.phone = phone
        self.dpos = dpos
        self.chief = chief
    def __str__(self):
        info = f'{self.dname} {self.phone} {self.dpos} {self.chief}'
        return info



tahee = Student(201526304, '김태희', '경기 고양','1986,12,30', '컴퓨터', 504)
print(tahee)

tahee.addr = '서울 관악'    # 항목 변경
print(tahee)

lee = Professor('이순신','프로그래밍', '[자바, 파이썬]', '컴퓨터')
print(lee)

programming = Subject('0205','프로그래밍', '자바', '컴퓨터', 301)
print(programming)


computer = Department('컴퓨터공학','123-456-7890', 'E동 2층', 504)
print(computer)


# 77
class Book:
    def __init__(self, bookno, bookname, publish, author, price, isborrowed):
        self.bookno = bookno
        self.bookname = bookname
        self.publish = publish
        self.author = author
        self.price = price
        self.isborrowed = isborrowed


class Member:
    def __init__(self, memno, memname, memph, memlct, borrowing, coin):
        self.memno = memno
        self.memname = memname
        self.memph = memph
        self.memlct = memlct
        self.borrowing = borrowing
        self.coin = coin


class Employee:
    def __init__(self, empno, empname, emplct, empph, emp_passwd, hour_login, hour_logout):
        self.empno = empno
        self.empname = empname
        self.emplct = emplct
        self.empph = empph
        self.emp_passwd = emp_passwd
        self.hour_login = hour_login
        self.hour_logout = hour_logout
















































