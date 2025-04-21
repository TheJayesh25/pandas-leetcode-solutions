import pandas as pd

# Problem: Big Countries
# A country is big if area >= 3,000,000 OR population >= 25,000,000.

def solution(world: pd.DataFrame) -> pd.DataFrame:
    mask = (world["area"] >= 3_000_000) | (world["population"] >= 25_000_000)
    return world[mask][["name", "population", "area"]]
