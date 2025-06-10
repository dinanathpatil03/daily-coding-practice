

select * from table1

select * from table1 as a inner join table1 as b
on a.c1 = b.c1

select * from table1 as a left join table1 as b
on a.c1 = b.c1

select * from table1 as a join table1 as b
on a.c1 = b.c1

select a.c1, b.c2 from table1 as a join table1 as b
on a.c1 = b.c1