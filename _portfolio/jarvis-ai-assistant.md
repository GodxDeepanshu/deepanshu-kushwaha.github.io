---
title: "J.A.R.V.I.S. — Planetary Intelligence & Situational Awareness System"
excerpt: "Planetary intelligence and situational awareness command center inspired by Stark Industries, featuring a 4K photorealistic 3D Earth, real-time CelesTrak SGP4 orbital tracking, live OpenSky ADS-B flight feeds, global news radar, and Stark AGI conversational engine."
collection: portfolio
---

**Status:** Completed (2025 – 2026)  
**Repository:** [GitHub: GodxDeepanshu/jarvis-ai-assistant](https://github.com/GodxDeepanshu/jarvis-ai-assistant)

## Overview
Inspired by Tony Stark's iconic J.A.R.V.I.S., this system is a real-time global intelligence and situational awareness command platform. It fuses live orbital mechanics, global civil and military aviation transponders, real-time geopolitical news feeds, and an interactive conversational AI interface into a unified cinematic glass cockpit.

## Key Subsystems & Engineering
- **Photorealistic 3D WebGL Earth:** Built using Three.js with realistic multi-layer surface textures, day/night terminators, dynamic cloud layers, specular ocean reflections, and orbital camera navigation.
- **Orbital Mechanics Engine:** Integrates real-time Two-Line Element (TLE) satellite ephemeris from CelesTrak, propagating orbital positions using SGP4 perturbation models in Web Workers.
- **Live ADS-B Flight Tracking:** Synchronizes live transponder broadcasts via the OpenSky Network, rendering 3D aircraft models with heading, true altitude, vertical climb/descent rates, and drop-down altitude ribbons.
- **Geographic News Intelligence:** Monitors international wire and RSS streams, geotagging real-time events to interactive coordinate citadels on the globe.
- **Stark AGI Conversational Engine:** Bidirectional voice and text agent equipped with system telemetry control, target interception protocols, and situational analysis.

## Tech Stack
- **Frontend:** HTML5, CSS3, Three.js, WebGL, Web Speech API
- **Backend:** Python, FastAPI, Uvicorn, SGP4, Skyfield
- **Data APIs:** CelesTrak, OpenSky Network, NewsAPI
