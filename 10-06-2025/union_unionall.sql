

select * from append1

select * from append2

select * from append1
union all
select * from append2

select * from append1
union 
select * from append2

-- Number of column present in select list have to be same
-- Data types of columns have to be same
-- Order in which column have return have to be same 

select c1, c2, c3 from append1 -- c1 int, c2 nvarchar, c3 int
union 
select c1, c3, c2 from append2

-- Alias names which are specified in 1st select statement will be assigned to columns

select c1 [Column1], c2 [Column2], c3 [Column3] from append1 
union 
select c1 [Col1], c2 [Col2], c3 [Col3] from append2