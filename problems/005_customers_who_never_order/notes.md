# 005 - Customers Who Never Order

## Problem
Find customers with no orders — an anti-join pattern.

## Key Concepts
- `~isin()` is the pandas equivalent of SQL's NOT IN.
- Alt: LEFT JOIN + filter for NaN in the right-table column — the classic anti-join pattern.

## Anti-Join Pattern
Left join keeps all left rows; where right side is NaN means no match was found.
This is equivalent to NOT EXISTS or NOT IN in SQL.
