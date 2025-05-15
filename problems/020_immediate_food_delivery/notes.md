# 020 - Immediate Food Delivery II

## Problem
Calculate the percentage of first orders that were immediate (same-day delivery preference).

## Key Concepts
- First, identify each customer's earliest order using `groupby + min()`.
- Merge back to get only the first-order rows.
- Among those, count how many have `order_date == customer_pref_delivery_date`.
- Divide and multiply by 100, round to 2 decimals.

## Pattern
"First order per customer" = groupby customer + min(order_date), then join back.
