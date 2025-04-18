import pandas as pd

# Problem: Combine Two Tables (Alt)
# Using pd.merge() with explicit left join and selecting final columns.
# Equivalent result — demonstrates how unmatched rows naturally become NaN.

def solution(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(person, address, on="personId", how="left")[
        ["firstName", "lastName", "city", "state"]
    ]