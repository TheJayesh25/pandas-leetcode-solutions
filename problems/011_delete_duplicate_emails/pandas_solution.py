import pandas as pd

# Problem: Delete Duplicate Emails
# Keep only the row with the smallest id for each email; delete the rest.

def solution(person: pd.DataFrame) -> pd.DataFrame:
    person.sort_values("id", inplace=True)
    person.drop_duplicates(subset=["email"], keep="first", inplace=True)
    return person
