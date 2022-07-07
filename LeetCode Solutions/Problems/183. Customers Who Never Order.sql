# Write your MySQL query statement below
SELECT Name AS Customers
FROM Customers
WHERE Id NOT IN (SELECT Customers.Id FROM Orders WHERE Orders.CustomerId = Customers.Id);