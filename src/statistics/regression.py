"""
Ordinary Least Squares (OLS) Regression.

Estimate the hedge ratio (beta) for pairs trading.
"""

from __future__ import annotations

import pandas as pd
import statsmodels.api as sm

from src.data.loader import MarketDataLoader


class RegressionAnalyzer:
    """
    Estimate hedge ratio using Ordinary Least Squares.
    """

    @staticmethod
    def load_prices() -> pd.DataFrame:

        loader = MarketDataLoader()

        ko = loader.get("KO")
        pep = loader.get("PEP")

        return pd.DataFrame(
            {
                "KO": ko["Close"],
                "PEP": pep["Close"],
            }
        ).dropna()

    @staticmethod
    def fit(df: pd.DataFrame):

        X = sm.add_constant(df["PEP"])

        y = df["KO"]

        model = sm.OLS(y, X).fit()

        return model

    @staticmethod
    def hedge_ratio(model) -> float:

        return float(model.params["PEP"])

    @staticmethod
    def intercept(model) -> float:

        return float(model.params["const"])


def main():

    df = RegressionAnalyzer.load_prices()

    model = RegressionAnalyzer.fit(df)

    beta = RegressionAnalyzer.hedge_ratio(model)

    intercept = RegressionAnalyzer.intercept(model)

    print()

    print("=" * 60)

    print("OLS REGRESSION")

    print("=" * 60)

    print()

    print(f"Intercept      : {intercept:.6f}")

    print(f"Hedge Ratio β  : {beta:.6f}")

    print()

    print(model.summary())


if __name__ == "__main__":
    main()

