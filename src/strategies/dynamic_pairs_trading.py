"""
Dynamic Pairs Trading Strategy using Rolling Hedge Ratio.
"""

from __future__ import annotations

import pandas as pd

from src.statistics.dynamic_spread import DynamicSpread
from src.research.universe import StockUniverse


class DynamicPairsTrading:

    ENTRY_Z = 2.0
    EXIT_Z = 0.5

    @staticmethod
    def generate_signals(df: pd.DataFrame) -> pd.DataFrame:

        result = df.copy()

        result["Signal"] = 0

        # Long Spread
        result.loc[
            result["ZScore"] < -DynamicPairsTrading.ENTRY_Z,
            "Signal",
        ] = 1

        # Short Spread
        result.loc[
            result["ZScore"] > DynamicPairsTrading.ENTRY_Z,
            "Signal",
        ] = -1

        # Exit
        result.loc[
            result["ZScore"].abs() < DynamicPairsTrading.EXIT_Z,
            "Signal",
        ] = 0

        return result


def main():

    prices = StockUniverse.download()[["KO", "PEP"]]

    spread = DynamicSpread.calculate(prices)

    signals = DynamicPairsTrading.generate_signals(spread)

    print()

    print("=" * 70)
    print("DYNAMIC PAIRS TRADING")
    print("=" * 70)

    print()

    print(
        signals[
            [
                "KO",
                "PEP",
                "Beta",
                "Spread",
                "ZScore",
                "Signal",
            ]
        ].tail(40)
    )

    print()

    print("Signal Counts")

    print(signals["Signal"].value_counts())


if __name__ == "__main__":
    main()
