# Write your MySQL query statement below
select T.ID, case when T.P_ID is null then "Root" when T.ID in (select distinct T.P_ID M from TREE T) then "Inner" else "Leaf" end TYPE from TREE T