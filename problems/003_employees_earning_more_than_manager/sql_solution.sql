-- SQL solution
-- Problem: Employees Earning More Than Their Manager

SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
