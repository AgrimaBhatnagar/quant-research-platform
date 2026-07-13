"""
Download historical stock data from Yahoo Finance.

Author: Agrima Bhatnagar
"""

from pathlib import Path

import pandas as pd
import yfinance as yf
from src.utils.logger import logger

from config.settings import (
    RAW_DATA_DIR,
    START_DATE,
    END_DATE,
)


def download_stock_data(
    ticker: str,
    start_date: str = START_DATE,
    end_date: str | None = END_DATE,
) -> pd.DataFrame:
    """
    Download historical OHLCV data for a stock.

    Parameters
    ----------
    ticker : str
        Stock symbol.

    start_date : str
        Download start date.

    end_date : str | None
        Download end date.

    Returns
    -------
    pd.DataFrame
    """

    logger.info(f"Downloading {ticker}...")

    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False,
    )

    if df.empty:
        raise ValueError(f"No data downloaded for {ticker}")

    df.index.name = "Date"

    return df


def save_stock_data(
    df: pd.DataFrame,
    ticker: str,
):
    """
    Save dataframe to CSV.
    """

    output_path = RAW_DATA_DIR / f"{ticker}.csv"

    df.to_csv(output_path)

    logger.info(f"Saved -> {filepath}")


def download_multiple_stocks(
    tickers: list[str],
):
    """
    Download multiple stocks.
    """

    for ticker in tickers:

        try:

            df = download_stock_data(ticker)

            save_stock_data(df, ticker)

        except Exception as e:

            print(f"{ticker} failed")

            print(e)


if __name__ == "__main__":

    download_multiple_stocks(
        [
            "KO",
            "PEP",
        ]
    )

