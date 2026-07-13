"""
Correlation analysis for financial assets.
"""

from __future__ import annotations

import pandas as pd

from src.data.loader import MarketDataLoader
from src.statistics.returns import ReturnCalculator


class CorrelationAnalyzer:

    @staticmethod
    def prepare_returns() -> pd.DataFrame:

        loader = MarketDataLoader()

        ko = loader.get("KO")
        pep = loader.get("PEP")

        ko_returns = ReturnCalculator.daily_returns(ko["Close"])
        pep_returns = ReturnCalculator.daily_returns(pep["Close"])

        df = pd.DataFrame(
            {
                "KO": ko_returns,
                "PEP": pep_returns,
            }
        ).dropna()

        return df

    @staticmethod
    def pearson(df: pd.DataFrame) -> float:

        return df["KO"].corr(df["PEP"], method="pearson")

    @staticmethod
    def spearman(df: pd.DataFrame) -> float:

        return df["KO"].corr(df["PEP"], method="spearman")

    @staticmethod
    def covariance(df: pd.DataFrame):

        return df.cov()


def main():

    df = CorrelationAnalyzer.prepare_returns()

    print()

    print("First 5 Daily Returns")
    print(df.head())

    print()

    print("Pearson Correlation")
    print(CorrelationAnalyzer.pearson(df))

    print()

    print("Spearman Correlation")
    print(CorrelationAnalyzer.spearman(df))

    print()

    print("Covariance Matrix")
    print(CorrelationAnalyzer.covariance(df))


if __name__ == "__main__":
    main()
