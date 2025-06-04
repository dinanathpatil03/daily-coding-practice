
select * from dbo.Sales

select paymentmethod, sum(totalamount) [Totol sales value] from dbo.Sales
group by PaymentMethod

select ProductID, PaymentMethod, sum(TotalAmount) [Sum of Amount] from dbo.Sales
group by ProductID, PaymentMethod

select ProductID, PaymentMethod, sum(TotalAmount) [Sum of Amount] from dbo.Sales
group by ProductID, PaymentMethod
order by ProductID asc


