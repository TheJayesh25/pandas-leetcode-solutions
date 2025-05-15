import pandas as pd

# Problem: Immediate Food Delivery II
# Find % of customers whose first order was an immediate order.
# Immediate = order_date == customer_pref_delivery_date

def solution(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery["order_date"] = pd.to_datetime(delivery["order_date"])
    delivery["customer_pref_delivery_date"] = pd.to_datetime(
        delivery["customer_pref_delivery_date"]
    )
    first_orders = delivery.groupby("customer_id")["order_date"].min().reset_index()
    first_orders.columns = ["customer_id", "first_date"]
    merged = delivery.merge(first_orders, on="customer_id")
    first = merged[merged["order_date"] == merged["first_date"]]
    immediate = first[first["order_date"] == first["customer_pref_delivery_date"]]
    pct = round(len(immediate) / len(first) * 100, 2)
    return pd.DataFrame({"immediate_percentage": [pct]})
