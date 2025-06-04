

-- sum function
select * from dbo.Sales

select sum(quantity) [Sum of Quantity] from dbo.Sales

select sum(quantity) [Total quantity], sum(totalamount) [Sum of amount] from dbo.Sales

-- average function

select avg(quantity) [Average Quantity] from dbo.Sales

select avg(quantity) [Average Quantity], avg(totalamount) [Average Total Amount] from dbo.Sales

-- In the output we want sum of quantity, sum of total amount, average of quantity and average of total amount for each distitnct product

select
ProductID,
sum(Quantity) as [Sum of Quantity],
sum(TotalAmount) as [Sum of Amount],
avg(Quantity) as [Avg of quantity],
avg(TotalAmount) as [Avg of Total amount]
from dbo.Sales
group by ProductID

select * from dbo.Sales

-- sum of quamtity, sum of amount, avg of quantity, avg of amount for distinct combinations of productid and storeid

select
ProductID, 
StoreID,
sum(quantity) [Sum of Quantity],
sum(TotalAmount) [Sum of amount],
avg(Quantity) [Average of Quantity],
avg(TotalAmount) [Average of amount]
from dbo.Sales
group by ProductID, StoreID

-- count function

select * from dbo.Sales

select COUNT(*) [Number of rows] from dbo.Sales

select count(paymentmethod) [Number of Payment method] from dbo.Sales

select count(distinct productid) [No of ids] from dbo.Sales

select paymentmethod, count(distinct PaymentMethod) [No of payment] from dbo.Sales
group by PaymentMethod

select paymentmethod, count(PaymentMethod) [No of payment] from dbo.Sales
group by PaymentMethod

select paymentmethod, count(*) [No of payment] from dbo.Sales
group by PaymentMethod





