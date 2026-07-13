"""
Data preprocessing utilities.
"""

from pathlib import Path

import pandas as pd

from config.settings import RAW_DATA_DIR


class DataPreprocessor:
    """
    Cleans downloaded Yahoo Finance data.
    """

    REQUIRED_COLUMNS = [
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    ]

    def __init__(self, data_dir=RAW_DATA_DIR):
        self.data_dir = Path(data_dir)

    def load(self, ticker: str) -> pd.DataFrame:
        """
        Load CSV for one ticker.
        """

        file_path = self.data_dir / f"{ticker}.csv"

        df = pd.read_csv(file_path)

        return self.clean(df)

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean dataframe.
        """

        # -----------------------------
        # Handle MultiIndex CSV produced
        # by newer yfinance versions
        # -----------------------------

        if df.columns[0] == "Price":

            first = df.iloc[0]
            second = df.iloc[1]

            columns = ["Date"]

            for c in df.columns[1:]:
                columns.append(c)

            df = df.iloc[2:].copy()

            df.columns = columns

        # -----------------------------
        # Date
        # -----------------------------

        df["Date"] = pd.to_datetime(df["Date"])

        # -----------------------------
        # Numeric columns
        # -----------------------------

        numeric_columns = [
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
        ]

        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col])

        # -----------------------------
        # Sort
        # -----------------------------

        df = df.sort_values("Date")

        # -----------------------------
        # Missing values
        # -----------------------------

        df = df.dropna()

        # -----------------------------
        # Reset index
        # -----------------------------

        df = df.reset_index(drop=True)

        return df


if __name__ == "__main__":

    processor = DataPreprocessor()

    ko = processor.load("KO")

    print(ko.head())

    print()

    print(ko.info())

