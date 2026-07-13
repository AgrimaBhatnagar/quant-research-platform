"""
Pairs Trading Strategy
"""

from __future__ import annotations

import pandas as pd

from src.statistics.spread import SpreadAnalyzer
from src.statistics.regression import RegressionAnalyzer


class PairsTradingStrategy:

    ENTRY = 2.0
    EXIT = 0.5

    @staticmethod
    def generate_signals(df: pd.DataFrame) -> pd.DataFrame:

        signals = df.copy()

        signals["Signal"] = 0

        # Long KO / Short PEP
        signals.loc[
            signals["ZScore"] < -PairsTradingStrategy.ENTRY,
            "Signal",
        ] = 1

        # Short KO / Long PEP
        signals.loc[
            signals["ZScore"] > PairsTradingStrategy.ENTRY,
            "Signal",
        ] = -1

        # Exit
        signals.loc[
            signals["ZScore"].abs() < PairsTradingStrategy.EXIT,
            "Signal",
        ] = 0

        return signals


def main():

    prices = RegressionAnalyzer.load_prices()

    model = RegressionAnalyzer.fit(prices)

    beta = RegressionAnalyzer.hedge_ratio(model)

    spread = SpreadAnalyzer.calculate(prices, beta)

    signals = PairsTradingStrategy.generate_signals(spread)

    print()

    print("=" * 60)
    print("SIGNALS")
    print("=" * 60)

    print()

    print(signals[["Spread", "ZScore", "Signal"]].tail(40))

    print()

    print("Signal Counts")

    print(signals["Signal"].value_counts())


if __name__ == "__main__":
    main()