---
title: "Final Project: Agentic Physical AI Manipulation"
lab_number: 3
card_label: "Final Project"
lab_series: assessments
course: "RAS 545: Robotics Systems I"
status: complete
summary: "Develop a robotic manipulation system that interprets natural-language or spoken instructions through an LLM/VLM-based agent and executes context-aware physical tasks."
description: "A capstone Physical AI project integrating multimodal prompting, visual grounding, depth estimation, kinematic reasoning, task planning, and robot manipulation."
topics:
  - Physical AI
  - LLM and VLM agents
  - Visual grounding
  - Depth estimation
  - Robot manipulation
layout: lab
permalink: /labs/final-project-physical-ai/
date: 2025-12-13
author_profile: false
classes: wide
hide_page_metadata: true
---

**Instructor:** Prof. [Sangram Redkar](mailto:Sangram.Redkar@asu.edu)

> **Source material:** [Original final-project brief]({{ '/labs/final-project-physical-ai/final-project-assignment.pdf' | relative_url }})

## Project Overview

The final project develops a Physical AI system in which a robot interprets typed or spoken instructions and converts them into context-aware manipulation actions. An LLM/VLM-based agent connects language understanding with perception, spatial reasoning, kinematics, planning, and physical execution.

The project moves beyond text generation: the agent must ground language in the observed scene, identify relevant objects and spatial relationships, determine a feasible manipulation sequence, and execute the task safely.

## Reference Architecture

~~~text
Typed or spoken instruction
          ↓
LLM/VLM agent and task interpretation
          ↓
Object detection and visual grounding
          ↓
Relative depth and spatial estimation
          ↓
Kinematic and workspace reasoning
          ↓
Task and motion planning
          ↓
Robot manipulation
          ↓
Execution monitoring and verification
~~~

## Core Requirements

- Accept natural-language instructions through text or speech.
- Identify referenced objects using attributes such as color, size, and type.
- Interpret spatial relationships including left, right, above, inside, and on top.
- Decompose a prompt into an ordered sequence of robot actions.
- Estimate relative object depth from monocular imagery.
- Account for robot pose, object height, workspace limits, and reachability.
- Execute pick, place, stack, rotate, and relative-positioning tasks.
- Monitor execution and report task completion or failure.
- Support a broad range of prompt variations rather than a fixed command list.

## Representative Commands

The original project brief includes tasks such as:

- placing a small blue block in the box on the right;
- placing a large yellow block in the box on the left;
- stacking a small block on a larger block;
- rotating a selected block by 90 degrees about the vertical axis before placement; and
- placing a yellow block to the right of a red block.

These examples require the agent to combine semantic object selection with geometric constraints and multi-step robot behavior.

## Kinematic Awareness

The agent must reason about the physical scene rather than generate symbolic actions alone. The robot may begin at different heights relative to the objects, so the system must estimate relative depth and construct feasible approach, grasp, transfer, and placement poses.

Monocular depth estimation can provide relative scene geometry, while robot calibration and kinematic models translate perceived locations into executable targets. Collision avoidance, workspace boundaries, grasp orientation, and safe approach/retract motions remain part of the final action plan.

## Suggested System Modules

| Module | Responsibility |
|---|---|
| Prompt interface | Capture typed or spoken commands. |
| Language and vision agent | Parse intent, resolve object references, and produce a structured task plan. |
| Scene perception | Detect, classify, and localize objects and containers. |
| Depth estimation | Estimate relative depth and geometric relationships from monocular imagery. |
| World model | Maintain object attributes, poses, relationships, and task state. |
| Kinematic reasoning | Validate reachability and generate feasible end-effector goals. |
| Motion execution | Perform approach, grasp, transfer, rotation, placement, and retreat motions. |
| Verification | Confirm the final scene state and support recovery from unsuccessful actions. |

## Evaluation Strategy

Credible validation should include:

- varied wording for equivalent commands;
- multiple object colors, sizes, and arrangements;
- changes in robot and object relative height;
- successful grounding of relational language;
- reachable and unreachable target cases;
- execution monitoring and recovery behavior; and
- repeatable completion of multi-step manipulation tasks.

## Demonstration Policy

- The complete project setup must be assembled, calibrated, powered, and ready to run **before the TA or grader is called**.
- Each project is limited to a maximum of **two official demonstration attempts**.

## Deliverables and Grading

| Deliverable | Weight |
|---|---:|
| Live demonstration | 50 points |
| Technical report | 25 points |
| Source code | 10 points |
| Demonstration video | 15 points |
| **Total** | **100 points** |

The report should document the system architecture, prompt-to-action pipeline, perception and depth methods, kinematic reasoning, experimental setup, evaluation cases, results, and limitations.

## Completion Criteria

- [ ] Typed or spoken commands are converted into structured robot tasks.
- [ ] Referenced objects are grounded correctly in the visual scene.
- [ ] Relative depth and spatial relationships inform the action plan.
- [ ] The agent evaluates kinematic feasibility before execution.
- [ ] The robot completes pick-and-place, stacking, rotation, and relational placement tasks.
- [ ] Execution outcomes are monitored and verified.
- [ ] The code, report, demonstration, and video present the complete Physical AI pipeline.
