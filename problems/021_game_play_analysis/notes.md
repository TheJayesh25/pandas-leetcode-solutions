# 021 - Game Play Analysis IV

## Problem
What fraction of players logged in the day after their very first login?

## Key Concepts
- Find each player's first login date.
- Compute first_date + 1 day as the "next day".
- Check if an activity record exists for that next day.
- Fraction = players who returned next day / total players.

## Note
Denominator is ALL players (from first_login), not just those who returned.
