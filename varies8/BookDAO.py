import varies8.dbinfo2 as dbinfo

insertsql = ' insert into book (bkname, author, pubilisher, pubdate, retail, '\
             ' price, pctoff,mileage) values (%s,%s,%s,%s,%s,%s,%s,%s) '

selectsql = ' select bkno, bkname, author, pubilisher, price from book '

selectonesql = ' select * from book where bkname = %s '

updatesql =  'update book set bkname=%s, author=%s, publisher=%s,  '\
             ' pubdate=%s, retail=%s, price=%s, pctoff=%s, mileage=%s '\
             ' regdate=current_timestamp where bkno =%s '

deletesql = 'delete from book where bkno = %s '


class BookDAO:
    @staticmethod
    def insert_book(bk):
        cursor, conn = dbinfo.openConn()
        params = [bk.bkname, bk.author, bk.pubilisher, bk.pubdate,
                  int(bk.retail), int(bk.price), int(bk.pctoff), int(bk.milege)]

        cursor.execute(insertsql, params)
        conn.commit()
        rowcnt = cursor.rowcount

        dbinfo.closeConn(cursor, conn)
        return rowcnt


    @staticmethod
    def select_book():
        cursor, conn = dbinfo.openConn()

        cursor.execute(selectsql)
        rows = cursor.fetchall()

        dbinfo.closeConn(cursor, conn)
        return rows



    @staticmethod
    def selectone_book(bkname):
        cursor, conn = dbinfo.openConn()

        cursor.execute(selectonesql, [bkname])
        row = cursor.fetchone()

        dbinfo.closeConn(cursor, conn)
        return row



    @staticmethod
    def update_book(bk):
        cursor, conn = dbinfo.openConn()

        params = [bk.bkname, bk.author, bk.pubilisher, bk.pubdate,
                  int(bk.retail), int(bk.price), int(bk.pctoff), int(bk.milege),
                  bk.bkno]
        cursor.execute(updatesql, params)
        conn.commit()

        dbinfo.closeConn(cursor, conn)
        return rowcnt


    @staticmethod
    def delelte_book(bkno):
        cursor, conn = dbinfo.openConn()
        cursor.execute(deletesql, [bkno])
        conn.commit()
        rowcnt = cursor.rowcount

        dbinfo.closeConn(cursor, conn)
        return rowcnt


