---
title: "Lab 6: Smart Factory Integration, MQTT, and Digital Twins"
lab_number: 6
lab_series: automation
course: "RAS 598: Industrial Robotics & Smart Factory Automation"
status: under-preparation
summary: "Connect the automated workcell to a smart-manufacturing data layer using MQTT, dashboards, production metrics, and a digital representation of system state."
description: "A capstone smart-factory laboratory covering MQTT, production data, diagnostics, dashboards, and digital-twin validation."
topics:
  - MQTT and industrial data
  - Digital twins
  - Smart manufacturing
layout: lab
permalink: /labs/lab-06-automation/
date: 2026-10-08
author_profile: false
classes: wide
hide_page_metadata: true
---

> **Status:** This laboratory is under preparation. The final data architecture and dashboard requirements will be published before release.

## Planned Scope

The final laboratory combines the controller, material-handling system, HMI, and robot into a connected smart-manufacturing workflow. Students will publish selected machine data through MQTT, calculate production metrics, and compare physical workcell behavior with a digital representation.

## Learning Outcomes

By the end of this laboratory, students should be able to:

- Select useful controller data for supervisory monitoring.
- Publish structured machine data through Python-based MQTT integration.
- Distinguish commands, state, events, alarms, and historical measurements.
- Calculate cycle time, throughput, downtime, and fault metrics.
- Build a dashboard that communicates system health and production state.
- Validate synchronization between a physical system and its digital representation.

## Planned Workflow

1. Define the workcell data model and topic hierarchy.
2. Publish controller and HMI data to an MQTT broker.
3. Subscribe, timestamp, and validate the message stream.
4. Calculate production and diagnostic metrics.
5. Build the monitoring dashboard.
6. Connect the live data to a digital model or simulation.
7. Run the capstone acceptance test and document discrepancies.

## Planned Deliverables

- System architecture and data-flow diagram.
- MQTT topic and payload specification.
- Python integration code and configuration files.
- Dashboard showing production and diagnostic metrics.
- Digital-twin comparison and synchronization results.
- Final demonstration and engineering report.
