---
title: "Not Creepy Elf: Interactive Holiday Animatronic"
collection: portfolio
date: 2021-12-06
project_period: "Aug 2021 – Dec 2021"
summary: "Designed and built a dual-mode holiday animatronic around a custom PSoC-based PCB, motion sensing, motor control, LEDs, and Bluetooth communication."
role: "Embedded systems, PCB design, and prototype integration"
featured_image: "https://raw.githubusercontent.com/Tatwik19/Tatwik19.github.io/master/assets/Projects/Final%20Design%20-%20Not%20Creepy%20Elf/PCB%20photos/FRONT%20-%20TATWIK.jpg"
featured_image_alt: "Front of the custom Not Creepy Elf printed circuit board"
technologies:
  - PSoC 4100S Plus
  - C
  - Cadence Allegro
  - Bluetooth Low Energy
  - PCB design
repository_url: "https://github.com/Tatwik19/Tatwik19.github.io/tree/master/assets/Projects/Final%20Design%20-%20Not%20Creepy%20Elf"
report_url: "https://raw.githubusercontent.com/Tatwik19/Tatwik19.github.io/master/assets/Projects/Final%20Design%20-%20Not%20Creepy%20Elf/00_Final_Report.pdf"
---

## Project Overview

Not Creepy Elf is an electronic decoration designed to switch between a playful Christmas character and a motion-activated Halloween animatronic. The project combined embedded hardware, firmware, sensing, lighting, and mechanical actuation in a compact prototype.

[View project files]({{ page.repository_url }}) · [Read the final report]({{ page.report_url }})

## System Design

The prototype used a PSoC 4100S Plus microcontroller and a custom PCB designed in Cadence Allegro. Its main subsystems were:

- a PIR sensor for motion detection;
- an analog accelerometer for orientation and movement sensing;
- a temperature sensor using I²C communication;
- a DC motor and motor driver controlled with PWM;
- eye LEDs and a diagnostic LED; and
- Bluetooth Low Energy communication for selecting the operating mode.

When motion was detected, the firmware activated different motor and lighting sequences for the Christmas and Halloween modes. The final implementation also used accelerometer input to vary LED brightness.

## My Contributions

- Designed, assembled, and debugged an individual custom PCB for the shared team architecture.
- Integrated the PSoC, sensor, motor-driver, LED, power, and communication circuits.
- Supported firmware development and hardware bring-up across the sensing and actuation subsystems.
- Helped revise the design when component compatibility and schedule constraints required a stepper-to-DC-motor change and replacement of the planned RFID reader.

## Results and Lessons Learned

The final prototype demonstrated motion-triggered behavior, LED control, motor actuation, sensor acquisition, and one-way Bluetooth communication. Measured results included a 5 m detection range, a 0.4 kg prototype mass, and approximately 120° of mechanical motion.

The project also exposed practical PCB-development constraints. Component substitutions required fly-wiring, a voltage-follower redesign for the analog front end, updated LED resistor values, and firmware changes. Those changes reinforced the value of early breadboard validation, careful datasheet review, and designing for testability before fabrication.

![Front of the custom PCB]({{ page.featured_image }})

![Back of the custom PCB](https://raw.githubusercontent.com/Tatwik19/Tatwik19.github.io/master/assets/Projects/Final%20Design%20-%20Not%20Creepy%20Elf/PCB%20photos/BACK%20-%20TATWIK.jpg)

## Team

Adriana Juarez, Sai Srinivas Tatwik Meesala, Noah Blevins, and Ian Mansfield. Developed for EGR 304 at Arizona State University.
