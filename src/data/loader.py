
"""
Market data loader.

Loads cleaned market data and caches it in memory.
"""

from __future__ import annotations

from typing import Dict

import pandas as pd

from src.data.preprocessor import DataPreprocessor


class MarketDataLoader:
    """
    Loads and caches cleaned market data.
    """

    def __init__(self) -> None:
        self.processor = DataPreprocessor()
        self._cache: Dict[str, pd.DataFrame] = {}

    def get(self, ticker: str) -> pd.DataFrame:
        ticker = ticker.upper()

        if ticker not in self._cache:
            self._cache[ticker] = self.processor.load(ticker)

        return self._cache[ticker].copy()

    def clear_cache(self) -> None:
        self._cache.clear()

    def loaded_tickers(self) -> list[str]:
        return list(self._cache.keys())


def main() -> None:
    loader = MarketDataLoader()

    ko = loader.get("KO")
    pep = loader.get("PEP")

    print("\nLoaded tickers:")
    print(loader.loaded_tickers())

    print("\nKO")
    print(ko.head())

    print("\nPEP")
    print(pep.head())


if __name__ == "__main__":
    main()
