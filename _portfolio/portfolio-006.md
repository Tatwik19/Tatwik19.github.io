---
title: "SoulTech: Portable Gait-Analysis and Feedback Device"
collection: portfolio
date: 2023-05-01
project_period: "Jan 2023 – May 2023"
summary: "Developed pressure-sensing footwear with inertial measurement, Bluetooth telemetry, and haptic feedback for portable gait assessment."
role: "Embedded-system prototyping, sensor integration, and gait-analysis software"
featured_image: "https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/CAD-Design.png"
featured_image_alt: "CAD design of the SoulTech portable gait-analysis device"
technologies:
  - Arduino Nano 33 IoT
  - Pressure sensing
  - IMU
  - Bluetooth
  - Haptic feedback
repository_url: "https://github.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device"
---

## Project Overview

SoulTech is a portable gait-analysis prototype developed to make pressure and motion measurements available outside a fixed gait laboratory. The system places pressure-sensitive elements in footwear and combines them with an ankle-mounted embedded module for inertial sensing, wireless data transfer, and real-time haptic feedback.

[View repository]({{ page.repository_url }})

## Problem and Objectives

Traditional gait-analysis systems can require specialized facilities and expensive equipment. In consultation with practitioners at Barrow Neurological Institute, the project focused on a lightweight platform that could capture useful walking characteristics while remaining wearable and easy to transport.

The target measurements included pressure distribution, initial foot contact, stance time, stride behavior, cadence, and spatial movement. The haptic channel was intended to provide an immediate cue when the measured gait departed from a desired pattern.

## System Design

An Arduino Nano 33 IoT acquired eight analog pressure channels and data from its integrated IMU. The software combined accelerometer and gyroscope measurements with filtering and coordinate transformations to estimate device motion. Bluetooth provided live telemetry to an external interface, while a linear vibration motor supplied feedback to the wearer.

The pressure elements were connected through conductive traces in the sole, and the controller, battery, IMU, and vibration hardware were packaged in a detachable ankle enclosure. This modular arrangement kept the sensing layer flexible and allowed the electronics to be removed for maintenance or cleaning.

## My Contributions

- Prototyped the pressure-sensing and embedded-electronics architecture.
- Integrated multi-channel analog acquisition, IMU data, Bluetooth communication, and haptic output.
- Contributed to filtering and gait-feature calculations for stance, contact, stride, and cadence analysis.
- Supported CAD packaging, requirements development, testing, and technical documentation.

## Outcome and Next Steps

The prototype demonstrated simultaneous pressure acquisition, inertial measurement, wireless telemetry, and haptic actuation in a portable form. It was an engineering prototype, not a clinical device; future work identified in the project includes improved calibration, more robust signal filtering, longer-term validation, and integration with additional wearable or rehabilitation systems.

![SoulTech CAD design]({{ page.featured_image }})

## Acknowledgments

Developed for EGR 555 with guidance from Prof. Troy McDaniel and feedback from Joelly Lobato De Faria and Kyle Sandoval at Barrow Neurological Institute.
