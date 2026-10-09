---
title: "Lab 3: Conveyor, Sensors, and Pneumatic Sequence Control"
lab_number: 3
lab_series: automation
course: "RAS 598: Industrial Robotics & Smart Factory Automation"
status: under-preparation
summary: "Integrate a conveyor, industrial sensors, and pneumatic actuators into an interlocked automatic material-handling sequence."
description: "A material-handling laboratory covering conveyor control, sensors, pneumatics, sequencing, and fault recovery."
topics:
  - Conveyors and sensors
  - Pneumatics
  - Sequence control
layout: lab
permalink: /labs/lab-03-automation/
date: 2026-10-08
author_profile: false
classes: wide
hide_page_metadata: true
---

> **Status:** This laboratory is under preparation. Final workstation assignments and pneumatic schematics will be added before release.

## Planned Scope

This laboratory applies PLC programming to a physical material-handling cell. Students will coordinate a conveyor, presence and position sensors, and pneumatic actuators while enforcing timing, motion, and safety constraints.

## Learning Outcomes

By the end of this laboratory, students should be able to:

- Interpret electrical and pneumatic schematics.
- Commission photoelectric, proximity, and position sensors.
- Control conveyor and solenoid-valve outputs from a PLC.
- Build an automatic sequence with sensor-confirmed transitions.
- Detect timeouts, jams, and invalid actuator states.
- Provide controlled manual operation for setup and recovery.

## Planned Workflow

1. Inspect the conveyor and pneumatic hardware.
2. Validate each sensor and actuator in manual mode.
3. Define the normal material-flow sequence.
4. Implement sensor-confirmed transitions.
5. Add timeout and jam detection.
6. Test emergency stop, reset, and recovery behavior.
7. Measure and document cycle performance.

## Planned Deliverables

- Electrical and pneumatic I/O map.
- Sequence diagram or state machine.
- PLC project with automatic and manual modes.
- Fault-injection and recovery test results.
- Demonstration video of the validated workcell cycle.
