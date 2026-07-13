"""
Rolling OLS Regression for dynamic hedge ratio estimation.
"""

from __future__ import annotations
from src.utils.logger import logger
import pandas as pd
import statsmodels.api as sm

from src.research.universe import StockUniverse


class RollingRegression:

    WINDOW = 252

    @staticmethod
    def hedge_ratio(prices: pd.DataFrame) -> pd.DataFrame:

        betas = []

        logger.info("Estimating rolling hedge ratios...")

        for i in range(len(prices)):

            if i < RollingRegression.WINDOW:

                betas.append(None)

                continue

            window = prices.iloc[
                i - RollingRegression.WINDOW : i
            ]

            X = sm.add_constant(window["PEP"])

            y = window["KO"]

            model = sm.OLS(y, X).fit()

            betas.append(model.params["PEP"])

        result = prices.copy()

        result["Beta"] = betas

        logger.info("Rolling regression completed.")

        return result


def main():

    prices = StockUniverse.download()[["KO", "PEP"]]

    results = RollingRegression.hedge_ratio(prices)

    print()

    print(results.tail())


if __name__ == "__main__":
    main()
