# 013 - Customer Placing Largest Orders

## Problem
Find the customer who has placed the most orders.

## Key Concepts
- `groupby + size()` counts orders per customer.
- Find the max count, then filter for customers matching it (handles ties gracefully).
- SQL uses `ORDER BY COUNT(*) DESC LIMIT 1` — but this doesn't handle ties.

## Tie Handling
The pandas approach using `== max_count` returns all tied customers.
The SQL LIMIT 1 approach returns only one — choose based on problem requirements.
