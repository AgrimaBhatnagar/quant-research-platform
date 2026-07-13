# Quant Research Platform

A production-style quantitative research platform for developing, testing, and evaluating **statistical arbitrage (pairs trading)** strategies using Python.

The platform automates the complete research workflow from market data collection to strategy evaluation through rolling regression, cointegration analysis, dynamic backtesting, and an interactive Streamlit dashboard.

---

## Features

- Market data collection using Yahoo Finance
- Data preprocessing and cleaning
- Correlation analysis
- Engle-Granger Cointegration Test
- Rolling OLS Regression for Dynamic Hedge Ratio
- Spread and Z-Score calculation
- Statistical Arbitrage Signal Generation
- Dynamic Backtesting Engine
- Performance Analytics
- Interactive Streamlit Dashboard
- Automated Pair Discovery
- Research Pipeline for Multiple Assets

---

## Project Architecture

```
Market Data
      │
      ▼
Download & Preprocess
      │
      ▼
Correlation Analysis
      │
      ▼
Cointegration Testing
      │
      ▼
Rolling Regression
      │
      ▼
Spread Calculation
      │
      ▼
Signal Generation
      │
      ▼
Dynamic Backtesting
      │
      ▼
Performance Analytics
      │
      ▼
Interactive Dashboard
```

---

## Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Statistics | Statsmodels, SciPy |
| Visualization | Matplotlib, Plotly |
| Dashboard | Streamlit |
| Data Source | Yahoo Finance (yfinance) |

---

## Folder Structure

```
quant-research-platform
│
├── config/
├── dashboard/
├── src/
│   ├── analytics/
│   ├── backtesting/
│   ├── data/
│   ├── models/
│   ├── research/
│   ├── statistics/
│   ├── strategies/
│   ├── utils/
│   └── visualization/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Statistical Arbitrage Workflow

1. Download historical market data.
2. Identify highly correlated assets.
3. Test for cointegration.
4. Estimate rolling hedge ratios.
5. Compute the spread.
6. Calculate rolling Z-Scores.
7. Generate buy and sell signals.
8. Execute a dynamic backtest.
9. Evaluate performance using quantitative metrics.

---

## Performance Metrics

The platform evaluates strategies using:

- Total Return
- Annual Return
- Annual Volatility
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown

---

## Dashboard

Dashboard screenshots will be added here.

### Main Dashboard

```
Coming Soon
```

### Portfolio Performance

```
Coming Soon
```

### Trading Signals

```
Coming Soon
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/AgrimaBhatnagar/quant-research-platform.git

cd quant-research-platform
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Future Improvements

- Portfolio Optimization
- Bayesian Parameter Optimization
- Kalman Filter Hedge Ratio
- Multi-Pair Trading
- Transaction Cost Modeling
- Walk-Forward Validation
- Live Trading Support
- Docker Deployment

---

## Author

**Agrima Bhatnagar**

GitHub

https://github.com/AgrimaBhatnagar

---

## License

This project is licensed under the MIT License.
