import pandas as pd

# Problem: Classes More Than 5 Students
# Find all classes that have at least 5 students enrolled.

def solution(courses: pd.DataFrame) -> pd.DataFrame:
    counts = courses.groupby("class", as_index=False)["student"].count()
    result = counts[counts["student"] >= 5][["class"]]
    return result
