---
title: "Stellantis Industrial Physical AI Robot Demonstrator"
collection: portfolio
date: 2026-10-21
project_period: "Sep 2026 - Oct 2026"
summary: "Integrated and deployed an industrial collaborative-robot workcell that connected UR5e motion execution through Wandelbots NOVA with an NVIDIA Isaac Sim digital twin."
role: "Workcell integration, industrial networking, NOVA application deployment, Isaac Sim digital-twin integration, commissioning, and on-site validation"
featured_image: "/assets/Projects/Industrial_Physical_AI_Robot_Demonstrator/01_Digital_twin_and_physical_workcell.png"
featured_image_alt: "NVIDIA Isaac Sim digital twin and physical collaborative-robot workcell"
technologies:
  - Universal Robots UR5e
  - Wandelbots NOVA
  - Industrial PC
  - NVIDIA Isaac Sim
  - OpenUSD
  - Kubernetes and containerd
  - REST and WebSocket APIs
  - NATS
  - Industrial Ethernet
---

## Project Overview

Developed at Arizona State University in collaboration with [Wandelbots](https://www.wandelbots.com/), this demonstrator connected a physical Universal Robots UR5e collaborative robot to an NVIDIA Isaac Sim digital twin through [Wandelbots NOVA](https://www.wandelbots.com/wandelbots-nova-the-physical-ai-platform). The completed workcell was presented at [Stellantis Factory Booster Day 2026](https://www.media.stellantis.com/uk-en/corporate/press/factory-booster-day-2026-accelerates-innovation-across-stellantis-global-manufacturing-network) in Michigan.

The physical robot executed validated pickup and transfer motions while NOVA coordinated planning, execution, telemetry, and application services. Isaac Sim represented the broader dual-robot manufacturing concept and mirrored the physical robot's joint state in the virtual workcell.

### Project Highlights

- Integrated industrial robot control, edge computing, containerized applications, and digital-twin visualization.
- Established repeatable networking and deployment procedures for transportation and recommissioning.
- Validated physical motion execution, live state streaming, and physical-to-virtual articulation updates.

## Media

<figure class="portfolio-project__media portfolio-project__media--wide">
  <img src="/assets/Projects/Industrial_Physical_AI_Robot_Demonstrator/01_Digital_twin_and_physical_workcell.png" alt="Isaac Sim digital twin beside the physical collaborative-robot workcell">
</figure>

<figure class="portfolio-project__media portfolio-project__media--portrait">
  <video width="240" controls playsinline preload="metadata" style="display: block; width: 240px; max-width: 100%; height: auto; margin: 0 auto;">
    <source src="/assets/Projects/Industrial_Physical_AI_Robot_Demonstrator/Demo.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</figure>

## My Contributions

- Integrated the UR5e controller and industrial PC through a dedicated Ethernet network with persistent addressing and automatic startup.
- Installed, updated, and validated containerized NOVA applications and deployment manifests.
- Configured controller identities, motion groups, application services, and state-monitoring interfaces.
- Connected the Isaac Sim workcell to the physical NOVA motion group for live articulation updates.
- Supported camera integration, system commissioning, troubleshooting, relocation testing, and on-site operation.
- Verified motion execution, controller and joint-state streaming, TCP-pose reporting, and digital-twin synchronization.

## System Architecture

| Layer | Implementation | Function |
|---|---|---|
| Physical execution | Universal Robots UR5e controller | Executes robot trajectories and retains responsibility for physical motion and safety functions. |
| Industrial edge | IPC running NOVA OS | Hosts robot configuration, planning, communication, application, and monitoring services. |
| Application runtime | Kubernetes, k3s, and containerd | Runs and manages the containerized demonstration applications on the IPC. |
| Service interface | HTTP/REST API | Provides robot models, controller configurations, motion-group descriptions, and planning resources. |
| Execution and telemetry | WebSocket interfaces | Transmits trajectories and streams joint states, TCP poses, controller modes, and execution status. |
| Event middleware | NATS | Distributes controller states, I/O updates, execution events, and service notifications. |
| Digital twin | NVIDIA Isaac Sim and OpenUSD | Represents the workcell and maps physical joint states to the corresponding virtual robot articulation. |
| Network | Dedicated static Ethernet | Maintains deterministic communication between the robot controller and industrial PC. |

## Integration Workflow

The UR5e controller connected directly to the industrial PC through dedicated Ethernet with persistent static addressing. NOVA represented the robot through a cell, controller, and motion-group hierarchy, giving the application layer a stable robot identity across deployment locations.

### Command and Execution

```text
Application command
  -> NOVA planning service
  -> Time-parameterized joint trajectory
  -> WebSocket execution channel
  -> UR5e controller
  -> Physical robot motion
```

### State and Digital-Twin Synchronization

```text
UR5e joint states and TCP pose
  -> NOVA state services
  -> WebSocket and NATS distribution
  -> Monitoring applications
  -> Isaac Sim virtual articulation
```

The NOVA Isaac Sim extension associated the OpenUSD articulation with the physical motion group. Streamed joint states updated the simulated robot configuration, creating a live physical-to-virtual view of the workcell.

## Application Deployment

Demonstration applications were delivered as versioned container images and NOVA manifests. They were imported into the local runtime and deployed in the NOVA cell namespace, enabling controlled updates without rebuilding the industrial PC. Deployment patches provided camera and hardware access, and application status endpoints supported verification.

## Demonstration Workflow

The operator initialized the workcell through NOVA, selected the configured motion group, and executed predefined joint-space and Cartesian trajectories. NOVA distributed controller and execution states while Isaac Sim visualized the corresponding configuration. A second virtual robot represented the extended screwdriving concept, clearly separating verified physical behavior from the broader simulated process.

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

The resulting architecture maintained a clear division of responsibility: the UR5e controller retained physical execution and safety functions; NOVA supplied planning, application integration, execution management, and state distribution; and Isaac Sim provided virtual workcell representation and live state visualization.

## Research Output

A two-page technical paper, *Physical-Virtual Integration of an Industrial Collaborative Robot Manipulator for Digital-Twin-Assisted Assembly*, was submitted to the **2026 Southwest Robotics Symposium**. The paper documents the edge architecture, communication interfaces, motion-group abstraction, physical execution, and Isaac Sim integration.

## Collaboration and Showcase

This project was conducted at Arizona State University in collaboration with [Wandelbots](https://www.wandelbots.com/) and presented to manufacturing and automation professionals at [Stellantis Factory Booster Day 2026](https://www.media.stellantis.com/uk-en/corporate/press/factory-booster-day-2026-accelerates-innovation-across-stellantis-global-manufacturing-network) in Michigan.
