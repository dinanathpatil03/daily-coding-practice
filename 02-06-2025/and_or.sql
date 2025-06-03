

select * from EmployeeRecords
where LastName = 'Miller' and EmployeeID = 1

select * from dbo.EmployeeRecords
where Department = 'HR' or Department = 'Finance'

select * from dbo.EmployeeRecords
where (Department = 'HR' or Department = 'Finance') and Salary = 60000