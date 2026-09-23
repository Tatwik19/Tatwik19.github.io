---
title: "SmartFollower & Tracker: Autonomous TurtleBot 4 Object Tracking"
collection: portfolio
date: 2026-05-01
project_period: "2026"
summary: "Developed an autonomous TurtleBot 4 system that follows an ArUco-tagged target, predicts through short occlusions, enforces LiDAR safety, and records a 2D reconstruction."
role: "Perception, tracking, recovery behavior, hardware integration, and validation"
featured_image: "https://mobile-robots-ugv.github.io/milestones/hardware%20demo.gif"
featured_image_alt: "TurtleBot 4 following an ArUco marker target"
technologies:
  - ROS 2
  - TurtleBot 4
  - OAK-D
  - RPLidar
  - OpenCV
  - Kalman filtering
  - SLAM Toolbox
project_url: "https://mobile-robots-ugv.github.io/"
repository_url: "https://github.com/Mobile-Robots-UGV/turtlebot4-smart-follower-tracker-hardware"
---

## Project Overview

SmartFollower & Tracker (SFT) is an autonomous TurtleBot 4 platform for following a designated object of interest in indoor warehouse and laboratory environments. A human operator carries a printed ArUco marker board; the robot estimates its pose, follows at a controlled distance, predicts through short occlusions, and stops safely when confidence or clearance is lost.

[View project website]({{ page.project_url }}) · [Final milestone](https://mobile-robots-ugv.github.io/milestones/milestone_3.html) · [View repository]({{ page.repository_url }})

![Hardware following demonstration]({{ page.featured_image }})

## System Pipeline

```text
OAK-D camera
  → ArUco detection and solvePnP pose estimation
  → Kalman or particle-filter tracking
  → measured / predicted / lost state machine
  → PD following control with deadband
  → LiDAR safety guard
  → TurtleBot 4 velocity commands
```

OpenCV estimates the marker board's 3D pose from its known geometry. The tracker filters lateral and forward position before the controller generates linear and angular velocity commands. SLAM Toolbox and RViz2 provide mapping, trajectory visualization, and spatial context for logged observations.

## Tracking and Recovery

Two tracking backends were implemented and compared:

- a Kalman Filter with state `[x, z, vx, vz]` for smoothing and short-term prediction; and
- a 300-particle filter with motion propagation, likelihood weighting, and systematic resampling.

The state machine operates in three modes:

| State | Condition | Robot behavior |
| --- | --- | --- |
| `measured` | Fresh marker detection | Normal following |
| `predicted` | Detection lost for less than three seconds | Reduced-speed following using prediction |
| `lost` | Detection lost for more than three seconds | Full stop |

A control deadband reduces unnecessary micro-corrections. A forward LiDAR safety region can override the follower and stop the robot when an obstacle enters the protected area.

## My Contributions

- Developed the ArUco perception and pose-estimation pipeline.
- Integrated simulation behavior with the hardware recovery workflow.
- Implemented `recovery_follower_node.py`, `sft_hardware_recovery.launch.py`, and `leader_odom_tf_node.py`.
- Contributed to tracker benchmarking, system integration, and hardware validation.
- Contributed commit [`ca3c1c1`](https://github.com/Mobile-Robots-UGV/turtlebot4-smart-follower-tracker-hardware/commit/ca3c1c16c686656dc3cf1c0ee818889cd69674d9).

## Results

Both filters were evaluated on the same 20 Hz hardware-following dataset. The Kalman Filter remained stable and maintained a mean measured-state error of approximately 0.04 m. The Particle Filter began diverging after about 12 seconds and reached errors of approximately 2.0–2.7 m. These results supported selecting the Kalman Filter for the tested walking and laboratory conditions.

The system also demonstrated short-occlusion recovery, conservative predicted-mode motion, autonomous stopping, and synchronized mapping of robot motion and target observations.

![Tracker state timeline](https://mobile-robots-ugv.github.io/milestones/status_timeline.png)

![Measurement error comparison](https://mobile-robots-ugv.github.io/milestones/measurement_error.png)

## Limitations and Next Steps

ArUco detection remains sensitive to lighting and visibility. LiDAR safety performance can degrade around glass, mirrors, transparent surfaces, and some reflective or dark materials. Future work should add broader environmental testing, stronger privacy handling for incidental camera imagery, and improved particle-filter initialization and tuning.
