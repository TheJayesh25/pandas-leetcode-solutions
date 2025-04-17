import pandas as pd

# Problem: Employees Earning More Than Their Manager
# Find employees whose salary is greater than their manager's salary.

def solution(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(
        employee, left_on="managerId", right_on="id", suffixes=("_emp", "_mgr")
    )
    result = merged[merged["salary_emp"] > merged["salary_mgr"]][["name_emp"]]
    result.columns = ["Employee"]
    return result
