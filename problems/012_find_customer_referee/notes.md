# 012 - Find Customer Referee

## Problem
Find customers not referred by id=2. Include customers with no referee (NULL).

## Key Concepts
- NULL handling is the core challenge: `!= 2` does NOT capture NULL rows in SQL or pandas.
- Must explicitly include NaN rows with `| isna()`.
- In pandas, `NaN != 2` evaluates to `False` (not True), so those rows get dropped unless you add the isna check.

## Key Rule
Whenever filtering with !=, always ask: should NULL/NaN rows be included? If yes, add `| isna()`.
