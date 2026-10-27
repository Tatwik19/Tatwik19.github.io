---
title: "Stellantis Industrial Physical AI Robot Demonstrator"
collection: portfolio
date: 2026-10-21
project_period: "Sep 2026 - Oct 2026"
summary: "Architected and validated an industrial Physical AI workcell that unified collaborative-robot execution, software-defined orchestration, and an NVIDIA Isaac Sim digital twin."
role: "System architecture, physical-virtual integration, edge application deployment, commissioning, and experimental validation"
featured_image: "/assets/Projects/Industrial_Physical_AI_Robot_Demonstrator/01_Digital_twin_and_physical_workcell.png"
featured_image_alt: "NVIDIA Isaac Sim digital twin and physical collaborative-robot workcell"
technologies:
  - Universal Robots UR5e
  - Wandelbots NOVA
  - NVIDIA Isaac Sim
  - OpenUSD
  - Kubernetes and containerd
  - REST and WebSocket APIs
  - NATS
  - Digital twins
---

## Project Overview

Developed at Arizona State University in collaboration with [Wandelbots](https://www.wandelbots.com/), this industrial Physical AI demonstrator unified collaborative-robot execution, software-defined orchestration, and a high-fidelity digital twin within one operational architecture. The completed workcell was presented at [Stellantis Factory Booster Day 2026](https://www.media.stellantis.com/uk-en/corporate/press/factory-booster-day-2026-accelerates-innovation-across-stellantis-global-manufacturing-network) in Michigan.

The Universal Robots UR5e executed manipulation tasks through [Wandelbots NOVA](https://www.wandelbots.com/wandelbots-nova-the-physical-ai-platform), while live robot state synchronized the corresponding NVIDIA Isaac Sim articulation. The virtual environment extended the physical demonstrator into a dual-robot assembly scenario, providing a foundation for virtual commissioning, process validation, and scalable automation development.

### Project Highlights

- Unified robot control, edge orchestration, application services, and digital-twin synchronization.
- Established a reusable physical-virtual architecture based on robot and motion-group abstractions.
- Validated the complete workcell through laboratory commissioning, relocation, and an industrial showcase.

## Media

<figure class="portfolio-project__media portfolio-project__media--wide">
  <img src="/assets/Projects/Industrial_Physical_AI_Robot_Demonstrator/01_Digital_twin_and_physical_workcell.png" alt="Isaac Sim digital twin beside the physical collaborative-robot workcell">
</figure>

<div class="portfolio-project__video-row">
  <figure class="portfolio-project__media portfolio-project__media--portrait">
    <video width="240" controls playsinline preload="metadata" style="display: block; width: 240px; max-width: 100%; height: auto; margin: 0 auto;">
      <source src="/assets/Projects/Industrial_Physical_AI_Robot_Demonstrator/Build.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </figure>

  <figure class="portfolio-project__media portfolio-project__media--portrait">
    <video width="240" controls playsinline preload="metadata" style="display: block; width: 240px; max-width: 100%; height: auto; margin: 0 auto;">
      <source src="/assets/Projects/Industrial_Physical_AI_Robot_Demonstrator/Demo.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </figure>
</div>

## My Contributions

- Architected the end-to-end integration of the physical robot, NOVA platform, edge applications, and Isaac Sim environment.
- Configured the robot and motion-group abstractions used for planning, execution, monitoring, and simulation.
- Engineered the containerized application workflow for repeatable deployment on the industrial edge platform.
- Integrated live robot-state telemetry with the OpenUSD articulation to synchronize physical and virtual motion.
- Led system commissioning, cross-layer troubleshooting, relocation testing, and on-site validation.
- Evaluated motion execution, telemetry continuity, application behavior, and digital-twin fidelity as a complete system.

## System Architecture

| Layer | Implementation | Function |
|---|---|---|
| Physical system | Universal Robots UR5e | Executes collaborative manipulation tasks and enforces controller-level motion and safety functions. |
| Physical AI platform | Wandelbots NOVA OS | Provides robot abstraction, motion planning, execution management, and application integration. |
| Edge runtime | Kubernetes and containerd | Hosts versioned, containerized services for portable and repeatable deployment. |
| Application interface | REST and WebSocket APIs | Exposes robot models, motion groups, planning resources, trajectory execution, and telemetry. |
| Event layer | NATS | Distributes robot state, execution events, I/O updates, and service notifications. |
| Digital twin | NVIDIA Isaac Sim and OpenUSD | Represents the manufacturing workcell and synchronizes virtual articulations with physical robot state. |

## Physical-Virtual Workflow

NOVA decoupled task-level application logic from the robot controller through a common cell and motion-group abstraction. This architecture connected planning and physical execution with continuous state synchronization in Isaac Sim.

```text
Task application -> NOVA planning and execution -> UR5e motion
UR5e state -> NOVA telemetry and events -> Isaac Sim digital twin
```

The OpenUSD articulation and physical robot shared the same motion-group identity. This enabled the virtual workcell to reflect executed robot motion while supporting a broader dual-robot assembly scenario for process development and visualization.

## Software-Defined Deployment

Versioned application containers and NOVA manifests packaged the workcell software as a reproducible deployment. The edge-native architecture separated application services from the robot hardware, supporting controlled updates, consistent commissioning, and reuse across physical and virtual environments.

## System Validation

The workcell was commissioned at ASU, transported to Michigan, and recommissioned for the industrial showcase. End-to-end validation confirmed:

- coordinated point-to-point and Cartesian motion execution;
- continuous controller, joint-state, and tool-pose telemetry;
- synchronized physical and virtual robot articulation;
- reliable operation of containerized application services; and
- repeatable system behavior after relocation.

## Industry Relevance

The demonstrator addresses a central manufacturing challenge: transferring automation from simulation to the shop floor while preserving reusable application logic across hardware configurations. Its architecture illustrates several capabilities central to scalable industrial Physical AI:

- **Virtual commissioning:** Robot behavior and manufacturing scenarios can be developed and evaluated in a high-fidelity digital environment before physical deployment.
- **Hardware abstraction:** A common motion-group interface separates application logic from controller-specific implementation.
- **Software-defined automation:** Versioned edge applications support repeatable deployment, controlled updates, and reuse across workcells.
- **Operational visibility:** Live telemetry and digital-twin synchronization provide a shared representation for monitoring, validation, and process analysis.
- **Deployment portability:** The integrated workcell retained its system behavior through transportation and recommissioning in an industrial event environment.

## Research Output

A technical paper titled *Physical-Virtual Integration of an Industrial Collaborative Robot Manipulator for Digital-Twin-Assisted Assembly* was submitted to the **2026 Southwest Robotics Symposium**. The paper presents the system architecture, communication framework, motion-group abstraction, physical execution pipeline, and digital-twin integration.
