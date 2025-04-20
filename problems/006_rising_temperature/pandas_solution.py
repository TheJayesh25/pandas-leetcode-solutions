import pandas as pd

# Problem: Rising Temperature
# Find all dates where temperature is higher than the previous day.

def solution(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values("recordDate").reset_index(drop=True)
    weather["prev_temp"] = weather["temperature"].shift(1)
    weather["prev_date"] = weather["recordDate"].shift(1)
    mask = (
        (weather["temperature"] > weather["prev_temp"]) &
        (weather["recordDate"] - weather["prev_date"] == pd.Timedelta(days=1))
    )
    return weather[mask][["id"]].reset_index(drop=True)
