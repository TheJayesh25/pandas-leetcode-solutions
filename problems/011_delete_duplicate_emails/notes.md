# 011 - Delete Duplicate Emails

## Problem
Delete duplicate emails, keeping only the one with the lowest id.

## Key Concepts
- Sort by `id` ascending first so `keep="first"` retains the row with the smallest id.
- `drop_duplicates(subset=["email"], keep="first")` removes all but the first occurrence.
- In SQL, a self-join DELETE removes rows where a smaller id exists for the same email.

## Gotcha
Sorting before deduplication is critical — without it, "first" is arbitrary order.
