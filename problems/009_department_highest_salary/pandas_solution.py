import pandas as pd

# Problem: Department Highest Salary
# Find employees who have the highest salary in their department.

def solution(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    dept_max = employee.groupby("departmentId")["salary"].transform("max")
    top_earners = employee[employee["salary"] == dept_max]
    result = top_earners.merge(department, left_on="departmentId", right_on="id")
    return result[["name_y", "name_x", "salary"]].rename(
        columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    )
