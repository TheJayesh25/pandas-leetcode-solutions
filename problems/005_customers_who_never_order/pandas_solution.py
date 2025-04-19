import pandas as pd

# Problem: Customers Who Never Order
# Find customers who have no corresponding order in the Orders table.

def solution(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers[~customers["id"].isin(orders["customerId"])][["name"]]
    result.columns = ["Customers"]
    return result
