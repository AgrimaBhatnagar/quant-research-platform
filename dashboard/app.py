"""
Pairs Trading Dashboard
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(PROJECT_ROOT))
import streamlit as st
import pandas as pd

from src.backtesting.dynamic_backtest import DynamicBacktest
from src.analytics.dynamic_metrics import DynamicMetrics

st.set_page_config(
    page_title="Pairs Trading Dashboard",
    layout="wide",
)

st.title("📈 Statistical Arbitrage Dashboard")

results = DynamicBacktest.run()

portfolio = results["PortfolioValue"]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Return",
    f"{DynamicMetrics.total_return(portfolio):.2%}",
)

col2.metric(
    "Sharpe Ratio",
    f"{DynamicMetrics.sharpe_ratio(portfolio):.2f}",
)

col3.metric(
    "Max Drawdown",
    f"{DynamicMetrics.max_drawdown(portfolio):.2%}",
)

st.divider()

st.subheader("Portfolio Value")

st.line_chart(
    results["PortfolioValue"]
)

st.subheader("Spread")

st.line_chart(
    results["Spread"]
)

st.subheader("Z Score")

st.line_chart(
    results["ZScore"]
)

st.subheader("Signals")

st.dataframe(
    results[
        [
            "Spread",
            "ZScore",
            "Signal",
            "PortfolioValue",
        ]
    ].tail(100)
)
