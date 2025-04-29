# 015 - Article Views I

## Problem
Find authors who have viewed their own articles (author_id == viewer_id).

## Key Concepts
- Direct column comparison within the same row: `df["col_a"] == df["col_b"]`.
- `drop_duplicates()` ensures each author appears once.
- `sort_values` matches the expected output ordering.
