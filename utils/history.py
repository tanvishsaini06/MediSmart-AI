import pandas as pd
import os


HISTORY_FILE = "data/search_history.csv"


def save_search(medicine):
    if not os.path.exists(HISTORY_FILE):
        df = pd.DataFrame(columns=["Medicine"])
    else:
        df = pd.read_csv(HISTORY_FILE)

    new_row = pd.DataFrame({"Medicine": [medicine]})
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(HISTORY_FILE, index=False)


def load_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)
    return pd.DataFrame(columns=["Medicine"])