import pandas as pd

# Problem: Exchange Seats (Alt)
# Using numpy-style index swapping for cleaner pair exchange.

def solution(seat: pd.DataFrame) -> pd.DataFrame:
    seat = seat.sort_values("id").reset_index(drop=True)
    students = seat["student"].tolist()
    for i in range(0, len(students) - 1, 2):
        students[i], students[i + 1] = students[i + 1], students[i]
    seat["student"] = students
    return seat
