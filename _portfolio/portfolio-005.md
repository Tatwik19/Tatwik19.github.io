---
title: "Semi-Autonomous Twin-Hoist System for Copper-Foil Changeover"
collection: portfolio
date: 2023-04-28
project_period: "Aug 2022 – Apr 2023"
summary: "Designed a twin-hoist concept for Isola's PCB-laminate line that reduced the modeled worst-case roll-changeover time from two minutes to 36 seconds."
role: "X-axis CAD, electrical design, wiring, integration, and project management"
featured_image: "https://raw.githubusercontent.com/Tatwik19/Tatwik19.github.io/master/files/Semi-Autonomous-Twin-Hoist-System.gif"
featured_image_alt: "CAD animation of the semi-autonomous twin-hoist system"
technologies:
  - SolidWorks
  - MATLAB
  - Simulink
  - FEA
  - Industrial automation
repository_url: "https://github.com/Tatwik19/24-Increasing-Changeover-Capabilities-at-Isola"
report_url: "https://github.com/Tatwik19/24-Increasing-Changeover-Capabilities-at-Isola/blob/main/01_Final%20Report.pdf"
slides_url: "https://github.com/Tatwik19/24-Increasing-Changeover-Capabilities-at-Isola/blob/main/00_Final%20Presentation%20Slides.pdf"
---

## Project Overview

Isola's Chandler facility manufactures copper-fiberglass laminate for printed circuit boards. Its copper-foil roll changeover was a largely manual, two-minute process that could stage only two rolls and created a production bottleneck. Our four-person capstone team designed a semi-autonomous twin-hoist system to move 500–700 lb rolls between a staging pallet and the existing machine chucks.

[View repository]({{ page.repository_url }}) · [Final report]({{ page.report_url }}) · [Presentation slides]({{ page.slides_url }})

## Requirements and System Design

The industrial partner required a changeover below 40 seconds, capacity for at least four staged rolls, compatibility with the existing 480 V power and 24 V controls, and materials suitable for an ISO Class 6 clean-room environment.

The selected concept places two independently driven hoists on the existing gantry. Each hoist contains:

- an X-axis carriage for horizontal travel;
- a ball-screw Z-axis for lifting;
- a rack-and-pinion Y-axis/end effector for engaging the roll; and
- optical through-beam sensing to verify roll presence.

Using two carriages allows one hoist to handle the outgoing roll while the other prepares the replacement, reducing idle motion and keeping operators at a safer distance.

## My Contributions

- Developed the X-axis CAD design, motor mounts, support structure, and packaging allowances.
- Produced electrical schematics and wiring-harness documentation.
- Contributed to subsystem integration, design reviews, the bill of materials, and project scheduling.
- Supported CAD iteration, simulation planning, and communication with the industrial partner.

## Results and Validation

The project scope was a detailed, analysis-backed design rather than a fabricated full-scale machine. MATLAB/Simulink models predicted a 36-second worst-case changeover—meeting the 40-second requirement and representing a 70% reduction from the existing two-minute process. SolidWorks FEA verified the design against the 700 lb operating load, and the selected components supported the clean-room requirement.

The final package included mechanical and electrical designs, CAD drawings, a control-flow concept, BOM, cost information, FEA, and dynamic simulations.

![Twin-hoist CAD animation]({{ page.featured_image }})

## Team

Sai Srinivas Tatwik Meesala, Samir Strasser, Reagan Gillespie, and Litzi Matancillas. Developed with Isola for EGR 401/402 at Arizona State University.
