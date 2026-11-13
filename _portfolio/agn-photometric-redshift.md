---
title: "Active Galactic Nuclei (AGN) Photometric Redshift Prediction"
excerpt: "Ensemble deep learning and gradient-boosted pipeline predicting photometric redshifts (z) of Active Galactic Nuclei across multi-band astronomical survey catalogs."
collection: portfolio
---

**Status:** Completed (2025)

## Overview
Active Galactic Nuclei (AGN) are extremely energetic galactic cores powered by supermassive black holes. Estimating their cosmological redshifts ($z$) via spectroscopic methods is computationally and observationally expensive. This project develops an end-to-end machine learning pipeline to accurately predict $z$ purely from multi-band photometric flux measurements.

## Key Contributions & Methodology
- **Multi-Band Catalog Ingestion:** Ingested and cross-matched multi-wavelength astronomical survey data spanning optical, mid-infrared, and X-ray bands.
- **Feature Engineering:** Formulated synthetic celestial color-index differentials ($u-g, g-r, r-i, i-z, z-W1, W1-W2$) and designed specialized imputation algorithms for non-detections in high-frequency bands.
- **Ensemble Model:** Constructed an ensemble combining deep feed-forward neural networks in PyTorch with LightGBM and XGBoost gradient boosters.
- **Results:** Achieved an **8% improvement in Pearson correlation** and a **20% reduction in Root Mean Squared Error (RMSE)** relative to published single-model astronomical baselines.

## Tech Stack
- **Languages & Libraries:** Python, PyTorch, AstroPy, Scikit-learn, LightGBM, XGBoost, Pandas, NumPy
