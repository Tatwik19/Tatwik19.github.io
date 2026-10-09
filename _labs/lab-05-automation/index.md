---
title: "Lab 5: Collaborative Robot and PLC Integration"
lab_number: 5
lab_series: automation
course: "RAS 598: Industrial Robotics & Smart Factory Automation"
status: under-preparation
summary: "Integrate a FANUC or Universal Robots platform with a PLC, exchange commands and status, and validate an interlocked workcell sequence."
description: "An industrial robot integration laboratory covering robot programming, PLC handshakes, interlocks, and workcell validation."
topics:
  - FANUC and Universal Robots
  - PLC handshakes
  - Workcell integration
layout: lab
permalink: /labs/lab-05-automation/
date: 2026-10-08
author_profile: false
classes: wide
hide_page_metadata: true
---

> **Status:** This laboratory is under preparation. Robot-specific safety and programming instructions will be finalized for each workstation.

## Planned Scope

This laboratory connects an industrial or collaborative robot to the automation cell. Students will create a robot task, exchange command and status signals with the PLC, and validate a deterministic handshake for starting, completing, and recovering the cycle.

## Learning Outcomes

By the end of this laboratory, students should be able to:

- Apply robot-cell startup, recovery, and safe-teaching procedures.
- Define tool, user, and work-object coordinate frames.
- Program and validate a basic pick-and-place routine.
- Exchange commands, status, and fault signals with a PLC.
- Implement robot-ready, start, busy, complete, and fault handshakes.
- Prevent conflicting motion through PLC and robot interlocks.

## Planned Workflow

1. Inspect the robot cell and verify safety functions.
2. Configure frames, payload, tool, and operating speed.
3. Teach and test the robot task at reduced speed.
4. Map robot and PLC communication signals.
5. Implement the command/status handshake.
6. Integrate the robot with the conveyor sequence.
7. Test cycle completion, interrupted operation, and fault recovery.

## Planned Deliverables

- Robot program and frame configuration record.
- PLC–robot signal map and handshake diagram.
- Integrated controller project.
- Safety and recovery validation checklist.
- Demonstration video of the complete workcell cycle.
