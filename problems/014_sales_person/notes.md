# 014 - Sales Person

## Problem
Find salespeople who have never dealt with company "RED".

## Key Concepts
- Two-step filter: first get RED's company id, then find all sales_ids tied to RED orders.
- Then anti-filter salespeople using `~isin()`.
- This is a multi-table anti-join pattern.

## Pattern
Multi-table anti-join: filter → collect exclusion set → apply ~isin on target table.
