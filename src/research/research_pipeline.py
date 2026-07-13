"""
Complete Quant Research Pipeline.
"""

from __future__ import annotations

from pathlib import Path
from src.utils.logger import logger

from src.research.universe import StockUniverse
from src.research.pair_selector import PairSelector
from src.research.pair_ranker import PairRanker


OUTPUT_DIR = Path("outputs/research")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class ResearchPipeline:

    @staticmethod
    def run():

        print("=" * 70)
        print("QUANT RESEARCH PIPELINE")
        print("=" * 70)

        logger.info("Step 1 : Downloading universe...")
        prices = StockUniverse.download()

        logger.info("Done")

        print("\nStep 2 : Computing returns...")
        returns = PairSelector.returns(prices)

        logger.info("Done")

        print("\nStep 3 : Correlation matrix...")
        corr = PairSelector.correlation_matrix(returns)

        logger.info("Done")

        print("\nStep 4 : Selecting candidate pairs...")
        pairs = PairSelector.candidate_pairs(corr)

        print(f"✓ Found {len(pairs)} candidate pairs")

        print("\nStep 5 : Cointegration ranking...")
        ranked = PairRanker.rank(prices, pairs)

        logger.info("Done")

        ranked.to_csv(
            OUTPUT_DIR / "pair_ranking.csv",
            index=False,
        )

        print("\nTop 10 Pairs")
        print("-" * 70)

        print(ranked.head(10))

        print("\nResearch report saved to:")
        print(OUTPUT_DIR / "pair_ranking.csv")


def main():

    ResearchPipeline.run()


if __name__ == "__main__":
    main()
