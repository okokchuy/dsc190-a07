"""Clean raw events: drop missing/invalid rows, normalize timestamps."""
import pandas as pd
from pathlib import Path

VALID_EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}

INPUT = Path("data/raw/events.csv")
OUTPUT = Path("data/clean/events.csv")


def main():
    df = pd.read_csv(INPUT)

    # drop rows with any missing field
    df = df.dropna()

    # drop rows with invalid event_type
    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    # drop rows with non-positive duration_seconds
    df = df[df["duration_seconds"] > 0]
    df["duration_seconds"] = df["duration_seconds"].astype(int)
   
     # normalize timestamp to ISO 8601 (YYYY-MM-DDTHH:MM:SS)
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="mixed", errors="coerce")
    df = df.dropna(subset=["timestamp"])
    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)


if __name__ == "__main__":
    main()
