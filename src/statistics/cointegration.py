"""
Cointegration analysis using the Engle-Granger test.
"""

from __future__ import annotations

import pandas as pd
from statsmodels.tsa.stattools import coint

from src.data.loader import MarketDataLoader


class CointegrationAnalyzer:

    @staticmethod
    def load_prices() -> pd.DataFrame:

        loader = MarketDataLoader()

        ko = loader.get("KO")
        pep = loader.get("PEP")

        df = pd.DataFrame(
            {
                "KO": ko["Close"],
                "PEP": pep["Close"],
            }
        ).dropna()

        return df

    @staticmethod
    def test(df: pd.DataFrame):

        score, pvalue, critical_values = coint(
            df["KO"],
            df["PEP"],
        )

        return score, pvalue, critical_values


def main():

    df = CointegrationAnalyzer.load_prices()

    score, pvalue, critical_values = CointegrationAnalyzer.test(df)

    print()

    print("Engle-Granger Cointegration Test")

    print(f"\nTest Statistic : {score:.4f}")

    print(f"P-value        : {pvalue:.6f}")

    print("\nCritical Values")

    print(f"1%  : {critical_values[0]:.4f}")
    print(f"5%  : {critical_values[1]:.4f}")
    print(f"10% : {critical_values[2]:.4f}")

    print()

    if pvalue < 0.05:
        print("✓ Pair is cointegrated.")
    else:
        print("✗ Pair is NOT cointegrated.")


if __name__ == "__main__":
    main()

