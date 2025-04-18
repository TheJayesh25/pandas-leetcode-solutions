# 001 - Combine Two Tables

## Problem
Report `firstName`, `lastName`, `city`, and `state` for **every** person in the `Person` table.
If a person has no matching entry in `Address`, return `null` for city and state.

## Primary Pandas Solution
- `person.merge(address, on="personId", how="left")` performs a left join — all rows from `Person` are kept, and matching rows from `Address` are attached where available.
- Where no match exists, pandas automatically fills the address columns with `NaN`.
- Select only the four required columns at the end.

## SQL Solution
- `LEFT JOIN` is the direct equivalent: keeps every row from the left table (`Person`) and fills `NULL` for unmatched right-table (`Address`) columns.
- An `INNER JOIN` would silently drop people with no address — a common bug in this type of problem.

## Alt Pandas Solution
- `pd.merge(person, address, ...)` is the module-level function equivalent of `person.merge(address, ...)`.
- Functionally identical — just a matter of style preference. The method form (`df.merge`) is more common in chained pipelines; the function form (`pd.merge`) can feel clearer when joining two independent DataFrames.

## Core Concept: JOIN Types
| Join type | Keeps |
|---|---|
| `INNER` / `how="inner"` | Only rows with a match on both sides |
| `LEFT` / `how="left"` | All left rows; NaN where no right match |
| `RIGHT` / `how="right"` | All right rows; NaN where no left match |
| `OUTER` / `how="outer"` | All rows from both sides |

## Gotcha
The instinct is often to use an inner join since it feels "cleaner" — but the problem explicitly requires every person to appear, making `LEFT JOIN` the only correct choice. Always check: *should missing matches be dropped or preserved?*