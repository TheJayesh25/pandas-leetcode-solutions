# 002 - Second Highest Salary

## Problem
Return the second highest distinct salary. Return null if it doesn't exist.

## Key Concepts
- `drop_duplicates()` ensures we're looking at distinct salaries before ranking.
- `nlargest(2)` gets the top 2 values; if fewer than 2 exist, return None.
- Wrapping the result in a DataFrame with explicit None handles the null-return edge case cleanly.

## Alt Approach
- `rank(method="dense")` assigns ranks without gaps — rank 2 is exactly the second highest.
- Dense rank is essential here vs "min" or "average" which behave differently with ties.

## Gotcha
- Always handle the edge case where there's only one unique salary — return null, not an error.
