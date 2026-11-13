---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
redirect_from:
  - /research.html
---

{% include base_path %}

My academic research lies at the convergence of **statistical machine learning, astrophysical survey science, quantitative modeling, and resilient distributed systems**. I focus on formulating principled mathematical models and computational pipelines to extract actionable insights from large, complex, and noisy empirical datasets.

---

## Primary Research Thrusts

### 1. Deep Learning for Astrophysical Surveys & AGN Redshift Estimation
* **Focus:** Non-linear cosmological redshift ($z$) estimation from multi-band photometric survey catalogs.
* **Problem & Methods:** Spectroscopic confirmation for high-redshift Active Galactic Nuclei (AGN) is constrained by telescope time and observational resources. By harmonizing disparate optical, infrared, and X-ray photometric bands and engineering physical color-index differentials, I train deep neural ensembles and gradient-boosted trees that model non-linear celestial SEDs, decreasing root-mean-squared error by 20% over traditional photometric baselines.
* **Keywords:** `Computational Astrophysics`, `Photometric Redshifts`, `AstroPy`, `Ensemble Deep Learning`, `Survey Harmonization`.

### 2. Galactic Dynamics & Kinematic Star Cluster Modeling
* **Focus:** 3D Galactocentric stellar kinematics and spatial segregation using Gaia DR3 astrometric data.
* **Problem & Methods:** Investigating the dynamical relaxation, mass segregation, and tidal dissolution of open clusters within the Milky Way disc. By computing full $(U, V, W)$ space velocity vectors from proper motions, parallaxes, and radial velocities, and deploying Minimum Spanning Tree (MST) graph algorithms to compute mass segregation indices ($\Lambda_{MSR}$), our pipelines delineate dynamically bound cluster members from field stars.
* **Keywords:** `Stellar Kinematics`, `Gaia DR3`, `Minimum Spanning Tree`, `Galactic Dynamics`, `Graph Algorithms`.

### 3. Quantitative Financial Modeling & Stochastic Risk Optimization
* **Focus:** High-dimensional portfolio risk estimation, tail-event modeling, and dynamic asset allocation.
* **Problem & Methods:** Modeling non-Gaussian asset returns and estimating extreme drawdown exposures through 10,000+ path Monte Carlo simulations. Integrating parametric and historical Value-at-Risk (VaR) and Conditional VaR (CVaR / Expected Shortfall) with quadratic programming along the Markowitz Efficient Frontier, augmented with fine-tuned NLP headline sentiment alpha for real-time risk reweighting.
* **Keywords:** `Quantitative Finance`, `Monte Carlo Methods`, `Markowitz Optimization`, `Value at Risk (VaR/CVaR)`, `NLP Sentiment`.

### 4. Low-Bandwidth Distributed Systems & Resilient Real-Time Protocols
* **Focus:** Adaptive real-time media transmission over degraded mobile networks in underserved regions.
* **Grant & Support:** Supported by an international Seed Grant from the **Aspire Institute** (founded by Harvard Business School faculty).
* **Problem & Methods:** Designing custom WebRTC compression frameworks, hardware codec parameter tuning, and low-latency state synchronization mechanisms that reduce video and audio bandwidth overhead by over 60%, delivering smooth digital classroom experiences over fragile 2G/3G connectivity.
* **Keywords:** `WebRTC`, `Distributed Systems`, `Adaptive Bitrate`, `Offline-First Architecture`.

---

## Research Milestones & Grants
* **Aspire Institute Seed Fund Grant ($500 Seed Funding):** Awarded by Harvard Business School faculty for innovative technological solutions addressing rural educational inequity.
* **Reliance Foundation Undergraduate STEM Scholarship:** Awarded competitive merit fellowship (top 5,000 nationwide from 1,000,000+ applicants) supporting academic excellence throughout the undergraduate curriculum.
* **Paradox 2025 (IIT Madras):** Participated in advanced workshops on *Building Trustworthy AI through Data Quality*, focusing on fairness metrics, algorithmic bias auditing, SHAP/LIME explainability, and adversarial robustness.
