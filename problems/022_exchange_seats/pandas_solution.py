import pandas as pd

# Problem: Exchange Seats
# Swap every pair of adjacent students. If total is odd, last student stays.

def solution(seat: pd.DataFrame) -> pd.DataFrame:
    seat = seat.sort_values("id").reset_index(drop=True)
    n = len(seat)
    new_ids = []
    for i in range(n):
        if i % 2 == 0:  # even index (1-based odd id)
            new_ids.append(i + 2 if i + 1 < n else i + 1)
        else:  # odd index (1-based even id)
            new_ids.append(i)
    seat["id"] = new_ids
    return seat.sort_values("id").reset_index(drop=True)
