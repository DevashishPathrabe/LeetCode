CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary from (SELECT Salary, DENSE_RANK() OVER(ORDER BY Salary DESC) as sal_rank from Employee) emp_sub where sal_rank = N
  );
END