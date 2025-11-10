---
title: "AeroFusion: Autonomous BLIMP Navigation and Sensor Integration Platform"

excerpt: 
    "Jan 2025 – Apr 2025<br/>
    The project aims to develop an integrated, sensor-driven framework that enables a Biologically-inspired, Lighter-than-air, Instructional, Mechatronics Program (BLIMP) UAV to operate autonomously in dynamic and uncertain environments."
# excerpt: "Short description of portfolio item number 1<br/><img src='/images/500x300.png'>"

collection: portfolio
---

<br/>

Check the website [here](https://ras598-2025-s-team03.github.io/)

<br/>

# AeroFusion

## Summary
AeroFusion develops a sensor-driven framework that enables a biologically inspired BLIMP UAV to detect, track, and approach targets autonomously in dynamic indoor environments. The system fuses IMU, barometer, and camera data within a modular ROS 2 stack and provides real-time telemetry through a browser-based GUI.

<br/>

## Highlights
- **Perception:** Custom YOLOv5 model with quadrant logic for target tracking.
- **Control:** PI and differential drive controls; force allocation via pseudo-inverse.
- **Sensor Fusion:** IMU + barometer filtering for stabilized altitude and attitude.
- **ROS 2 Stack:** C++ and Python nodes with explicit topic interfaces and launch files.
- **GUI:** WebSocket (rosbridge + roslibjs) interface with live video and telemetry.
- **Validation:** Thrust-stand characterization and Vicon-based motion tracking.

<br/>

## Media
![BLIMP CAD](https://ras598-2025-s-team03.github.io/figures/blimp_model.JPG)
*CAD rendering of the BLIMP platform.*

![ROS GUI](https://ras598-2025-s-team03.github.io/figures/blimp_gui.png)
*Browser-based ROS telemetry and controls.*

<br/>

## Architecture

```bash
/image_raw → YOLOv5_Detector → /blimp/detected_position
/imu_data + /barometer_data + /balloon_input → InvKine → /forces
/forces → F_to_ESC → /ESC_balloon_input
/ESC_Manual_input + /ESC_balloon_input → ModeSwitch → /ESC_input → ESC_Driver
```

<br/>


Key nodes:
- **detect_cpp** (C++): camera detection and goal/balloon modes.
- **inv_kine** (C++): force estimation from IMU/barometer/vision.
- **f_to_esc** (C++/Eigen): body forces → ESC PWM via pseudo-inverse.
- **esc_driver** (Python/pigpio): PWM output and ESC arming.
- **joy_to_esc** (Python): manual teleop mapping.
- **mode_switch** (Python): manual vs autonomous arbitration.
- **read_imu**, **read_altitude** (Python): sensor interfaces.

---

## Modeling and Identification
- **6-DOF dynamics:** rigid + added mass, Coriolis/centripetal, linear damping, restoring forces.
- **Allocation:** non-square thruster map solved with Moore–Penrose pseudo-inverse.
- **System ID:** SolidWorks inertia, Lamb k-factors for added mass, thrust-stand linear PWM→thrust fits, and damping via flight tests with Vicon.

Representative figures:
- Thrust vs PWM: <a href="https://ras598-2025-s-team03.github.io/figures/Figure4_5.jpg" target="_blank" rel="noopener">Figure 4/5</a>  
- Block diagram: <a href="https://ras598-2025-s-team03.github.io/figures/blimp_block_diagram.png" target="_blank" rel="noopener">System diagram</a>

---

## Implementation Details
**Platform:** Raspberry Pi, ROS 2 Humble, rclpy/rclcpp, Eigen, pigpio, OpenCV, roslibjs, rosbridge_server, web_video_server.

**Selected topics:**
- Perception: `/image_raw`, `/blimp/detected_position`
- Sensing: `/imu_data`, `/barometer_data`
- Control: `/forces`, `/ESC_balloon_input`, `/ESC_Manual_input`, `/ESC_input`

---

## How to Run (excerpt)
```bash
# Workspace
mkdir -p ~/blimp_ws/src
cd ~/blimp_ws/src && git clone https://github.com/RAS598-2025-S-Team03/BLIMP-Packages.git

# Build interfaces first, then all
cd ~/blimp_ws && colcon build --packages-select blimp_interfaces
source install/setup.bash
colcon build

# Optional: Oak-D Lite camera stack in separate workspace
# (see project docs for install script and rosdep)

# Verify joystick
ros2 run joy game_controller_node

# Arm ESCs
ros2 launch auto_control arming.py

# Launch full stack
ros2 launch auto_control updated_launch.py

# GUI bridge + camera stream
ros2 launch blimp_gui rosbridge_camera_launch.py
```
