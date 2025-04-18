-- SQL solution
-- Problem: Combine Two Tables
-- Use LEFT JOIN to keep all persons even if they have no matching address.

SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;