---
title: "Watching Distance: Wearable Depth-Perception Aid"
collection: portfolio
date: 2022-04-30
project_period: "Jan 2022 - Apr 2022"
summary: "Developed a wearable embedded prototype that measures object distance and presents it on a compact display for users with impaired depth perception after stroke."
role: "Embedded-system integration, PCB development, and prototyping"
featured_image: "https://user-images.githubusercontent.com/96451759/166118037-aef595fe-bed9-4bc8-a2e5-96a3eada7e6c.jpg"
featured_image_alt: "Watching Distance wearable embedded-system prototype"
technologies:
  - Embedded systems
  - Microchip PIC
  - Analog and digital sensing
  - I2C and UART
  - Cadence Allegro
  - Surface-mount assembly
repository_url: "https://github.com/Tatwik19/Team205-Watching-Distance"
schematic_url: "https://github.com/Tatwik19/Team205-Watching-Distance/files/8578224/FINALSCHEMATICBRD.pdf"
poster_url: "https://github.com/Tatwik19/Team205-Watching-Distance/files/8597608/Poster.pdf"
---

## Project Overview

Watching Distance is a wearable depth-perception aid for people who experience impaired depth perception after a stroke. The device measures object distance and displays the result in meters. An MPU-6050 gyroscope detects the raise-and-point interaction.

[Repository]({{ page.repository_url }}) · [PCB schematic]({{ page.schematic_url }}) · [Project poster]({{ page.poster_url }})

## Hardware at a Glance

| Component | Model | Interface / role |
|---|---|---|
| Microcontroller | Microchip **PIC18F27Q43-I/SO** | MCC, ADC, I2C, UART, GPIO |
| Distance sensor | **QSE114**, **GP2S700HCP**, **QED223** | Analog sensing -> ADC |
| Inertial sensor | **MPU-6050** | I2C gyroscope |
| Display | **OD-358R** | Digital serial display |
| Display drivers | **MM5452V**, **AS1115-BSST** | Display control |
| Shift register | **SN74LS674DW** | Serial output expansion |
| Signal conditioning | **LM358** | Analog amplification |
| Wireless module | Wi-Fi module | UART / serial |
| Voltage regulator | **AP7361-33E-13** | 3.3 V display rail |
| PCB | Cadence Allegro | Surface-mount layout and routing |

**Protocols:** I2C · UART · ADC · serial shift-register · GPIO

## My Contributions

- Integrated the PIC, analog distance sensor, MPU-6050, display, Wi-Fi module, and digital I/O.
- Contributed to the schematic and Cadence Allegro PCB design.
- Developed the raise-and-measure interaction using gyroscope data.
- Supported firmware debugging, hardware revisions, testing, and documentation.

## Results

The team built and tested a compact wearable embedded system that converted live distance data into immediate local feedback. The design demonstrated analog sensing, I2C motion sensing, wireless communication, regulated power distribution, and a functioning custom PCB.

## Project Artifacts

- [GitHub repository]({{ page.repository_url }})
- [PCB schematic]({{ page.schematic_url }})
- [Project poster]({{ page.poster_url }})

![Watching Distance prototype]({{ page.featured_image }})
