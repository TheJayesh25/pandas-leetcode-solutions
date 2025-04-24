import pandas as pd

# Problem: Department Top Three Salaries (Alt)
# Using dense_rank per department to find top 3.

def solution(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee["rank"] = employee.groupby("departmentId")["salary"].rank(
        method="dense", ascending=False
    )
    top_earners = employee[employee["rank"] <= 3]
    result = top_earners.merge(department, left_on="departmentId", right_on="id")
    return result[["name_y", "name_x", "salary"]].rename(
        columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    )
