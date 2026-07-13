"""
Rank candidate pairs using the Engle-Granger cointegration test.
"""

from __future__ import annotations

import pandas as pd
from statsmodels.tsa.stattools import coint
from src.utils.logger import logger

from src.research.universe import StockUniverse
from src.research.pair_selector import PairSelector


class PairRanker:

    MAX_PVALUE = 0.05

    @staticmethod
    def rank(prices: pd.DataFrame,
             candidates: pd.DataFrame) -> pd.DataFrame:

        ranked = []

        logger.info("Running cointegration tests...")

        for _, row in candidates.iterrows():

            t1 = row["Ticker1"]
            t2 = row["Ticker2"]

            score, pvalue, _ = coint(
                prices[t1],
                prices[t2]
            )

            ranked.append(
                {
                    "Ticker1": t1,
                    "Ticker2": t2,
                    "Correlation": row["Correlation"],
                    "PValue": pvalue,
                    "Statistic": score,
                    "Tradable": pvalue < PairRanker.MAX_PVALUE,
                }
            )

        ranked = (
            pd.DataFrame(ranked)
            .sort_values(
                by=["Tradable", "PValue"],
                ascending=[False, True]
            )
            .reset_index(drop=True)
        )

        logger.info("Cointegration ranking completed.")

        return ranked


def main():

    prices = StockUniverse.download()

    returns = PairSelector.returns(prices)

    corr = PairSelector.correlation_matrix(returns)

    candidates = PairSelector.candidate_pairs(corr)

    ranked = PairRanker.rank(prices, candidates)

    print()
    print("=" * 70)
    print("PAIR RANKING")
    print("=" * 70)
    print()

    print(ranked)

    ranked.to_csv(
        "outputs/metrics/pair_ranking.csv",
        index=False,
    )

    print()
    print("Saved -> outputs/metrics/pair_ranking.csv")


if __name__ == "__main__":
    main()
