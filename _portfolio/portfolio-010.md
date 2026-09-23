---
title: "ArcFold: Foldable Inchworm Robot"
collection: portfolio
date: 2025-12-20
project_period: "Oct 2025 – Dec 2025"
summary: "Designed, simulated, fabricated, and tested a laminate inchworm robot whose gait combines a foldable linkage, alternating friction anchors, and ESP32-controlled actuation."
role: "Mechanism design, MuJoCo simulation, fabrication, control, and experimental validation"
featured_image: "https://inchworm-foldable-robotics.github.io/assets/01_Home/Inch_Worm.jpg"
featured_image_alt: "ArcFold foldable inchworm robot prototype"
technologies:
  - MuJoCo
  - SolidWorks
  - ESP32
  - Foldable robotics
  - Laser cutting
  - Experimental tracking
project_url: "https://inchworm-foldable-robotics.github.io/"
repository_url: "https://github.com/Inchworm-Foldable-Robotics/Inchworm-Foldable-Robotics.github.io"
---

## Project Overview

ArcFold is a compact crawling robot inspired by the alternating anchor-and-arch gait of an inchworm. The robot uses a rigid foldable body, a central compression mechanism, and front and rear friction-modulated feet to turn periodic shape change into forward motion.

[View project website]({{ page.project_url }}) · [View repository]({{ page.repository_url }})

<video width="700" controls>
  <source src="https://raw.githubusercontent.com/Inchworm-Foldable-Robotics/Inchworm-Foldable-Robotics.github.io/master/assets/04_Results/P4_Inchworm_Good.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Design and Fabrication

The design progressed through four major iterations. Early box-like and hardware-heavy concepts clarified the required geometry but introduced excessive mass and mechanical complexity. The final prototype returned to a lightweight triangular structure made from a five-layer laminate: cardstock outer layers, adhesive layers, and a flexible hinge-film core.

The flat pattern was created in CAD and produced with staged laser-cutting operations for hinge lines and through-cuts. Registration features aligned the layers during heat-press lamination. Three SG92R micro servos—one at the central joint and one at each foot—were controlled by an ESP32 to execute the anchor, compress, release, and extend sequence.

## Modeling and Control

A MuJoCo model represented linkage geometry, compliant flexures, actuator dynamics, mass, damping, and measured friction. Gait periods of 4, 2, 1, and 0.5 seconds were swept to study how actuation frequency affected forward progress and stability.

Physical testing showed that foot engagement had to complete before body compression. Approximately twelve timing variants were explored before settling on the most reliable sequence:

```text
foot engage → body compress → opposite foot release → body extend
```

## My Contributions

- Contributed to mechanism development and CAD iteration from concept through the laminate prototype.
- Built and tuned the MuJoCo model for gait-period studies.
- Supported laser-cut fabrication, ESP32/servo integration, and gait sequencing.
- Analyzed tracked hardware motion against the simulated trajectories.

## Results

The 4-second gait traveled about 0.26 m in 28 seconds, while the 1-second and 0.5-second trials traveled approximately 0.33–0.36 m in 11–12 seconds—near 30 mm/s and roughly three times the speed of the 4-second trial. The 2-second trial underperformed because of foot slip.

Simulation and hardware agreed on the overall relationship between gait timing and forward progress, but the idealized model generally overpredicted stride consistency. At 0.5 seconds, the simulation developed lateral drift while the physical prototype continued forward with greater slip and variability. These differences identified clear next steps: better actuator dynamics, improved hinge reinforcement, engineered friction pads, stronger mounting, and closed-loop sensing.

![MuJoCo simulation of ArcFold](https://inchworm-foldable-robotics.github.io/assets/04_Results/inchworm_crawlP4.gif)

## Team

Sai Srinivas Tatwik Meesala, Colin Fricke, and Nathan Vairora. Developed for RAS 557 at Arizona State University under Prof. Daniel M. Aukes.
