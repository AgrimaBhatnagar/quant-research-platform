"""
Generate strategy performance report.
"""

from __future__ import annotations

from src.analytics.metrics import PerformanceMetrics
from src.backtesting.engine import BacktestEngine


def main():

    results = BacktestEngine.run()

    portfolio = results["PortfolioValue"]

    print()

    print("=" * 60)
    print("PERFORMANCE REPORT")
    print("=" * 60)

    print()

    print(
        f"Total Return        : "
        f"{PerformanceMetrics.total_return(portfolio):.2%}"
    )

    print(
        f"Annual Return       : "
        f"{PerformanceMetrics.annual_return(portfolio):.2%}"
    )

    print(
        f"Annual Volatility   : "
        f"{PerformanceMetrics.annual_volatility(portfolio):.2%}"
    )

    print(
        f"Sharpe Ratio        : "
        f"{PerformanceMetrics.sharpe_ratio(portfolio):.3f}"
    )

    print(
        f"Maximum Drawdown    : "
        f"{PerformanceMetrics.max_drawdown(portfolio):.2%}"
    )


if __name__ == "__main__":
    main()
