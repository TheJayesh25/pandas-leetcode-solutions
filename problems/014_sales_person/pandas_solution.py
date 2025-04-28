import pandas as pd

# Problem: Sales Person
# Find salespeople who have NOT made any orders for company "RED".

def solution(
    sales_person: pd.DataFrame,
    company: pd.DataFrame,
    orders: pd.DataFrame
) -> pd.DataFrame:
    red_id = company[company["name"] == "RED"]["id"]
    red_orders = orders[orders["com_id"].isin(red_id)]["sales_id"]
    result = sales_person[~sales_person["sales_id"].isin(red_orders)][["name"]]
    return result
