import pandas as pd

# Problem: Customers Who Never Order (Alt)
# Using left join and filtering for NaN in the joined column.

def solution(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(orders, left_on="id", right_on="customerId", how="left")
    result = merged[merged["customerId"].isna()][["name"]]
    result.columns = ["Customers"]
    return result
