
 
select * from table1

select * from table2

select * from table1 right join table2 
on table1.c1 = table2.c1

select * from table1 right outer join table2 
on table1.c1 = table2.c1

select a.c1, a.c2, b.c3 from table1 a right join table2 b 
on a.c1 = b.c1

-- anti left join

select * from table1 left join table2 on table1.c1 = table2.c1

select * from table1 left join table2 on table1.c1 = table2.c1
where table2.c3 is null

-- anti right join

select * from table1 right join table2 on table1.c1 = table2.c1

select * from table1 right join table2 on table1.c1 = table2.c1
where table1.c2 is null



 
