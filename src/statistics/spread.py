"""
Spread and Z-Score calculations for pairs trading.
"""

from __future__ import annotations

import pandas as pd

from src.statistics.regression import RegressionAnalyzer


class SpreadAnalyzer:

    WINDOW = 30

    @staticmethod
    def calculate(df: pd.DataFrame, beta: float) -> pd.DataFrame:
        """
        Calculate spread and rolling statistics.
        """

        result = df.copy()

        result["Spread"] = result["KO"] - beta * result["PEP"]

        result["RollingMean"] = (
            result["Spread"]
            .rolling(SpreadAnalyzer.WINDOW)
            .mean()
        )

        result["RollingStd"] = (
            result["Spread"]
            .rolling(SpreadAnalyzer.WINDOW)
            .std()
        )

        result["ZScore"] = (
            result["Spread"] - result["RollingMean"]
        ) / result["RollingStd"]

        return result


def main():

    df = RegressionAnalyzer.load_prices()

    model = RegressionAnalyzer.fit(df)

    beta = RegressionAnalyzer.hedge_ratio(model)

    spread = SpreadAnalyzer.calculate(df, beta)

    print()

    print("=" * 60)
    print("SPREAD")
    print("=" * 60)

    print()

    print(spread.head(35))

    print()

    print("Latest Spread")

    print(spread[["Spread", "RollingMean", "RollingStd", "ZScore"]].tail())


if __name__ == "__main__":
    main()
