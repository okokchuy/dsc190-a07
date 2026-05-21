"""Add a 'date' column to cleaned events."""
import pandas as pd
from pathlib import Path

INPUT = Path("data/clean/events.csv")
OUTPUT = Path("data/transformed/events.csv")


def main():
    df = pd.read_csv(INPUT)
    # timestamp is already YYYY-MM-DDTHH:MM:SS, so date is the first 10 chars
    df["date"] = df["timestamp"].str.slice(0, 10)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)


if __name__ == "__main__":
    main()
