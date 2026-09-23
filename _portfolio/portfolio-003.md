---
title: "PLC-Controlled 3D-Filament Pellet Sorting Workstation"
collection: portfolio
date: 2022-04-28
project_period: "Jan 2022 – Apr 2022"
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

This project automated an SMC HAS-200 industrial workstation used to transport and sort boxed 3D-filament pellets. A Rockwell PLC coordinated pneumatic actuators, a vacuum pick-and-place mechanism, conveyor motion, barcode acquisition, operator controls, and tower-light feedback.

[View PLC project files]({{ page.repository_url }})

## Control Architecture

The ladder-logic program was divided into focused routines for machine reset, production sequencing, barcode reading, accept/reject sorting, magazine indexing, stop handling, and flasher timing. The main routine coordinated these subroutines and supported both physical push buttons and HMI commands.

The production sequence:

1. ejects a box from the magazine;
2. lowers and extends the vacuum head;
3. verifies that the box was captured;
4. transfers it to the conveyor;
5. releases the box and returns the mechanism home; and
6. advances the magazine for the next cycle.

Sensor checks and timers guard each transition. If the vacuum system fails to confirm a pickup within the allowed period, the sequence issues a stop instead of continuing with an unsafe or incomplete cycle.

## Barcode Sorting and HMI

The barcode routine validates the incoming transfer identifier and expected character length before copying the scan data. The sorting routine then extracts the encoded color value and actuates the reject cylinder when a box does not meet the acceptance condition.

The SCADA/HMI interface exposes start, stop, reset, automatic, and manual operations while displaying machine state for testing and troubleshooting.

## My Contributions

- Developed and debugged ladder-logic routines for coordinated workstation operation.
- Integrated industrial sensors, pneumatic actuators, conveyor logic, and barcode data.
- Built SCADA/HMI controls for automatic and manual operation.
- Added interlocks, sensor verification, timers, and stop/reset behavior to improve safe recovery.

## Demonstrations

[Automatic mode video](https://drive.google.com/file/d/1nFZ3G9hHAkfYh79k1DYMpi_41WU68J7D/view?usp=drive_link) · [Manual mode video](https://drive.google.com/file/d/1KCGYvSb65EKQRfCQ9AiHpFBMndduPnzX/view?usp=drive_link)

![SCADA interface]({{ page.featured_image }})
