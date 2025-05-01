# 017 - Employee Bonus

## Problem
Return employees with bonus < 1000 or no bonus at all.

## Key Concepts
- LEFT JOIN preserves all employees even those without a bonus entry.
- NULL bonus rows must be explicitly included: `| isna()`.
- Same NULL-inclusion pattern as problem 012.

## Pattern
Left join + (condition OR isna) is a recurring pattern when NULLs should be included in results.
