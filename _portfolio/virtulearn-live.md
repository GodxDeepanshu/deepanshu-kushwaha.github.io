---
title: "VirtuLearn Live — Low-Bandwidth Real-Time Interactive Classroom"
excerpt: "Ultra-low-bandwidth, low-latency live study ecosystem tailored for tier-2/3 towns and rural students facing unstable network conditions. Funded by an international Seed Grant from the Aspire Institute (founded by Harvard Business School faculty)."
collection: portfolio
---

**Status:** Active Development (Jul 2026 – Present)  
**Funding & Honors:** Awarded a Seed Grant from the **Aspire Institute** (founded by Harvard Business School Professors Tarun Khanna and Karim Lakhani) in recognition of technological innovation and social impact in democratizing digital education.

## Overview
VirtuLearn Live is an end-to-end mobile and cloud interactive learning ecosystem engineered specifically for students in tier-2/3 cities and rural communities where unstable 2G/3G connectivity severely limits participation in standard video conferencing tools (Zoom, Google Meet).

## Key Innovations & Technical Architecture
- **Adaptive Bitrate Compression:** Designed a customized audio/video pipeline combining WebRTC, hardware codecs, and dynamic network quality probing that reduces total data consumption by **over 60%** relative to standard enterprise video tools.
- **Collaborative Whiteboard Engine:** Implemented real-time vectorized strokes synchronization over WebSockets and Firebase Realtime Database, enabling interactive instruction at sub-50ms sync latencies.
- **Offline-First Resilience:** Integrated client-side state caching with SQLite and Jetpack Room, ensuring continuous lecture audio playback and state restoration during intermittent dropouts.

## Tech Stack
- **Mobile Client:** Kotlin, Android SDK, Jetpack Compose, WebRTC Android Native bindings
- **Backend & Cloud:** Node.js, WebSockets, Firebase Realtime Database & Authentication
- **Media Optimization:** H.264 / VP8 baseline profiles, Opus adaptive audio bitrate encoding
