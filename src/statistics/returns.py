"""
Return calculations for financial time series.

This module provides reusable methods for computing
daily returns, log returns, cumulative returns,
annualized return, and annualized volatility.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


class ReturnCalculator:
    """
    Utility class for return calculations.
    """

    TRADING_DAYS = 252

    @staticmethod
    def daily_returns(prices: pd.Series) -> pd.Series:
        """
        Compute simple daily returns.

        r_t = (P_t / P_(t-1)) - 1
        """
        return prices.pct_change().dropna()

    @staticmethod
    def log_returns(prices: pd.Series) -> pd.Series:
        """
        Compute logarithmic returns.
        """
        return np.log(prices / prices.shift(1)).dropna()

    @staticmethod
    def cumulative_returns(returns: pd.Series) -> pd.Series:
        """
        Compute cumulative compounded returns.
        """
        return (1 + returns).cumprod() - 1

    @staticmethod
    def annualized_return(returns: pd.Series) -> float:
        """
        Compute annualized return.
        """
        compounded = (1 + returns).prod()

        years = len(returns) / ReturnCalculator.TRADING_DAYS

        return compounded ** (1 / years) - 1

    @staticmethod
    def annualized_volatility(returns: pd.Series) -> float:
        """
        Compute annualized volatility.
        """
        return returns.std() * np.sqrt(ReturnCalculator.TRADING_DAYS)


def main() -> None:

    prices = pd.Series(
        [
            100,
            102,
            101,
            104,
            108,
            110,
        ]
    )

    returns = ReturnCalculator.daily_returns(prices)

    print()

    print("Daily Returns")
    print(returns)

    print()

    print("Log Returns")
    print(ReturnCalculator.log_returns(prices))

    print()

    print("Cumulative Returns")
    print(ReturnCalculator.cumulative_returns(returns))

    print()

    print("Annualized Return")
    print(ReturnCalculator.annualized_return(returns))

    print()

    print("Annualized Volatility")
    print(ReturnCalculator.annualized_volatility(returns))


if __name__ == "__main__":
    main()
