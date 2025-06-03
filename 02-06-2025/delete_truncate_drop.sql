

select * from dbo.Employees

select * into #item2 from dbo.Employees

select * from #item2

delete from #item2
where LastName = '' or Salary = '0'

select * into #item3 from dbo.Employees

select * from #item3

delete from #item3

select * from #item2

truncate table #item2

drop table #item2

-- Delete - delete certain records from the table
-- if we use delete without where condition, all records from the table will deleted but the structure remains intact

-- Truncate - It will delete all the record from the table but the structure of the table remains intact

-- drop - all the records will be deleted plus the table structure will also be removed



