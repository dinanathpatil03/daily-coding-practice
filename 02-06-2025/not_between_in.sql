
select * from dbo.EmployeeRecords

select * from dbo.EmployeeRecords
where not FirstName = 'John' and not Salary = 60000

select * from dbo.EmployeeRecords
where not LastName = 'Miller' or not Department = 'HR'



select * from dbo.EmployeeRecords
where Salary between 70000 and 80000

select * from dbo.EmployeeRecords
where Salary>=75000 and Salary<=85000

select * from dbo.EmployeeRecords
where salary not between  70000 and 85000

select * from dbo.EmployeeRecords
where not salary between  70000 and 85000

select * from dbo.EmployeeRecords
where Department in ('HR', 'IT')

select * from dbo.EmployeeRecords
where Department not in ('HR', 'IT')

select * from EmployeeRecords
where not Department in ('HR', 'IT')
