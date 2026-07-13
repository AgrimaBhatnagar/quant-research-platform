"""
Project configuration.
"""

from pathlib import Path

# =====================================================
# Project Paths
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

OUTPUT_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"
METRICS_DIR = OUTPUT_DIR / "metrics"
TRADES_DIR = OUTPUT_DIR / "trades"
RESEARCH_DIR = OUTPUT_DIR / "research"

for directory in [
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    FIGURES_DIR,
    METRICS_DIR,
    TRADES_DIR,
    RESEARCH_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

# =====================================================
# Data
# =====================================================

START_DATE = "2018-01-01"
END_DATE = None

DEFAULT_PAIR = ["KO", "PEP"]

UNIVERSE = [
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

# =====================================================
# Strategy Parameters
# =====================================================

ENTRY_Z = 2.0
EXIT_Z = 0.5

ROLLING_WINDOW = 30
REGRESSION_WINDOW = 252

INITIAL_CAPITAL = 100000

COMMISSION = 0.001
SLIPPAGE = 0.0005

TRADING_DAYS = 252