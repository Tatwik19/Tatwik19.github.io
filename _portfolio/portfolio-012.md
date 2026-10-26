---
title: "Stellantis Industrial Physical AI Robot Demonstrator"
collection: portfolio
date: 2026-10-21
project_period: "Sep 2026 - Oct 2026"
summary: "Integrated and deployed an industrial collaborative-robot workcell that connected UR5e motion execution through Wandelbots NOVA with an NVIDIA Isaac Sim digital twin."
role: "Workcell integration, industrial networking, NOVA application deployment, Isaac Sim digital-twin integration, commissioning, and on-site validation"
technologies:
  - Universal Robots UR5e
  - Wandelbots NOVA
  - Kontron KBox industrial PC
  - NVIDIA Isaac Sim
  - OpenUSD
  - Kubernetes and containerd
  - REST and WebSocket APIs
  - NATS
  - Industrial Ethernet
---

## Project Overview

The Stellantis Industrial Physical AI Robot Demonstrator was developed at Arizona State University in collaboration with Wandelbots GmbH for **Stellantis Factory Booster Day 2026** in Michigan. The project integrated a physical Universal Robots UR5e collaborative robot, a Kontron KBox industrial PC running NOVA OS, containerized automation applications, and an NVIDIA Isaac Sim digital twin.

The physical demonstration used one UR5e as the helper robot for predefined pickup and transfer motions. The Isaac Sim environment represented the complete dual-robot workcell, including the helper station and the virtual screwdriving operation. This arrangement connected physical robot execution with a broader virtual manufacturing scenario without representing the virtual screwdriving sequence as a completed physical operation.

## My Contributions

- Integrated the UR5e controller with the NOVA industrial PC through a dedicated Ethernet network.
- Configured persistent static addressing and automatic network activation for repeatable startup after transportation.
- Installed, updated, and validated containerized NOVA applications on the IPC.
- Imported application images into the IPC container runtime and deployed their manifests through the NOVA command-line interface.
- Configured robot-controller identities, motion groups, application services, and state-monitoring interfaces.
- Integrated the Isaac Sim workcell with the NOVA motion group through the NOVA Isaac Sim extension.
- Supported camera-device integration and application-level verification.
- Performed system commissioning, troubleshooting, relocation testing, and on-site demonstration support.
- Verified robot communication, motion execution, controller-state streaming, TCP-pose reporting, and virtual articulation updates.

## System Architecture

| Layer | Implementation | Function |
|---|---|---|
| Physical execution | Universal Robots UR5e controller | Executes robot trajectories and retains responsibility for physical motion and safety functions. |
| Industrial edge | Kontron KBox running NOVA OS | Hosts robot configuration, planning, communication, application, and monitoring services. |
| Application runtime | Kubernetes, k3s, and containerd | Runs and manages the containerized demonstration applications on the IPC. |
| Service interface | HTTP/REST API | Provides robot models, controller configurations, motion-group descriptions, and planning resources. |
| Execution and telemetry | WebSocket interfaces | Transmits trajectories and streams joint states, TCP poses, controller modes, and execution status. |
| Event middleware | NATS | Distributes controller states, I/O updates, execution events, and service notifications. |
| Digital twin | NVIDIA Isaac Sim and OpenUSD | Represents the workcell and maps physical joint states to the corresponding virtual robot articulation. |
| Network | Dedicated static Ethernet | Maintains deterministic communication between the robot controller and industrial PC. |

## Communication and Digital-Twin Workflow

The UR5e controller connected directly to the industrial PC through a dedicated Ethernet interface with persistent static addressing. NOVA represented the robot through its cell, controller, and motion-group hierarchy, allowing the application layer to reference a stable robot identity independently of the physical deployment location.

The integrated workflow followed this sequence:

```text
Application command
  -> NOVA planning service
  -> Time-parameterized joint trajectory
  -> WebSocket execution channel
  -> UR5e controller
  -> Physical robot motion
```

During execution, separate communication paths streamed robot and system information:

```text
UR5e joint states and TCP pose
  -> NOVA state services
  -> WebSocket and NATS distribution
  -> Monitoring applications
  -> Isaac Sim virtual articulation
```

The NOVA Isaac Sim extension associated the OpenUSD robot articulation with the physical NOVA motion group. Streamed joint states updated the simulated robot configuration and provided a live physical-to-virtual visualization of the workcell state.

## Application Deployment

The demonstration applications were delivered as container images and NOVA application manifests. The images were transferred to the industrial PC, imported into the local container runtime, and deployed as workloads in the NOVA cell namespace.

This deployment process supported controlled application updates without rebuilding the industrial PC. Image tags identified each software revision, while the application manifests defined the corresponding service configuration. Camera and hardware-device access were applied through deployment configuration patches and verified through application status endpoints.

## Demonstration Workflow

The physical demonstration focused on the helper robot and used predefined joint-space and Cartesian trajectories. The operator initialized the workcell through NOVA, selected the configured motion group, and executed the demonstration sequence. NOVA distributed controller states and execution status to the application services while Isaac Sim visualized the corresponding robot configuration.

The digital environment showed the broader dual-robot manufacturing concept. One virtual robot represented the helper and material-handling role, while the second represented the screwdriving operation. This separated the verified physical behavior from the extended virtual process concept.

## Deployment and Validation

The workcell was assembled and commissioned at ASU before being transported to Michigan. After relocation, the system resumed operation using the persistent controller identity and saved network configuration.

The deployed system demonstrated:

- reliable communication between the UR5e controller and industrial PC;
- NOVA-based point-to-point and Cartesian motion execution;
- controller-state, joint-state, and TCP-pose streaming;
- containerized application deployment and revision updates;
- camera-device detection and application access;
- physical-to-virtual joint-state mapping in Isaac Sim; and
- successful recommissioning after transportation.

The on-site demonstration established functional integration across the physical robot, industrial edge computer, application services, communication middleware, and digital-twin workstation.

## Engineering Outcomes

The project demonstrated that a portable industrial robot workcell requires coordinated configuration across several technical layers. Stable controller identities, persistent network profiles, versioned application images, and repeatable startup procedures were essential for reliable relocation and recommissioning.

The work also clarified the division of responsibility across the architecture. The UR5e controller retained physical execution and safety functions. NOVA supplied planning, application integration, execution management, and state distribution. Isaac Sim provided the virtual workcell representation and live robot-state visualization.

## Research Output

A two-page technical paper based on this work was submitted to the **2026 Southwest Robotics Symposium**:

**“Physical-Virtual Integration of an Industrial Collaborative Robot Manipulator for Digital-Twin-Assisted Assembly.”**

The paper documents the edge architecture, communication interfaces, motion-group abstraction, physical robot execution, and Isaac Sim digital-twin integration.

## Event

**Stellantis Factory Booster Day 2026**

The completed system was transported from Arizona State University to Michigan for an industrial technology demonstration. The event presented the workcell to manufacturing and automation professionals in a production-oriented setting.

## Acknowledgment

This project was conducted at Arizona State University in collaboration with Wandelbots GmbH.
