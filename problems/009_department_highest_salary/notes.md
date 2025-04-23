# 009 - Department Highest Salary

## Problem
Return employees who earn the maximum salary within their department.

## Key Concepts
- `transform("max")` broadcasts the group max back to every row — allows row-level comparison without losing original row structure.
- This is more elegant than merge + filter because it stays in one DataFrame.
- Join with Department table afterwards to get department names.

## transform vs agg
- `agg` collapses groups into one row per group.
- `transform` returns a Series the same length as the original — ideal for row-level filtering.
