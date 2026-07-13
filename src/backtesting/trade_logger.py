"""
Trade Logger
"""

from __future__ import annotations

import pandas as pd


class TradeLogger:

    @staticmethod
    def generate(results: pd.DataFrame) -> pd.DataFrame:

        trades = []

        current_position = 0

        entry_index = None
        entry_spread = None

        trade_id = 1

        for idx, row in results.iterrows():

            signal = row["Signal"]

            # --------------------------
            # Open Trade
            # --------------------------

            if current_position == 0 and signal != 0:

                current_position = signal

                entry_index = idx

                entry_spread = row["Spread"]

            # --------------------------
            # Close Trade
            # --------------------------

            elif current_position != 0 and signal == 0:

                exit_index = idx

                exit_spread = row["Spread"]

                pnl = current_position * (
                    exit_spread - entry_spread
                )

                trades.append(
                    {
                        "TradeID": trade_id,
                        "Direction": (
                            "Long"
                            if current_position == 1
                            else "Short"
                        ),
                        "EntryIndex": entry_index,
                        "ExitIndex": exit_index,
                        "EntrySpread": entry_spread,
                        "ExitSpread": exit_spread,
                        "PnL": pnl,
                        "HoldingDays":
                            exit_index - entry_index,
                    }
                )

                trade_id += 1

                current_position = 0

        return pd.DataFrame(trades)
