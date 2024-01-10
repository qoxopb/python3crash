create table book(
         bkno int auto_increment,
         bkname varchar(100)     not null,
         author varchar(100)     not null,
         pubilisher varchar(100) not null,
         pubdate datetime        not null,
         retail int              not null,
         price  int              default 0,
         pctoff int              not null,
         milege int              default 0,
         regdate datetime        default current_timestamp,
         primary key (bkno)
);

insert into book (bkname, author, pubilisher, pubdate, retail, pctoff)
values ('파이썬 기초', '한빛미디어', '한빛미디어', '2024-01-01 00:00:00', 35000, 10);


select bkno, bkname, author, price from book;

select * from book where bkno = 1;

update book set bkname = '', author = '', publisher = '',
                pubdate = '', retail = -1, pctoff = -1
where bkno = ?;

delete book wher bkno = ?;
