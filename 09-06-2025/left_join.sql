

select * from table1

select * from table2

select * from table1 left join table2 on table1.c1 = table2.c1

select * from table1 left outer join table2 on table1.c1 = table2.c1

select a.c1, a.c2, b.c3 from table1 a left join table2 b 
on a.c1 = b.c1