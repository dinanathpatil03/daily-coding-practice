

select * from dbo.Sales

select * from dbo.Sales
where TotalAmount>=161

select productid, sum(totalamount) [Sum of sale] from dbo.Sales
group by ProductID 

select productid, sum(totalamount) [Sum of sale] from dbo.Sales
where TotalAmount>=161
group by ProductID
having sum(totalamount)>=250
order by ProductID desc

select productid, sum(totalamount) [Sum of sale] from dbo.Sales
where TotalAmount>=161
group by ProductID
having sum(totalamount)>=250
order by sum(totalamount)

