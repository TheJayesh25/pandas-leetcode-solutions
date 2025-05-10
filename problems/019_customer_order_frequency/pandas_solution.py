import pandas as pd

# Problem: Customer Order Frequency
# Find customers who spent >= $100 in June 2020 AND >= $100 in July 2020.

def solution(
    customers: pd.DataFrame,
    orders: pd.DataFrame,
    product: pd.DataFrame
) -> pd.DataFrame:
    merged = orders.merge(product, on="product_id")
    merged["amount"] = merged["quantity"] * merged["price"]
    merged["order_date"] = pd.to_datetime(merged["order_date"])

    june = merged[merged["order_date"].dt.month == 6].groupby("customer_id")["amount"].sum()
    july = merged[merged["order_date"].dt.month == 7].groupby("customer_id")["amount"].sum()

    qualified = june.index.intersection(july.index)
    qualified = [c for c in qualified if june[c] >= 100 and july[c] >= 100]

    result = customers[customers["customer_id"].isin(qualified)][["customer_id", "name"]]
    return result
