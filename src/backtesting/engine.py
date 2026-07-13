"""
Simple event-driven backtesting engine.
"""

from __future__ import annotations
from src.backtesting.trade_logger import TradeLogger
import pandas as pd

from src.statistics.regression import RegressionAnalyzer
from src.statistics.spread import SpreadAnalyzer
from src.strategies.pairs_trading import PairsTradingStrategy


class BacktestEngine:

    INITIAL_CAPITAL = 100000.0

    @staticmethod
    def run() -> pd.DataFrame:

        # ------------------------
        # Load Data
        # ------------------------

        prices = RegressionAnalyzer.load_prices()

        model = RegressionAnalyzer.fit(prices)

        beta = RegressionAnalyzer.hedge_ratio(model)

        spread = SpreadAnalyzer.calculate(prices, beta)

        df = PairsTradingStrategy.generate_signals(spread)

        # ------------------------
        # Portfolio
        # ------------------------

        # Build positions
        df["Position"] = df["Signal"]

        # Replace neutral signals with NaN
        df["Position"] = df["Position"].replace(0, float("nan"))

        # Carry last position forward
        df["Position"] = df["Position"].ffill()

        # Start flat
        df["Position"] = df["Position"].fillna(0)

        # Make sure Position is numeric
        df["Position"] = df["Position"].astype(float)

        df["SpreadChange"] = df["Spread"].diff()

        df["PnL"] = -df["Position"].shift(1) * df["SpreadChange"]

        df["PnL"] = df["PnL"].fillna(0)

        df["PortfolioValue"] = (
            BacktestEngine.INITIAL_CAPITAL
            + df["PnL"].cumsum()
        )

        return df


def main():

    results = BacktestEngine.run()

    print()

    print("=" * 60)
    print("BACKTEST")
    print("=" * 60)

    print()

    print(results[
        [
            "Spread",
            "ZScore",
            "Signal",
            "Position",
            "PnL",
            "PortfolioValue",
        ]
    ].tail(40))

    print()

    print("Initial Capital :", BacktestEngine.INITIAL_CAPITAL)

    print("Final Portfolio :", results["PortfolioValue"].iloc[-1])

    print("Total Profit    :",
          results["PortfolioValue"].iloc[-1]
          - BacktestEngine.INITIAL_CAPITAL)
    trades = TradeLogger.generate(results)

    print()

    print("=" * 60)

    print("TRADE LOG")

    print("=" * 60)

    print()

    print(trades.head())

    trades.to_csv(
        "outputs/trades/trades.csv",
        index=False,
    )

    print()

    print("Trade log saved.")


if __name__ == "__main__":
    main()

