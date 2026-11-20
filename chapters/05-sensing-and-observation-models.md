# Chapter 05 — Sensing and observation models

> **Status:** stub. **License:** CC BY-NC 4.0. **Hardware:** simulation only.

## Learning goals

- Describe typical Limo Pro sensor suite (LiDAR, IMU, cameras — per vendor docs).
- Write observation models that connect state to measurements.
- Noise, bias, and calibration as first-class course topics.

## Outline

1. Sensors on the course platform (sim placeholders first).
2. Range-bearing and occupancy observations.
3. IMU preintegration intuition (lightweight).
4. Time sync and ROS 2 message models.
5. Lab: inspect simulated scan / IMU topics; plot noise statistics.

## Adaptation notes

- Reuse existing Limo / Gazebo sensor plugins rather than authoring new ones.
