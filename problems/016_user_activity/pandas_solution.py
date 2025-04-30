import pandas as pd

# Problem: User Activity for the Past 30 Days I
# Count daily active users for each day where activity exists in a 30-day window.

def solution(activity: pd.DataFrame) -> pd.DataFrame:
    activity["activity_date"] = pd.to_datetime(activity["activity_date"])
    end_date = pd.Timestamp("2019-07-27")
    start_date = end_date - pd.Timedelta(days=29)
    filtered = activity[
        (activity["activity_date"] >= start_date) &
        (activity["activity_date"] <= end_date)
    ]
    result = (
        filtered.groupby("activity_date")["user_id"]
        .nunique()
        .reset_index()
    )
    result.columns = ["day", "active_users"]
    return result
