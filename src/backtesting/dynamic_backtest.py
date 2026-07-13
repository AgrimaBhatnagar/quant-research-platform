"""
Dynamic Backtesting Engine using Rolling Hedge Ratio.
"""

from __future__ import annotations

import pandas as pd
from src.utils.logger import logger

from src.strategies.dynamic_pairs_trading import DynamicPairsTrading
from src.statistics.dynamic_spread import DynamicSpread
from src.research.universe import StockUniverse


class DynamicBacktest:

    INITIAL_CAPITAL = 100000.0

    @staticmethod
    def run() -> pd.DataFrame:

        logger.info("Starting dynamic backtest...")

        prices = StockUniverse.download()[["KO", "PEP"]]

        df = DynamicSpread.calculate(prices)

        df = DynamicPairsTrading.generate_signals(df)

        # -----------------------
        # Position Management
        # -----------------------

        df["Position"] = df["Signal"]

        df["Position"] = (
            df["Position"]
            .replace(0, float("nan"))
            .ffill()
            .fillna(0)
        )

        # -----------------------
        # Spread Change
        # -----------------------

        df["SpreadChange"] = df["Spread"].diff()

        # -----------------------
        # Daily Profit/Loss
        # -----------------------

        df["PnL"] = (
            -df["Position"]
            .shift(1)
            .fillna(0)
            * df["SpreadChange"]
        )

        df["PnL"] = df["PnL"].fillna(0)

        # -----------------------
        # Portfolio
        # -----------------------

        df["PortfolioValue"] = (
            DynamicBacktest.INITIAL_CAPITAL
            + df["PnL"].cumsum()
        )

        logger.info("Backtest completed.")

        return df


def main():

    results = DynamicBacktest.run()

    print()

    print("=" * 70)
    print("DYNAMIC BACKTEST")
    print("=" * 70)

    print()

    print(
        results[
            [
                "Beta",
                "Spread",
                "ZScore",
                "Signal",
                "Position",
                "PnL",
                "PortfolioValue",
            ]
        ].tail(40)
    )

    print()

    print(
        "Initial Capital:",
        DynamicBacktest.INITIAL_CAPITAL,
    )

    print(
        "Final Portfolio:",
        results["PortfolioValue"].iloc[-1],
    )

    print(
        "Total Profit:",
        results["PortfolioValue"].iloc[-1]
        - DynamicBacktest.INITIAL_CAPITAL,
    )


if __name__ == "__main__":
    main()
