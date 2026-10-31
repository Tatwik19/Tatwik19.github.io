---
title: "Midterm 2: Vision-Guided 4 × 4 Maze Solving"
lab_number: 2
card_label: "Midterm 2"
lab_series: assessments
course: "RAS 545: Robotics Systems I"
status: complete
summary: "Transform a camera image of a 4 × 4 maze into a collision-free physical path and command the robot end effector to trace the solution."
description: "A robotics assessment integrating camera calibration, perspective correction, maze perception, graph search, coordinate transformation, path planning, and robot motion."
topics:
  - Computer vision
  - Camera calibration
  - Graph search
  - Path planning
  - Robot motion control
layout: lab
permalink: /labs/midterm-02-maze-solving/
date: 2025-11-07
author_profile: false
classes: wide
hide_page_metadata: true
---

**Instructor:** Prof. [Sangram Redkar](mailto:Sangram.Redkar@asu.edu)

> **Source materials:** [Assignment brief]({{ '/labs/midterm-02-maze-solving/midterm-2-maze-assignment.pdf' | relative_url }}) · [Download starter code]({{ '/labs/midterm-02-maze-solving/midterm-2-starter-code.zip' | relative_url }})

## Assessment Overview

This midterm develops an autonomous pipeline for solving printed 4 × 4 mazes. A camera image is converted into a geometric maze representation, a valid route is calculated from entrance to exit, and the solution is transformed into physical robot coordinates. The robot end effector then follows the path as connected straight-line segments.

The solution is expected to generalize across rectangular 4 × 4 mazes produced with the [Maze Generator](https://www.mazegenerator.net/), rather than relying on one fixed board.

## System Pipeline

~~~text
Camera image
    ↓
Maze-boundary detection and perspective correction
    ↓
Wall, grid, entrance, and exit extraction
    ↓
Graph representation of the 4 × 4 maze
    ↓
Maze search and waypoint simplification
    ↓
Pixel-to-robot coordinate transformation
    ↓
Safe straight-line end-effector motion
~~~

## Maze and Workspace Requirements

- Use a maze with four rows and four columns.
- Keep the maze within an approximately 3.5 × 3.5 inch robot workspace.
- Place the entrance at the top or bottom boundary rather than inside the maze.
- Accept variations in the maze-generation parameters.
- Determine the entrance, exit, and solution path automatically from the camera image.
- Convert image-space path points into physical robot waypoints.
- Follow the solution using straight-line sections.

## Starter-Code Package

The [starter-code archive]({{ '/labs/midterm-02-maze-solving/midterm-2-starter-code.zip' | relative_url }}) contains two complementary workflows.

### Camera Calibration and Robot Motion

- camera acquisition and pixel-coordinate selection;
- affine and homography estimation;
- image-to-robot coordinate conversion;
- robot homing, pose feedback, and point-to-point motion; and
- execution of maze waypoints in the physical workspace.

### Maze Perception and Planning

| Stage | Included capability |
|---|---|
| Image capture | Acquire the maze image and identify its boundary. |
| Perspective correction | Warp the detected board into a normalized top-down view. |
| Grid extraction | Detect walls, circles, cells, and grid structure. |
| Maze solution | Build the maze representation and calculate a path using breadth-first search. |
| Path projection | Map the solved path back onto the original camera image. |

The package uses Python with OpenCV, NumPy, Pillow, and robot-control utilities.

## Calibration and Coordinate Mapping

The perception pipeline produces waypoints in image coordinates. Robot execution requires a calibrated transformation from image pixels (u, v) to physical workspace coordinates (x, y).

An affine transformation is suitable when the camera view is approximately planar with limited perspective distortion:

~~~text
[x  y  1]ᵀ = A [u  v  1]ᵀ
~~~

A homography provides a projective mapping when perspective effects are significant. Calibration quality should be evaluated at multiple points across the usable maze area.

## Path Planning and Robot Execution

The detected maze can be represented as a graph whose nodes are cells and whose edges are traversable neighboring relationships. Breadth-first search, A*, or another justified search method can generate the route from entrance to exit.

The cell path should be simplified into straight sections before robot execution. Each section is transformed into robot coordinates and executed at a safe height above the maze board.

## Demonstration Criteria

- Maintain approximately 10–20 cm of vertical clearance above the board.
- Follow a path that closely matches the calculated maze solution.
- Produce straight, stable path segments.
- Generalize across different 4 × 4 mazes.
- Demonstrate reliable image processing and coordinate conversion.
- Complete the task efficiently and robustly.
- Include a safe stop or return-to-home behavior.

## Evaluation

The original assessment is worth **40 points**. Evaluation emphasizes:

- correctness of the maze solution;
- generality across maze configurations;
- quality of camera calibration and physical waypoint estimation;
- path accuracy, efficiency, and smoothness;
- robustness to image and setup variation; and
- safe robot behavior.

## References

### Vision and Calibration

- [ArUco marker overview](https://www.vision.ee.ethz.ch/en/vision/software/aruco.html)
- [OpenCV ArUco detection](https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html)
- [MATLAB TCP/IP communication](https://www.mathworks.com/help/matlab/matlab-engine/tcp-ip-communication.html)

### Robot Modeling and Motion

- [Robot modeling in MATLAB](https://www.youtube.com/playlist?list=PLWF9TXck7O_ymYWT8Q33omPb5K-A5v4Ae)
- [Simscape Multibody simulation](https://www.youtube.com/watch?v=pDiwAA1cnb0&t=2283s)
- [Forward kinematics in MATLAB](https://www.youtube.com/watch?v=xpA8TKEMpMk)
- [Robot trajectory planning in MATLAB](https://www.youtube.com/watch?v=Fd7wjZDoh7g)
- [URDF introduction](https://www.youtube.com/watch?v=CwdbsvcpOHM)
- [ROS robot fundamentals](https://www.youtube.com/watch?v=2lIV3dRvHmQ&list=PLunhqkrRNRhYYCaSTVP-qJnyUPkTxJnBt)
- [IKFast documentation](https://openrave.org/docs/latest_stable/openravepy/ikfast/#ik-types)

### Maze Solving

- [Maze Generator help](https://www.mazegenerator.net/Help.aspx)
- [MATLAB maze-solving discussion](https://www.mathworks.com/matlabcentral/answers/711803-random-maze-solving-algorithm-with-matrix)
- [Watershed-transform maze solving](https://www.mathworks.com/company/technical-articles/tips-and-tricks-solving-a-maze-with-the-watershed-transform.html)
- [Python maze solver](https://thecleverprogrammer.com/2021/01/26/maze-solver-with-python/)
- [Recursive and A* maze search](https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/)

## Completion Criteria

- [ ] The maze is detected and normalized from the camera image.
- [ ] Entrance, exit, walls, and traversable cells are identified.
- [ ] A valid solution path is generated automatically.
- [ ] Pixel coordinates are transformed into physical robot coordinates.
- [ ] The robot follows the path with safe clearance and straight segments.
- [ ] The solution generalizes across multiple 4 × 4 maze configurations.
- [ ] The demonstration documents perception, planning, calibration, and execution.
