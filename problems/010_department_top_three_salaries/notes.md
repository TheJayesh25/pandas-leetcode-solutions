# 010 - Department Top Three Salaries

## Problem
Return all employees earning one of the top 3 distinct salaries per department.

## Key Concepts
- "Top 3 distinct" means use dense rank (no gaps for ties).
- Alt approach: `groupby + rank(method="dense")` is clean and readable.
- Primary approach: `groupby + apply` with a custom function using `nlargest`.

## Dense Rank
- "dense" rank: 1, 2, 2, 3 (no gap after tie)
- "min" rank: 1, 2, 2, 4 (gap after tie)
- For "top N distinct values", always use dense rank.
