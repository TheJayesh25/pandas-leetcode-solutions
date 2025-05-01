import pandas as pd

# Problem: Employee Bonus
# Find employees whose bonus is less than 1000, or who have no bonus entry.

def solution(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(bonus, on="empId", how="left")
    result = merged[(merged["bonus"] < 1000) | (merged["bonus"].isna())]
    return result[["name", "bonus"]]
