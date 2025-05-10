# 019 - Customer Order Frequency

## Problem
Find customers who spent at least $100 in BOTH June and July 2020.

## Key Concepts
- Compute `amount = quantity * price` after joining Orders with Product.
- Split into month groups, then aggregate spend per customer per month.
- Use `index.intersection()` to find customers present in both months, then filter by amount.

## SQL CASE WHEN
SQL uses conditional aggregation (CASE WHEN inside SUM) to compute per-month totals in a single GROUP BY pass.
