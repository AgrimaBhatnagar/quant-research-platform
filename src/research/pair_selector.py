"""
Find highly correlated stock pairs.
"""

from __future__ import annotations

import itertools

import pandas as pd

from src.research.universe import StockUniverse


class PairSelector:

    MIN_CORRELATION = 0.50

    @staticmethod
    def returns(prices: pd.DataFrame) -> pd.DataFrame:
        return prices.pct_change().dropna()

    @staticmethod
    def correlation_matrix(returns: pd.DataFrame) -> pd.DataFrame:
        return returns.corr()

    @staticmethod
    def candidate_pairs(corr: pd.DataFrame) -> pd.DataFrame:

        pairs = []

        tickers = corr.columns.tolist()

        for a, b in itertools.combinations(tickers, 2):

            value = corr.loc[a, b]

            pairs.append(
                    {
                        "Ticker1": a,
                        "Ticker2": b,
                        "Correlation": value,
                    }
                )

        return (
                pd.DataFrame(pairs)
                .sort_values("Correlation", ascending=False)
                .reset_index(drop=True)
            )

def main():

    prices = StockUniverse.download()

    returns = PairSelector.returns(prices)

    corr = PairSelector.correlation_matrix(returns)

    pairs = PairSelector.candidate_pairs(corr)

    print()

    print("=" * 60)
    print("TOP CORRELATED PAIRS")
    print("=" * 60)

    print()

    print(pairs)


if __name__ == "__main__":
    main()

