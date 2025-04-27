import pandas as pd

# Problem: Customer Placing the Largest Number of Orders
# Find the customer(s) who placed the most orders.

def solution(orders: pd.DataFrame) -> pd.DataFrame:
    counts = orders.groupby("customer_number", as_index=False).size()
    max_count = counts["size"].max()
    result = counts[counts["size"] == max_count][["customer_number"]]
    return result
