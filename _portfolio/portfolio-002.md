---
title: "Bluetooth Robot Arm with Forward and Inverse Kinematics"
collection: portfolio
date: 2021-12-01
project_period: "Aug 2021 – Dec 2021"
summary: "Combined MATLAB kinematics with Bluetooth-based servo control to position a robotic arm and record repeatable motion sequences."
role: "Kinematics, MATLAB analysis, and embedded motion control"
technologies:
  - MATLAB
  - Arduino
  - C++
  - Bluetooth
  - Servo control
repository_url: "https://github.com/Tatwik19/Tatwik19.github.io/tree/master/assets/Projects/3DoF%20Robot"
---

## Project Overview

This project explored robotic-arm positioning through two connected components: a MATLAB kinematics model and an Arduino-based Bluetooth controller for the physical arm. The repository describes the mechanism as a 3-DoF robot-arm study, while the physical controller coordinates six servo channels for the assembled platform.

[View project files]({{ page.repository_url }})

## Kinematics

The MATLAB model constructs homogeneous transformation matrices from the robot geometry and symbolic joint angles. It supports:

- forward kinematics for calculating the end-effector pose from joint inputs;
- inverse-kinematics calculations for reaching a requested Cartesian target; and
- visualization and checking of the arm geometry before commanding hardware.

This separated geometric reasoning from low-level actuator control and made it easier to evaluate candidate configurations before moving the arm.

## Embedded Control

The Arduino controller communicates through an HC-05 Bluetooth module and drives the servo set with incremental motion rather than abrupt position jumps. The control program supports direct joint commands, adjustable movement speed, saved arm positions, sequence playback, and reset behavior.

## My Contributions

- Developed and evaluated the forward- and inverse-kinematics calculations in MATLAB.
- Implemented Bluetooth command handling for interactive arm control.
- Programmed smooth servo interpolation and position-sequence recording for repeatable motion.
- Integrated the analytical model with the constraints of the physical servo-driven arm.

## Outcome

The result was a compact educational platform for connecting manipulator mathematics to real actuator behavior. It demonstrated how target-position calculations, Bluetooth commands, and coordinated servo motion can be organized into a repeatable robot-arm workflow.
