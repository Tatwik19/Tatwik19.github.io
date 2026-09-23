---
title: "AeroFusion: Autonomous BLIMP Navigation and Sensor Integration"
collection: portfolio
date: 2025-04-30
project_period: "Spring 2025"
summary: "Built a modular ROS 2 platform that combines vision, inertial sensing, altitude estimation, control allocation, and browser-based telemetry for an autonomous indoor BLIMP."
role: "ROS 2 integration, perception, sensor fusion, controls, and system validation"
featured_image: "https://ras598-2025-s-team03.github.io/figures/blimp_model.JPG"
featured_image_alt: "CAD model of the AeroFusion lighter-than-air robot"
technologies:
  - ROS 2 Humble
  - Raspberry Pi
  - C++
  - Python
  - OpenCV
  - YOLOv5
project_url: "https://ras598-2025-s-team03.github.io/"
repository_url: "https://github.com/RAS598-2025-S-Team03/BLIMP-Packages"
---

## Project Overview

AeroFusion is an autonomous navigation and sensor-integration platform for a biologically inspired lighter-than-air robot. The system was designed for dynamic indoor environments where a BLIMP must detect and approach a visual target while maintaining stable motion with limited onboard sensing and actuation.

[View project website]({{ page.project_url }}) · [View ROS 2 packages]({{ page.repository_url }})

## System Architecture

The platform uses a Raspberry Pi and a modular ROS 2 stack. Camera images feed a custom YOLOv5 detector, which estimates a target's image-plane location. IMU and barometer nodes provide attitude and altitude measurements. The control stack combines these signals into body-force requests, maps the requested forces to the available thrusters with a Moore–Penrose pseudo-inverse, and converts the result to ESC commands.

```text
Camera → Target detection ─┐
IMU ───────────────────────┼→ State and force estimation → Thruster allocation → ESCs
Barometer ─────────────────┘
```

Manual joystick commands and autonomous commands pass through a mode-switch node before reaching the ESC driver, preserving a direct operator-control path during testing.

## Perception, Control, and Telemetry

- A custom YOLOv5 model and quadrant logic provide target tracking.
- PI and differential-control components generate motion commands.
- IMU and barometer filtering stabilize attitude and altitude estimates.
- A browser interface built with rosbridge, roslibjs, and web-video streaming displays telemetry and live imagery.
- Explicit ROS 2 topics and launch files keep sensing, estimation, control, actuation, and user-interface functions separable.

## My Contributions

- Contributed to the ROS 2 node architecture and interface integration.
- Supported visual perception, sensor processing, and autonomous-control development.
- Integrated camera, IMU, barometer, joystick, and ESC workflows.
- Contributed to documentation, launch configuration, and system-level testing.

## Validation

The team characterized the propulsion system on a thrust stand and used those relationships in the control-allocation model. SolidWorks mass properties, added-mass estimates, flight-test damping observations, and Vicon motion tracking supported the dynamic model and experimental validation.

![AeroFusion BLIMP model]({{ page.featured_image }})

![Browser-based ROS telemetry interface](https://ras598-2025-s-team03.github.io/figures/blimp_gui.png)

## Team

Sai Srinivas Tatwik Meesala, Nihar Masurkar, and Prajjwal Dutta.
