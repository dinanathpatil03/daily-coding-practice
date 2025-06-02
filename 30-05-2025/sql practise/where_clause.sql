
select * from [dbo].[EmployeeRecords]
where EmployeeID = 2

select EmployeeID, FirstName from EmployeeRecords
where EmployeeID = 2

select * from EmployeeRecords
where Salary >= 70000

select FirstName, LastName, Department, Salary from EmployeeRecords
where Salary < 70000

select distinct FirstName, LastName, Department, Salary from EmployeeRecords
where Salary < 75000