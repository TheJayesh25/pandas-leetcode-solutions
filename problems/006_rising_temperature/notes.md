# 006 - Rising Temperature

## Problem
Find IDs where today's temperature is greater than yesterday's, and dates are consecutive.

## Key Concepts
- Sort by date first, then use `shift(1)` to bring the previous row's values alongside the current.
- Check BOTH that temperature increased AND that dates are exactly 1 day apart (no gaps).
- `pd.Timedelta(days=1)` is how you compare date differences in pandas.

## Gotcha
Don't forget the consecutive-day check — data may have missing dates, so a simple shift isn't enough.
