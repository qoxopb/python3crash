import varies8.dbinfo2 as dbinfo

insertsql = ' insert into book (bkname, author, pubilisher, pubdate, retail, '\
             ' price, pctoff,mileage) values (%s,%s,%s,%s,%s,%s,%s,%s) '

selectsql = ' select bkno, bkname, author, pubilisher, price from book '

selectonesql = ' select * from book where bkno = %s '

updatesql =  'update book set bkname = %s, author = %s, publisher = %s,  '\
             ' pubdate = %s, retail = %s, pctoff = %s '\
             ' where bkno = %s '

deletesql = ' delete book wher bkno = %s '


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
    def update_book(self):
        pass


    @staticmethod
    def delelte_book(self):
        pass

