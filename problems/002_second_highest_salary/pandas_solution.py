import pandas as pd

# Problem: Second Highest Salary
# Return the second highest distinct salary from Employee table.
# If no second highest salary exists, return null.

def solution(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee["salary"].drop_duplicates().nlargest(2)
    if len(unique_salaries) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    second = unique_salaries.iloc[1]
    return pd.DataFrame({"SecondHighestSalary": [second]})
