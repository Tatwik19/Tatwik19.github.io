---
title: "PLC-Controlled 3D-Filament Pellet Sorting Workstation"
collection: portfolio
date: 2022-04-28
project_period: "Jan 2022 - Apr 2022"
summary: "Automated an SMC HAS-200 workstation with Rockwell ladder logic, barcode-based sorting, pneumatic handling, and SCADA/HMI controls."
role: "PLC programming, sequence control, and HMI/SCADA development"
featured_image: "https://raw.githubusercontent.com/Tatwik19/Tatwik19.github.io/master/assets/Projects/HAS%20PLC/SCADA.png"
featured_image_alt: "SCADA interface for the automated pellet sorting workstation"
technologies:
  - Rockwell PLC
  - Studio 5000 Logix Designer
  - Ladder logic
  - SCADA
  - HMI
repository_url: "https://github.com/Tatwik19/Tatwik19.github.io/tree/master/assets/Projects/HAS%20PLC"
---

## Project Overview

This project automated an SMC HAS-200 workstation for 3D-filament pellet sorting. A Rockwell PLC coordinated the magazine, conveyor, pneumatic handling, vacuum pick-and-place, barcode validation, accept/reject logic, and operator controls.

[PLC project files]({{ page.repository_url }}) · [Automatic mode video](https://drive.google.com/file/d/1nFZ3G9hHAkfYh79k1DYMpi_41WU68J7D/view?usp=drive_link) · [Manual mode video](https://drive.google.com/file/d/1KCGYvSb65EKQRfCQ9AiHpFBMndduPnzX/view?usp=drive_link)

## Control System at a Glance

| System | Implementation |
|---|---|
| PLC | Rockwell PLC programmed in Studio 5000 Logix Designer |
| Programming | Ladder logic with modular routines |
| Material handling | Magazine index, conveyor, pneumatic cylinders, and vacuum pickup |
| Identification | Barcode reader with transfer-ID validation |
| Sorting | Accept/reject decision with reject-cylinder actuation |
| Operator interface | HMI/SCADA start, stop, reset, automatic, and manual controls |
| Safety and recovery | Interlocks, sensor checks, timers, stop logic, and machine reset |
| Status feedback | Tower lights and HMI machine-state feedback |

## PLC Routines

- **AA Main Routine:** Coordinates the machine sequence and calls the control routines.
- **Production:** Runs the automatic pick, transfer, release, and magazine-index cycle.
- **Barcode Reader:** Validates the scanned identifier and extracts sorting data.
- **Accept Reject Box:** Controls the reject cylinder for nonconforming boxes.
- **Magazine Index:** Advances the next box into position.
- **Machine Reset:** Returns the workstation to a known start state.
- **Stop:** Handles operator and fault stops.
- **Flasher Timers:** Controls timed status and tower-light behavior.

## My Contributions

- Developed and debugged modular ladder-logic routines for the complete workstation sequence.
- Integrated barcode data, sensors, pneumatic actuators, conveyor motion, and vacuum handling.
- Built HMI/SCADA controls for automatic and manual operation.
- Implemented interlocks, timers, sensor verification, stop handling, and reset recovery.

## Results

The completed control system demonstrated automatic and manual workstation operation, barcode-based sorting, coordinated pneumatic handling, and operator-visible machine status through the HMI/SCADA interface.

![SCADA interface]({{ page.featured_image }})
