import pandas as pd

# Problem: Article Views I
# Find all authors who have viewed at least one of their own articles.

def solution(views: pd.DataFrame) -> pd.DataFrame:
    self_views = views[views["author_id"] == views["viewer_id"]]
    result = self_views[["author_id"]].drop_duplicates().sort_values("author_id")
    result.columns = ["id"]
    return result
