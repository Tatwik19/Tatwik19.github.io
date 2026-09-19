---
title: "SmartFollower & Tracker: Autonomous TurtleBot 4 Object Tracking"

excerpt:
    "2026<br/>
    Developed an autonomous TurtleBot 4 system that detects and follows an ArUco-tagged target, avoids obstacles, and records a 2D reconstruction for warehouse anomaly investigation.<br/>
    <img src='https://mobile-robots-ugv.github.io/milestones/hardware%20demo.gif'>"

collection: portfolio
---

Designed and integrated the perception, tracking, recovery, and safety behaviors for SmartFollower & Tracker (SFT), an autonomous TurtleBot 4 platform for following a designated object of interest in indoor warehouse and laboratory environments.

[Project website](https://mobile-robots-ugv.github.io/) · [Final milestone](https://mobile-robots-ugv.github.io/milestones/milestone_3.html)

<br/>

## Project Overview

SFT uses a TurtleBot 4 with an OAK-D camera and RPLidar to detect and follow a human operator carrying a printed ArUco marker board. The system combines visual pose estimation, state prediction, proportional-derivative following control, LiDAR safety checks, and SLAM to produce a 2D map, robot trajectory, and time-stamped target observations.

The system was designed for indoor warehouse and packaging environments where GPS is unavailable and the robot may encounter narrow aisles, clutter, occlusions, carts, pallets, and human traffic.

![Hardware following demo](https://mobile-robots-ugv.github.io/milestones/hardware%20demo.gif)

*TurtleBot 4 following an ArUco board while using SLAM and prediction during temporary target loss.*

## System Pipeline

```text
OAK-D camera
    -> ArUco detection and solvePnP pose estimation
    -> Kalman Filter or Particle Filter target tracking
    -> measured / predicted / lost state machine
    -> PD following control with deadband
    -> LiDAR safety guard
    -> TurtleBot 4 velocity commands
```

The camera estimates the target's 3D position from the known geometry of the marker board. The tracker then filters the lateral and forward coordinates before the controller converts them into linear and angular velocity commands. `slam_toolbox` and RViz2 provide mapping, visualization, and trajectory context.

## Tracking and Control

### Pose Estimation

OpenCV's `solvePnP` estimates the board pose from the detected ArUco markers. The controller uses the target's lateral position `x` and forward distance `z` to determine steering and speed.

### Prediction Filters

Two selectable tracking backends were implemented and evaluated:

- **Kalman Filter:** models the target state as `[x, z, vx, vz]`, smooths noisy measurements, and predicts the target during short occlusions.
- **Particle Filter:** maintains 300 candidate states and uses motion propagation, likelihood weighting, and systematic resampling for nonlinear target motion.

The state machine allows the robot to continue cautiously for up to three seconds after losing direct visibility. It then stops safely if the target cannot be reacquired.

| State | Condition | Robot behavior |
| --- | --- | --- |
| `measured` | Fresh board detection | Normal following |
| `predicted` | Board lost for less than three seconds | Slow following using the filter prediction |
| `lost` | Board lost for more than three seconds | Full stop |

The controller uses a deadband to prevent constant micro-corrections and a LiDAR-based safety guard to stop the robot when an obstacle enters the protected region.

## Demonstrations

- [Simulation demo](https://youtu.be/bWFFL76V-qk)
- [Hardware following demo](https://youtu.be/A36tL840Uys?si=ghFS8TSIxIrdmjJY)

## Benchmarking Results

The Kalman Filter and Particle Filter were evaluated on the same recorded hardware-following session. Data was logged at 20 Hz from the tracked pose, tracker status, and velocity command topics.

- The Kalman Filter remained stable throughout the trial and maintained a mean measured-state error of approximately **0.04 m**.
- The Particle Filter began to diverge after approximately **12 seconds**, reaching errors of roughly **2.0–2.7 m**.
- The Kalman Filter stayed within the expected forward-distance range and recovered quickly after brief occlusions.
- The Particle Filter's particle dispersion caused its estimate to hit the safety clamp and required additional tuning or reinitialization.

These results supported using the Kalman Filter as the preferred backend for the tested hardware and walking conditions.

![Tracker state timeline](https://mobile-robots-ugv.github.io/milestones/status_timeline.png)

![Tracked pose time series](https://mobile-robots-ugv.github.io/milestones/tracked_pose_timeseries.png)

![Measurement error comparison](https://mobile-robots-ugv.github.io/milestones/measurement_error.png)

## Safety and Limitations

The system uses conservative velocity limits and a front LiDAR safety guard. During prediction mode, the robot moves at a substantially reduced speed. The robot was validated in a laboratory environment with fluorescent lighting; ArUco detection may degrade under direct sunlight or low-light conditions. The RPLidar safety guard can also perform poorly with glass, mirrors, transparent surfaces, and highly reflective or dark materials.

Because the camera stream can include people in the environment, future deployments should process imagery locally or mask background individuals before publishing debug frames over the ROS 2 network.

## My Contributions

- Developed the perception and detection pipeline for the ArUco target.
- Integrated simulation behavior with the hardware recovery workflow.
- Implemented `recovery_follower_node.py` for target-following recovery behavior.
- Implemented `sft_hardware_recovery.launch.py` and `leader_odom_tf_node.py` for hardware integration.
- Contributed commit [`7646c12`](https://github.com/Mobile-Robots-UGV/turtlebot4-smart-follower-tracker-hardware/commit/ca3c1c16c686656dc3cf1c0ee818889cd69674d9).

## Technologies

`ROS 2` · `TurtleBot 4` · `OAK-D` · `RPLidar` · `OpenCV` · `ArUco` · `solvePnP` · `Kalman Filter` · `Particle Filter` · `PD Control` · `SLAM Toolbox` · `RViz2`
