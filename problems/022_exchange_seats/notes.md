# 022 - Exchange Seats

## Problem
Swap adjacent seat pairs. If odd number of students, last one stays.

## Key Concepts
- The key insight: swap the student names, keep the ids in order — OR swap the ids, keep names.
- Alt approach is cleaner: iterate through the student list, swap adjacent pairs in-place.
- SQL uses CASE WHEN on odd/even id modulo.

## Cleaner Mental Model
Think of it as swapping values in a list, not remapping IDs.
The alt approach with direct list swap is the most intuitive.
