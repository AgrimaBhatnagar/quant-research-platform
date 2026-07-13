"""
Performance metrics for trading strategies.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


class PerformanceMetrics:

    TRADING_DAYS = 252

    @staticmethod
    def total_return(portfolio: pd.Series) -> float:
        return (portfolio.iloc[-1] / portfolio.iloc[0]) - 1

    @staticmethod
    def daily_returns(portfolio: pd.Series) -> pd.Series:
        return portfolio.pct_change().dropna()

    @staticmethod
    def annual_return(portfolio: pd.Series) -> float:

        total = PerformanceMetrics.total_return(portfolio)

        years = len(portfolio) / PerformanceMetrics.TRADING_DAYS

        return (1 + total) ** (1 / years) - 1

    @staticmethod
    def annual_volatility(portfolio: pd.Series) -> float:

        returns = PerformanceMetrics.daily_returns(portfolio)

        return returns.std() * np.sqrt(
            PerformanceMetrics.TRADING_DAYS
        )

    @staticmethod
    def sharpe_ratio(portfolio: pd.Series) -> float:

        returns = PerformanceMetrics.daily_returns(portfolio)

        if returns.std() == 0:
            return 0.0

        return (
            returns.mean()
            / returns.std()
        ) * np.sqrt(
            PerformanceMetrics.TRADING_DAYS
        )

    @staticmethod
    def max_drawdown(portfolio: pd.Series) -> float:

        running_max = portfolio.cummax()

        drawdown = (
            portfolio - running_max
        ) / running_max

        return drawdown.min()

