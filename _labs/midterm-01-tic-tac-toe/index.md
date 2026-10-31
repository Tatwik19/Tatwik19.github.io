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

This midterm integrates perception, reasoning, and physical robot motion in a human-robot Tic-Tac-Toe game. The robot creates the board, observes the evolving game state, selects a valid move, and draws its mark in the corresponding cell. The human plays first and may choose either X or O; the robot uses the remaining mark.

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
Detect a human win, robot win, draw, or next turn
~~~

## Core Requirements

- Generate a repeatable 3 × 3 game grid with the robot.
- Allow the human player to move first and choose either X or O; assign the opposite mark to the robot.
- Detect the human move and associate it with the correct board cell.
- Maintain the board state across alternating turns.
- Select legal robot moves using minimax or another suitable strategy. Rule-based, MATLAB, GitHub-sourced, and generative-AI-assisted implementations are permitted.
- Draw the robot mark inside the selected cell.
- Detect both human and robot wins.
- Detect a full-board draw and command the robot to draw **D** beside the grid.
- Prevent overwriting an occupied cell.
- Maintain approximately **1–2 cm of vertical clearance** above the drawing surface during travel motions between strokes and grid cells.

## Technical Components

| Component | Purpose |
|---|---|
| Board calibration | Relate image-space cells to physical robot coordinates. |
| Visual perception | Detect the grid and classify human and robot marks. |
| Game-state model | Track occupancy, active player, legal moves, wins, and draws. |
| Decision engine | Select the next robot move from the current state. |
| Motion generation | Convert a board-cell decision into a repeatable drawing trajectory. |
| Safety logic | Maintain approximately 1–2 cm of vertical clearance during travel motions and controlled contact with the drawing surface. |

## Demonstration Policy

- The complete project setup must be assembled, calibrated, powered, and ready to run **before the TA or grader is called**.
- Each project is limited to a maximum of **two official demonstration attempts**.

## Deliverables and Grading

| Assessment | Points |
|---|---:|
| Core project: program the robot to play Tic-Tac-Toe against a human | **10** |
| Bonus 1: selectable first player and mark | **+5** |
| Bonus 2: consecutive-human-turn edge-case detection | **+5** |
| Bonus 3: robot-versus-robot game | **+5** |
| **Maximum available** | **25** |

### Core Project — 10 points

Program the robot to draw the grid and play a complete game against a human. The human moves first and selects X or O. The robot must use the opposite mark, recognize each move, select legal responses, detect a win by either player, and identify a draw by writing **D** beside the grid.

### Bonus 1 — 5 points

Support configurable game setup. The system must ask whether the human or robot moves first and allow selection of X or O.

### Bonus 2 — 5 points

Handle the edge case in which the human takes two consecutive turns before the robot responds. The robot must identify the invalid turn sequence and draw **E** beside the grid.

### Bonus 3 — 5 points

Demonstrate a robot-versus-robot Tic-Tac-Toe game completed by two teams.

## Presentation Resources

- [Sample video presentation](https://youtu.be/HTXOMVjY4V4)
- [ASU School of Manufacturing Systems and Networks](https://www.linkedin.com/showcase/school-of-manufacturing-systems-and-networks/)

## Completion Criteria

- [ ] The robot draws a consistent game grid.
- [ ] Camera observations are mapped to the correct board cells.
- [ ] Human and robot marks are represented correctly in the internal game state.
- [ ] The robot selects only legal moves.
- [ ] Drawing trajectories remain within the selected cells.
- [ ] Travel motions maintain approximately 1–2 cm of vertical clearance above the drawing surface.
- [ ] Human-win and robot-win conditions terminate the game correctly.
- [ ] A draw terminates the game and causes the robot to write **D** beside the grid.
