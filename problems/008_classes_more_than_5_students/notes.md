# 008 - Classes More Than 5 Students

## Problem
Find classes with 5 or more students.

## Key Concepts
- `groupby + count()` is the pandas equivalent of SQL's GROUP BY + HAVING COUNT.
- Filter after aggregation (not before) — like HAVING vs WHERE.
- `count()` ignores NaN, `size()` counts all rows including NaN.
