# Write your MySQL query statement below
select Name as Customers from Customers where Id not in (select Customers.Id from Orders where Orders.CustomerId = Customers.Id);