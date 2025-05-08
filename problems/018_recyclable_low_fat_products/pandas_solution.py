import pandas as pd

# Problem: Recyclable and Low Fat Products
# Find products that are both low fat AND recyclable.

def solution(products: pd.DataFrame) -> pd.DataFrame:
    mask = (products["low_fats"] == "Y") & (products["recyclable"] == "Y")
    return products[mask][["product_id"]]
