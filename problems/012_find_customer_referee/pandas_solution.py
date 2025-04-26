import pandas as pd

# Problem: Find Customer Referee
# Return customers NOT referred by customer with id = 2.

def solution(customer: pd.DataFrame) -> pd.DataFrame:
    mask = (customer["referee_id"] != 2) | (customer["referee_id"].isna())
    return customer[mask][["name"]]
