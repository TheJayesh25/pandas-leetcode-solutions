# 016 - User Activity for the Past 30 Days

## Problem
Count distinct active users per day in a 30-day window ending 2019-07-27.

## Key Concepts
- Date window: from (end - 29 days) to end date, inclusive = 30 days.
- `nunique()` counts distinct users per day.
- Convert to datetime with `pd.to_datetime()` before date arithmetic.

## Gotcha
The window is 30 days inclusive: July 27 back to June 28. "Past 30 days" means 29 days before the end date + the end date itself.
