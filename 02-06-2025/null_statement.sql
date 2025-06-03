

select * from dbo.Employees

insert into dbo.Employees
values (9, 'Mahesh', '', 'IT', 130000, '2025-05-03')

insert into dbo.Employees
values (10, 'Yash', 'Khanekar', 'Sales', '0', '2025-04-03')

select * from dbo.Employees where Department = null

select * from dbo.Employees where Department is null

select * from dbo.Employees where Department is not null