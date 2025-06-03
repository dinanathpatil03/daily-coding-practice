

select * from dbo.Employees

insert into dbo.Employees (EmployeeID, FirstName, LastName, Department, Salary, HireDate)
values (6, 'Dinanath', 'Patil', 'IT', 67000, '2025-06-02')

insert into dbo.Employees (EmployeeID, FirstName, LastName)
values (7, 'Aditi', 'Patil')

insert into dbo.Employees
values (8, 'Shreehari', 'Joshi', 'Training', 100000, '2025-06-05')

select * from INFORMATION_SCHEMA.COLUMNS
where TABLE_NAME = 'Employees'




