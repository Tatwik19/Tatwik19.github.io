---
title: "Midterm 1: Camera-Assisted Tic-Tac-Toe Robot"
lab_number: 1
card_label: "Midterm 1"
lab_series: assessments
course: "RAS 545: Robotics Systems I"
status: complete
summary: "Integrate robot drawing, camera-based board-state perception, game logic, and motion control to create a robotic Tic-Tac-Toe opponent."
description: "A robotics assessment combining visual perception, game-state reasoning, coordinate mapping, and physical drawing with an articulated robot."
topics:
  - Robot programming
  - Computer vision
  - Game-state reasoning
  - Coordinate mapping
  - Human-robot interaction
layout: lab
permalink: /labs/midterm-01-tic-tac-toe/
date: 2025-10-17
author_profile: false
classes: wide
hide_page_metadata: true
---

**Instructor:** Prof. [Sangram Redkar](mailto:Sangram.Redkar@asu.edu)

> **Source materials:** [Assignment overview]({{ '/labs/midterm-01-tic-tac-toe/midterm-1-assignment.pdf' | relative_url }}) · [Original project specification]({{ '/labs/midterm-01-tic-tac-toe/midterm-1-specification.pdf' | relative_url }})

## Assessment Overview

This midterm integrates perception, reasoning, and physical robot motion in a human-robot Tic-Tac-Toe game. The robot creates the board, observes the evolving game state, selects a valid move, and draws its mark in the corresponding cell.

The assessment emphasizes complete system behavior rather than an isolated algorithm: camera observations must be interpreted in board coordinates, game logic must maintain a consistent state, and the resulting decision must be converted into safe robot motion.

## Functional Workflow

~~~text
Draw the 3 × 3 board
        ↓
Observe the human move
        ↓
Detect and classify occupied cells
        ↓
Update the game state
        ↓
Select a legal robot move
        ↓
Map the selected cell to robot coordinates
        ↓
Draw the robot mark
        ↓
Detect win, draw, or next turn
~~~

## Core Requirements

- Generate a repeatable 3 × 3 game grid with the robot.
- Support a human player using either X or O.
- Detect the human move and associate it with the correct board cell.
- Maintain the board state across alternating turns.
- Select legal robot moves using a rule-based, MATLAB-based, or AI-assisted decision method.
- Draw the robot mark inside the selected cell.
- Identify wins and full-board draws.
- Prevent overwriting an occupied cell.

## Technical Components

| Component | Purpose |
|---|---|
| Board calibration | Relate image-space cells to physical robot coordinates. |
| Visual perception | Detect the grid and classify human and robot marks. |
| Game-state model | Track occupancy, active player, legal moves, wins, and draws. |
| Decision engine | Select the next robot move from the current state. |
| Motion generation | Convert a board-cell decision into a repeatable drawing trajectory. |
| Safety logic | Maintain a safe approach height and controlled contact with the drawing surface. |

## Extended Scenarios

The original specification also identifies advanced cases for a more complete implementation:

- configurable first player, including a robot opening move;
- recovery from ambiguous, duplicate, or incorrectly recognized marks;
- explicit draw and inconclusive-state handling; and
- two robots playing against one another.

Extended functionality should be documented in the report and demonstration video.

## Deliverables and Grading

| Deliverable | Weight |
|---|---:|
| Individual report | 10 points |
| Live demonstration | 10 points |
| Video presentation | 20 points |
| **Total** | **40 points** |

The original brief specifies a three-page individual report, a live demonstration, and a video presentation. The demonstration allows two attempts and is evaluated as a complete system behavior.

## Presentation Resources

- [Sample video presentation](https://youtu.be/HTXOMVjY4V4)
- [ASU School of Manufacturing Systems and Networks](https://www.linkedin.com/showcase/school-of-manufacturing-systems-and-networks/)

## Completion Criteria

- [ ] The robot draws a consistent game grid.
- [ ] Camera observations are mapped to the correct board cells.
- [ ] Human and robot marks are represented correctly in the internal game state.
- [ ] The robot selects only legal moves.
- [ ] Drawing trajectories remain within the selected cells.
- [ ] Win and draw conditions terminate the game correctly.
- [ ] The report and video explain the perception, decision, calibration, and motion pipeline.
