import pandas as pd

# Problem: Game Play Analysis IV
# Find fraction of players who logged in again the day after their first login.

def solution(activity: pd.DataFrame) -> pd.DataFrame:
    activity["event_date"] = pd.to_datetime(activity["event_date"])
    first_login = activity.groupby("player_id")["event_date"].min().reset_index()
    first_login.columns = ["player_id", "first_date"]
    first_login["next_day"] = first_login["first_date"] + pd.Timedelta(days=1)

    merged = activity.merge(first_login, on="player_id")
    returned = merged[merged["event_date"] == merged["next_day"]]
    fraction = round(returned["player_id"].nunique() / first_login["player_id"].nunique(), 2)
    return pd.DataFrame({"fraction": [fraction]})
