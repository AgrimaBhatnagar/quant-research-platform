"""
Performance metrics for the Dynamic Backtesting Engine.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.backtesting.dynamic_backtest import DynamicBacktest


class DynamicMetrics:

    TRADING_DAYS = 252

    @staticmethod
    def daily_returns(portfolio: pd.Series) -> pd.Series:

        return portfolio.pct_change().dropna()

    @staticmethod
    def total_return(portfolio: pd.Series) -> float:

        return portfolio.iloc[-1] / portfolio.iloc[0] - 1

    @staticmethod
    def annual_return(portfolio: pd.Series) -> float:

        total = DynamicMetrics.total_return(portfolio)

        years = len(portfolio) / DynamicMetrics.TRADING_DAYS

        return (1 + total) ** (1 / years) - 1

    @staticmethod
    def annual_volatility(portfolio: pd.Series) -> float:

        returns = DynamicMetrics.daily_returns(portfolio)

        return returns.std() * np.sqrt(
            DynamicMetrics.TRADING_DAYS
        )

    @staticmethod
    def sharpe_ratio(portfolio: pd.Series) -> float:

        returns = DynamicMetrics.daily_returns(portfolio)

        if returns.std() == 0:
            return 0.0

        return (
            returns.mean()
            / returns.std()
        ) * np.sqrt(
            DynamicMetrics.TRADING_DAYS
        )

    @staticmethod
    def sortino_ratio(portfolio: pd.Series) -> float:

        returns = DynamicMetrics.daily_returns(portfolio)

        downside = returns[returns < 0]

        if len(downside) == 0:
            return 0.0

        downside_std = downside.std()

        if downside_std == 0:
            return 0.0

        return (
            returns.mean()
            / downside_std
        ) * np.sqrt(
            DynamicMetrics.TRADING_DAYS
        )

    @staticmethod
    def max_drawdown(portfolio: pd.Series) -> float:

        running_max = portfolio.cummax()

        drawdown = (
            portfolio
            - running_max
        ) / running_max

        return drawdown.min()


def main():

    results = DynamicBacktest.run()

    portfolio = results["PortfolioValue"]

    print()

    print("=" * 70)
    print("DYNAMIC PERFORMANCE REPORT")
    print("=" * 70)

    print()

    print(
        f"Total Return      : {DynamicMetrics.total_return(portfolio):.2%}"
    )

    print(
        f"Annual Return     : {DynamicMetrics.annual_return(portfolio):.2%}"
    )

    print(
        f"Annual Volatility : {DynamicMetrics.annual_volatility(portfolio):.2%}"
    )

    print(
        f"Sharpe Ratio      : {DynamicMetrics.sharpe_ratio(portfolio):.4f}"
    )

    print(
        f"Sortino Ratio     : {DynamicMetrics.sortino_ratio(portfolio):.4f}"
    )

    print(
        f"Maximum Drawdown  : {DynamicMetrics.max_drawdown(portfolio):.2%}"
    )


if __name__ == "__main__":
    main()

