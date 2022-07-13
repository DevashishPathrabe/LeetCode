# Write your MySQL query statement below
select name as NAME, sum(t.amount) as BALANCE from Users u join Transactions t on u.account = t.account group by u.account having BALANCE > 10000;