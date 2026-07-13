"""
Dynamic Spread Calculation using Rolling Hedge Ratio.
"""

from __future__ import annotations

import pandas as pd

from src.models.rolling_regression import RollingRegression
from src.research.universe import StockUniverse


class DynamicSpread:

    WINDOW = 30

    @staticmethod
    def calculate(prices: pd.DataFrame) -> pd.DataFrame:

        df = RollingRegression.hedge_ratio(prices)

        df["Spread"] = (
            df["KO"]
            - df["Beta"] * df["PEP"]
        )

        df["RollingMean"] = (
            df["Spread"]
            .rolling(DynamicSpread.WINDOW)
            .mean()
        )

        df["RollingStd"] = (
            df["Spread"]
            .rolling(DynamicSpread.WINDOW)
            .std()
        )

        df["ZScore"] = (
            df["Spread"]
            - df["RollingMean"]
        ) / df["RollingStd"]

        return df


def main():

    prices = StockUniverse.download()[["KO", "PEP"]]

    results = DynamicSpread.calculate(prices)

    print()

    print("=" * 60)
    print("DYNAMIC SPREAD")
    print("=" * 60)

    print()

    print(results.tail())


if __name__ == "__main__":
    main()
