import pandas as pd

# Problem: Department Top Three Salaries
# Find employees who earn one of the top 3 unique salaries in their department.

def solution(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    def top3(group):
        top = group["salary"].nlargest(3, keep="first")
        return group[group["salary"].isin(top)]

    top_earners = employee.groupby("departmentId", group_keys=False).apply(top3)
    result = top_earners.merge(department, left_on="departmentId", right_on="id")
    return result[["name_y", "name_x", "salary"]].rename(
        columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    )
