

select * from dbo.Employees

select * into #item from dbo.Employees

select * from #item

update #item
set Department = 'coding'
where Department is null

update #item
set Salary = 89000, HireDate = '2025-01-01'
where EmployeeID = 7

select * into #item1 from dbo.Employees

select * from #item1

update #item1
set Department = 'finance'





