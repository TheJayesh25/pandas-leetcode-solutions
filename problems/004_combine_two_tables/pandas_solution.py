import pandas as pd

# Problem: Combine Two Tables
# Report firstName, lastName, city, and state for every person.
# If a person has no address, city and state should be null.

def solution(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged = person.merge(address, on="personId", how="left")
    return merged[["firstName", "lastName", "city", "state"]]