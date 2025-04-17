# 003 - Employees Earning More Than Their Manager

## Problem
Find all employees whose salary exceeds their direct manager's salary.

## Key Concepts
- Self-join on the same `Employee` table: join employee to manager via `managerId = id`.
- Use `suffixes=("_emp", "_mgr")` to differentiate columns after the merge.
- Filter rows where `salary_emp > salary_mgr`.

## Pattern
Self-joins are a classic SQL/pandas pattern for hierarchical data (employees, org trees).
Always alias clearly when self-joining to avoid confusion.
