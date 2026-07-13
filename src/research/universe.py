"""
Download and prepare a universe of stock prices.
"""

from __future__ import annotations
from src.utils.logger import logger
import pandas as pd
import yfinance as yf


class StockUniverse:

    TICKERS = [
        "KO",
        "PEP",
        "AAPL",
        "MSFT",
        "NVDA",
        "AMD",
        "META",
        "GOOG",
        "AMZN",
        "WMT",
    ]

    START = "2018-01-01"

    @classmethod
    def download(cls) -> pd.DataFrame:

        prices = pd.DataFrame()

        for ticker in cls.TICKERS:

            logger.info(f"Downloading {ticker}...")

            data = yf.download(
                ticker,
                start=cls.START,
                progress=False,
                auto_adjust=True,
            )

            prices[ticker] = data["Close"]

        prices = prices.dropna()

        return prices


def main():

    prices = StockUniverse.download()

    print()

    print(prices.head())

    print()

    print("Shape:", prices.shape)


if __name__ == "__main__":
    main()
