---
title: "Kinematic Modeling of Milky Way Open Clusters"
excerpt: "Automated astronomical kinematic pipeline computing 3D space velocities (U, V, W) and proper motions from Gaia DR3 survey data with Minimum Spanning Tree spatial clustering."
collection: portfolio
---

**Status:** Completed (2025)  
**Repository:** [GitHub: GodxDeepanshu/milkyway-open-cluster-kinematics](https://github.com/GodxDeepanshu/milkyway-open-cluster-kinematics)

## Overview
Open star clusters in the Milky Way disc provide crucial empirical anchors for understanding galactic stellar dynamics, star formation histories, and tidal destruction processes. This project constructs an automated processing and analysis pipeline for large-scale stellar kinematic surveys.

## Key Features & Algorithms
- **3D Space Velocity Derivation:** Computes full Galactocentric velocity vectors $(U, V, W)$ by combining right ascension, declination, radial velocities, and proper motions from the Gaia Data Release 3 (DR3).
- **Minimum Spanning Tree (MST) Clustering:** Applies graph-theoretic Minimum Spanning Tree algorithms to cluster coordinate manifolds to extract characteristic cluster radii, density gradients, and quantitative mass segregation indices ($\Lambda_{MSR}$).
- **Tidal Disruption Analysis:** Analyzes velocity dispersions to distinguish dynamically bound cluster members from unbound field star interlopers.

## Tech Stack
- **Languages & Scientific Libraries:** Python, AstroPy, NumPy, SciPy, Matplotlib, NetworkX
