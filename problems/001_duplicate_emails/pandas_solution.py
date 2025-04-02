import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicates = person.groupby("email").size().reset_index(name="count")
    duplicates = duplicates[duplicates["count"] > 1]

    return duplicates[["email"]]