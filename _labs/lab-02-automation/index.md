---
title: "Lab 2: PLC Programming with Ladder Logic and Structured Text"
lab_number: 2
lab_series: automation
course: "RAS 598: Industrial Robotics & Smart Factory Automation"
status: under-preparation
summary: "Develop, test, and troubleshoot PLC programs using Ladder Logic, Structured Text, timers, counters, interlocks, and reusable routines."
description: "A PLC programming laboratory covering Ladder Logic, Structured Text, sequencing, interlocks, and controller diagnostics."
topics:
  - Ladder Logic
  - Structured Text
  - Interlocks and diagnostics
layout: lab
permalink: /labs/lab-02-automation/
date: 2026-10-08
author_profile: false
classes: wide
hide_page_metadata: true
---

> **Status:** This laboratory is under preparation. The final controller project and acceptance tests will be published before release.

## Planned Scope

Students will create a maintainable PLC application that controls a small automation sequence. The exercise will compare Ladder Logic and Structured Text while emphasizing clear tag naming, modular routines, permissives, interlocks, and fault recovery.

## Learning Outcomes

By the end of this laboratory, students should be able to:

- Create controller tags and organize a PLC project.
- Implement seal-in, one-shot, timer, and counter logic.
- Express control decisions in Ladder Logic and Structured Text.
- Separate operating commands, machine states, and physical outputs.
- Add permissives and interlocks that prevent unsafe transitions.
- Diagnose a sequence using online monitoring and controller status data.

## Planned Workflow

1. Create the controller project and tag structure.
2. Program start, stop, reset, and mode-selection behavior.
3. Implement a multi-step automatic sequence.
4. Add manual controls for commissioning.
5. Introduce and diagnose test faults.
6. Verify safe restart and recovery behavior.
7. Compare equivalent Ladder Logic and Structured Text routines.

## Planned Deliverables

- PLC project archive and exported routines.
- State or sequence diagram.
- I/O and tag documentation.
- Test table covering normal operation, faults, and recovery.
- Screenshots of the online logic during validation.
