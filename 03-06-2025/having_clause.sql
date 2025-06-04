

select * from dbo.Sales

-- total sales, average sales, total quantity and average quantity for each distinct product

select 
ProductID,
sum(totalamount) [Total amount],
avg(TotalAmount) [Average of amount],
sum(Quantity) [Sum of quantity],
avg(Quantity) [Average of quantity]
from dbo.Sales
group by ProductID
having sum(TotalAmount)<700 and sum(Quantity) = 21



