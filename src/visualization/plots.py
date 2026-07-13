"""
Visualization module for the Quant Research Platform.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from src.backtesting.engine import BacktestEngine

OUTPUT_DIR = Path("outputs/figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class PlotGenerator:

    @staticmethod
    def equity_curve(df):

        plt.figure(figsize=(12,6))

        plt.plot(df.index,
                 df["PortfolioValue"],
                 linewidth=2)

        plt.title("Portfolio Equity Curve")

        plt.xlabel("Trading Days")

        plt.ylabel("Portfolio Value")

        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            OUTPUT_DIR / "equity_curve.png",
            dpi=300
        )

        plt.close()

    @staticmethod
    def spread(df):

        plt.figure(figsize=(14, 6))

        plt.plot(
            df.index,
            df["Spread"],
            label="Spread",
            linewidth=1.5,
        )

        plt.plot(
            df.index,
            df["RollingMean"],
            label="Rolling Mean",
            linewidth=2,
        )

        buys = df[df["Signal"] == 1]

        sells = df[df["Signal"] == -1]

        plt.scatter(
            buys.index,
            buys["Spread"],
            marker="^",
            s=90,
            label="BUY",
        )

        plt.scatter(
            sells.index,
            sells["Spread"],
            marker="v",
            s=90,
            label="SELL",
        )

        plt.title("Spread with Trading Signals")

        plt.xlabel("Trading Days")

        plt.ylabel("Spread")

        plt.legend()

        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            OUTPUT_DIR / "spread_signals.png",
            dpi=300,
        )

        plt.close()

    @staticmethod
    def zscore(df):

        plt.figure(figsize=(12,6))

        plt.plot(
            df.index,
            df["ZScore"],
            label="Z-Score"
        )

        plt.axhline(
            2,
            linestyle="--"
        )

        plt.axhline(
            -2,
            linestyle="--"
        )

        plt.axhline(
            0,
            linestyle=":"
        )

        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            OUTPUT_DIR / "zscore.png",
            dpi=300
        )

        plt.close()


def main():

    results = BacktestEngine.run()

    PlotGenerator.equity_curve(results)

    PlotGenerator.spread(results)

    PlotGenerator.zscore(results)

    print()

    print("Charts saved to outputs/figures/")


if __name__ == "__main__":
    main()
