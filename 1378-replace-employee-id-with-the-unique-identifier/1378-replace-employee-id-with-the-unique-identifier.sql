# Write your MySQL query statement below
select empuni.unique_id,e.name from Employees e left join EmployeeUNI empuni on e.id=empuni.id