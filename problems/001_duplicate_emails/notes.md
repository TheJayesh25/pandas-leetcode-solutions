# 004 - Duplicate Emails

## Problem
Return all email addresses that appear more than once in the `Person` table.

## Primary Pandas Solution
- `groupby("email").size()` counts how many times each email appears — equivalent to SQL's `GROUP BY + COUNT`.
- `.reset_index(name="count")` flattens the result back into a DataFrame with a named count column.
- Filter for `count > 1` to keep only duplicates, then return just the `email` column.

## SQL Solution
- `GROUP BY email` collapses rows by email.
- `HAVING COUNT(email) > 1` filters groups after aggregation — `HAVING` is the post-aggregation equivalent of `WHERE`.

## Alt Pandas Solution
- `duplicated("email", keep=False)` marks **every** row as `True` if its email appears more than once — both/all copies get flagged, not just the second occurrence.
- Filtering on that boolean mask gives all the duplicate rows, then `.drop_duplicates()` reduces them back to one row per email.
- The key difference from `keep="first"` or `keep="last"`: `keep=False` flags all occurrences, making it easy to retrieve the duplicate rows themselves rather than just counts.

## Key Distinction Between Approaches
| Approach | Mental model | Best when |
|---|---|---|
| `groupby + size` | Count occurrences, filter by count | You need the count value itself |
| `duplicated(keep=False)` | Flag rows that are duplicates | You need the actual duplicate rows |

## Gotcha
- `duplicated()` with default `keep="first"` marks only the *second and beyond* occurrences as `True` — the first copy is kept as `False`. Always use `keep=False` when you want to flag all copies of a duplicate.
