---
title: "AI-Driven Quantitative Portfolio Risk Advisor"
excerpt: "Institutional-grade portfolio risk engine executing Monte Carlo simulations (10,000+ iterations), Markowitz Efficient Frontier optimization, and NLP headline sentiment alpha."
collection: portfolio
---

**Status:** Completed (2025 – 2026)  
**Repository:** [GitHub: GodxDeepanshu/portfolio-risk-advisor](https://github.com/GodxDeepanshu/portfolio-risk-advisor)

## Overview
An institutional-grade quantitative risk modeling and decision-support system designed to evaluate multi-asset portfolios under varying market regimes, stress-test extreme downside volatility, and rebalance assets along the Markowitz Efficient Frontier.

## Key Features & Quantitative Architecture
- **Stochastic Risk Simulation:** Executes 10,000+ Monte Carlo paths to generate probabilistic future wealth distributions and compute Parametric and Historical Value at Risk (VaR 95%/99%) as well as Conditional Value at Risk (CVaR / Expected Shortfall).
- **Markowitz Optimization:** Computes quadratic programming optimization for minimum volatility and maximum Sharpe ratio allocations with custom leverage and sector exposure bounds.
- **NLP Sentiment Alpha:** Integrates financial news sentiment analysis (using fine-tuned Transformer pipelines) that adjusts volatility forecasts and dynamically penalizes vulnerable equity weights.
- **Production Architecture:** Fully containerized with Docker, featuring automated REST API endpoints for portfolio metrics, covariance matrices, and visualization charts.

## Tech Stack
- **Languages & Frameworks:** Python, NumPy, Pandas, PyTorch, SciPy, Matplotlib
- **Financial Tooling:** Yahoo Finance / AlphaVantage APIs, CVXPY Quadratic Solver
- **Infrastructure:** Docker, FastAPI, Pytest
