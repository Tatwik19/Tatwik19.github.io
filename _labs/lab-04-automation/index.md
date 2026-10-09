---
title: "Lab 4: HMI and SCADA Development with Ignition"
lab_number: 4
lab_series: automation
course: "RAS 598: Industrial Robotics & Smart Factory Automation"
status: under-preparation
summary: "Build an operator interface for commanding, monitoring, alarming, and trending an automated workcell using Ignition and PLC data."
description: "An HMI and SCADA laboratory covering PLC tags, operator controls, alarms, trends, and diagnostic interface design."
topics:
  - Ignition
  - HMI and SCADA
  - Alarms and trends
layout: lab
permalink: /labs/lab-04-automation/
date: 2026-10-08
author_profile: false
classes: wide
hide_page_metadata: true
---

> **Status:** This laboratory is under preparation. The final Ignition gateway and tag-provider instructions will be added before release.

## Planned Scope

Students will connect an Ignition project to PLC data and create a clear operator interface for the material-handling cell developed in Lab 3. The interface will separate commands from status, expose machine state, and provide actionable diagnostics.

## Learning Outcomes

By the end of this laboratory, students should be able to:

- Connect an HMI/SCADA platform to an industrial controller.
- Organize and bind PLC tags to interface components.
- Design start, stop, reset, mode, and manual-control screens.
- Display machine state, permissives, and active faults.
- Configure alarms, acknowledgments, and historical trends.
- Apply operator-interface conventions that reduce ambiguity and misuse.

## Planned Workflow

1. Connect Ignition to the controller or simulated tag provider.
2. Import and organize the required tags.
3. Build the overview and control screens.
4. Add equipment status and diagnostic indicators.
5. Configure alarm priorities and acknowledgment.
6. Create process trends and event history.
7. Complete an operator usability and failure-mode test.

## Planned Deliverables

- Exported Ignition project or gateway backup.
- HMI screen hierarchy and navigation map.
- Alarm list with priorities and operator responses.
- Trend capture showing a complete machine cycle.
- Short usability review with proposed improvements.
