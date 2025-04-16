import pandas as pd

# Problem: Second Highest Salary (Alt)
# Using rank to find the second highest salary.

def solution(employee: pd.DataFrame) -> pd.DataFrame:
    employee["rank"] = employee["salary"].rank(method="dense", ascending=False)
    result = employee[employee["rank"] == 2]["salary"]
    if result.empty:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    return pd.DataFrame({"SecondHighestSalary": [result.iloc[0]]})
