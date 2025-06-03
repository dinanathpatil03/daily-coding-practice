

select * from dbo.Sales

select max(TotalAmount) [Maximum Amount] from dbo.Sales

select max(saledate) [Max Sale Date] from dbo.Sales

select max(paymentmethod) [Max Pay method] from dbo.Sales

-- Maximum Quantity sold for each productID
select productID, max(quantity) [Maximum Quantity] from dbo.Sales
group by PRODUCTID

select * from dbo.Sales

-- Maximum total amount for all distinct dates in saledate column
select distinct saledate, max(totalamount) [Maximum Total Amount] from dbo.Sales
group by SaleDate


-- Min functionality

select * from dbo.Sales

select min(quantity) [Minimum Quantity] from dbo.Sales

select min(saledate) [Minimum Date] from dbo.Sales

select min(paymentmethod) [Minimum Payment method] from dbo.Sales

-- Show minimum total amount for each store id
select storeid, min(totalamount) [Minimum total amount] from dbo.Sales
group by StoreID







