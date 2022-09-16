# Write your MySQL query statement below
select W1.id from Weather W1, Weather W2 where DATEDIFF(w1.recordDate, w2.recordDate) = 1 and W1.temperature > W2.temperature