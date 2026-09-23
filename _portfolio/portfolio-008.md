---
title: "Robo_SIM: Manipulator Dynamics and Force-Control Package"
collection: portfolio
date: 2024-04-30
project_period: "Apr 2024"
summary: "Developed a MATLAB robotics package for user-defined manipulators, dynamics simulation, compliance control, impedance control, and interactive analysis."
role: "Manipulator dynamics, force-control simulation, and GUI development"
featured_image: "https://raw.githubusercontent.com/thulsonASU/robot_sim/main/images/DHGUI_3R.png"
featured_image_alt: "Robo_SIM Denavit-Hartenberg parameter interface"
technologies:
  - MATLAB
  - Simulink
  - Robot dynamics
  - Compliance control
  - Impedance control
repository_url: "https://github.com/thulsonASU/robot_sim"
---

## Project Overview

Robo_SIM is a MATLAB package for modeling and studying the dynamics and force control of serial robotic manipulators. A user supplies a Denavit–Hartenberg table, configures the simulation through a graphical interface, and analyzes the resulting joint and end-effector behavior.

[View repository]({{ page.repository_url }})

## Core Capabilities

### Dynamics Simulation

The package derives the manipulator equations of motion and simulates joint position, velocity, and acceleration for a selected mechanism and input trajectory. The plots expose both transient and steady-state behavior for model checking and controller evaluation.

### Compliance Control

The compliance-control module combines proportional-derivative control with gravity compensation. It lets the end effector yield to external interaction forces while tracking a desired motion, and plots desired versus actual end-effector position together with contact force.

### Impedance Control

The impedance controller uses inverse dynamics to shape the relationship between motion and environmental force. This provides a second indirect force-control strategy for comparing tracking behavior and interaction response.

### Interactive GUI

The interface organizes DH-table entry, robot generation, simulation parameters, controller selection, and plotting so that users can explore different manipulators without rewriting the full analysis pipeline.

## My Contributions

- Implemented and tested manipulator-dynamics calculations and simulation workflows.
- Developed force-control functionality for compliance and impedance experiments.
- Contributed to the interactive GUI and result visualization.
- Integrated user-defined robot geometry with the dynamics and control modules.

## Outcome

The completed package provides a reusable educational environment for moving from kinematic description to dynamic simulation and force-control analysis. It supports rapid comparison of controller behavior while keeping the underlying robot model configurable.

![DH parameter interface]({{ page.featured_image }})

![Dynamics simulation interface](https://raw.githubusercontent.com/thulsonASU/robot_sim/main/images/DySimGUI_3R.png)
