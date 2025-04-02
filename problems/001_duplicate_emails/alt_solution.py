import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicated = person[person.duplicated("email", keep=False)]

    return duplicated[["email"]].drop_duplicates()