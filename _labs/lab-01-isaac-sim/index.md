---
title: "Lab 1: Isaac Sim Basic Usage and First Physics Simulation"
lab_number: 1
course: "RAS 545: Robotics Systems I"
status: complete
summary: "Learn how to open Isaac Sim, create a USD stage and simple scene, add lights and objects, and run a basic rigid-body physics simulation."
description: "A hands-on Isaac Sim laboratory covering USD stages, scene creation, lighting, objects, and basic rigid-body physics simulation."
topics:
  - Isaac Sim
  - USD stages
  - Rigid-body physics
layout: lab
permalink: /labs/lab-01-isaac-sim/
date: 2026-09-12
author_profile: false
classes: wide
hide_page_metadata: true
---

<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {
  mermaid.initialize({ startOnLoad: false, theme: "default" });
  document.querySelectorAll("pre > code.language-mermaid").forEach(function (code) {
    var pre = code.parentElement;
    var div = document.createElement("div");
    div.className = "mermaid";
    div.textContent = code.textContent;
    pre.replaceWith(div);
  });
  mermaid.run();
});
</script>
<style>
@media print {
  .mermaid,
  pre,
  table,
  blockquote {
    break-inside: avoid;
    page-break-inside: avoid;
  }
}
</style>

**Instructor:** Prof. [Sangram Redkar](mailto:Sangram.Redkar@asu.edu)

**Authors:**

- Sai Srinivas Tatwik Meesala: [smeesala@asu.edu](mailto:smeesala@asu.edu)

- Prajval Arora: [parora24@asu.edu](mailto:parora24@asu.edu)

---

> **Required scope:** Complete Parts A–G and submit the required checkpoint files, screenshots, formal report, and demonstration video. The final check-off occurs after successful completion of Part G.

## Start Here

Complete the laboratory in order:

1. Read the software requirements and the linked NVIDIA GUI tutorial.
2. Create the `Lab1/checkpoints/` and `Lab1/screenshots/` directories.
3. Complete each part before moving to the next one.
4. Save a checkpoint stage and capture the required screenshot after every part.
5. Record the procedure, results, observations, and key learning in the formal report.
6. Notify the teaching staff for check-off after the final physics validation succeeds.

## Reference Tutorial

This laboratory follows the GUI workflow in the official [Isaac Sim Basic Usage Tutorial](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/introduction/quickstart_isaacsim.html).

Complete only the **GUI** tab. Do not complete the Extension or Standalone Python workflows for this laboratory.

## What You Will Do

You will:

1. Launch Isaac Sim.
2. Create and save a new USD stage.
3. Add a ground plane and light source.
4. Add, rename, move, rotate, and scale a cube.
5. Run the scene before physics is added.
6. Add rigid-body and collision properties.
7. Run the scene with gravity and verify that the cube falls and collides with the ground.

## Learning Goals

By the end of this laboratory, you will be able to:

- Navigate the Isaac Sim interface.
- Create and save objects in a USD stage.
- Modify object transforms.
- Distinguish visual geometry from physical geometry.
- Add rigid-body and collision properties.
- Run and stop a simulation.
- Explain the observed physics behavior.

## Required Software and Files

- Isaac Sim 6.0.1
- NVIDIA graphics driver
- A working Isaac Sim installation
- A directory for laboratory files

Create these folders before starting:

```text
Lab1/
├── checkpoints/
└── screenshots/
```

## Laboratory Roadmap

| Part | Main task | Required result | Checkpoint |
|---|---|---|---|
| A | Launch and save a blank stage | Isaac Sim is loaded and the stage is saved | `Lab1_00_blank_stage.usda` |
| B | Add a ground plane | Ground plane exists at approximately `(0, 0, 0)` | `Lab1_01_ground_plane.usda` |
| C | Add a distant light | Scene is visibly illuminated | `Lab1_02_lit_stage.usda` |
| D | Add and transform a cube | Cube is at approximately `(0, 0, 1)` with the required transform | `Lab1_03_cube_scene.usda` |
| E | Run without physics | Cube remains stationary | `Lab1_04_cube_without_physics.usda` |
| F | Add rigid body and colliders | Cube has physics properties | `Lab1_05_cube_physics.usda` |
| G | Run the physics simulation | Cube falls, collides, and comes to rest | `Lab1_06_final.usda` |

# Part A: Launch Isaac Sim

## A1. Launch the simulator

Launch Isaac Sim using the instructions for your operating system in the NVIDIA tutorial.

For Ubuntu, the command is typically:

```bash
cd ~/isaacsim
./isaac-sim.sh
```

For Windows, use the Isaac Sim batch file described in the tutorial. Wait until the interface is completely loaded.

> **Checkpoint:** Do not continue while Isaac Sim is still loading.

## A2. Identify the main interface areas

Locate the following areas:

| Interface area | Purpose |
|---|---|
| Viewport | Displays the simulated scene |
| Stage panel | Displays the USD scene hierarchy |
| Property panel | Displays properties of the selected object |
| Timeline | Controls simulation time |
| Play button | Starts the simulation |
| Stop button | Stops and resets the simulation |

Capture `screenshots/01_isaac_sim_interface.png` showing the interface.

## A3. Create a new stage

Select **File → New**. If prompted to save the current stage, select **Discard**. Then select **File → Save As** and save:

```text
Lab1/checkpoints/Lab1_00_blank_stage.usda
```

### Validation checkpoint A

The simulator is loaded, the main interface areas are visible, and the blank stage is saved.

# Part B: Create a Ground Plane

Select **Create → Physics → Ground Plane**. Confirm that the ground plane appears in the viewport and in the Stage panel. Its position should be approximately:

```text
Position X = 0.0
Position Y = 0.0
Position Z = 0.0
```

Do not delete the ground plane. Save:

```text
Lab1/checkpoints/Lab1_01_ground_plane.usda
```

Capture `screenshots/02_ground_plane.png`.

### Validation checkpoint B

The ground plane exists, is visible in the viewport, and is located approximately at the world origin.

# Part C: Add a Light Source

Select **Create → Lights → Distant Light** and rename the light `DistantLight`. If the scene is too dark, rotate the light until the ground plane is visible. The exact rotation is not important.

Save:

```text
Lab1/checkpoints/Lab1_02_lit_stage.usda
```

Capture `screenshots/03_distant_light.png` showing the light in the Stage panel and the illuminated scene.

### Validation checkpoint C

The Stage panel contains `DistantLight`, and the scene is sufficiently illuminated to see the ground plane and future cube.

# Part D: Add and Transform a Cube

## D1. Create the cube

Select **Create → Shape → Cube** and rename the cube `Cube`.

![Adding a cube to an Isaac Sim stage](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/_images/isim_4.5_base_tut_gui_add_cube.webp)

## D2. Set the cube transform

Select `Cube` and set approximately:

```text
Position X = 0.0
Position Y = 0.0
Position Z = 1.0

Rotation X = 0.0 degrees
Rotation Y = 0.0 degrees
Rotation Z = 0.0 degrees

Scale X = 1.0
Scale Y = 1.0
Scale Z = 1.0
```

## D3. Practice the transform tools

Use the following shortcuts:

```text
W = Move tool
E = Rotate tool
R = Scale tool
Esc = Deselect
```

Move, rotate, and scale the cube, then restore the required transform above.

![Moving, rotating, and scaling an object](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/_images/isim_4.5_base_tut_gui_move_cube.webp)

Save:

```text
Lab1/checkpoints/Lab1_03_cube_scene.usda
```

Capture `screenshots/04_cube_transform.png` showing the cube, Stage panel, and Property panel.

### Validation checkpoint D

The cube exists, is named `Cube`, and has the required position, rotation, and scale.

# Part E: Run the Cube Without Physics

Press **Play**, observe the cube, and then press **Stop**.

Expected result: the cube does not fall because it is currently visual geometry without rigid-body or collision properties.

Save:

```text
Lab1/checkpoints/Lab1_04_cube_without_physics.usda
```

Capture `screenshots/05_cube_without_physics.png` showing the cube during the simulation.

### Validation checkpoint E

The cube remains stationary before physics is added. Record this observation in the report and explain why it occurs.

# Part F: Add Physics to the Cube

Select `Cube`. In the Property panel, select **Add**, choose the physics properties category, and apply **Rigid Body with Colliders Preset**. This adds both rigid-body and collision properties.

![Adding physics and collision properties](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/_images/isim_4.5_base_tut_gui_physics_property.webp)

Save:

```text
Lab1/checkpoints/Lab1_05_cube_physics.usda
```

Capture `screenshots/06_cube_physics_properties.png` showing the cube selected and the physics properties visible.

### Validation checkpoint F

The cube has rigid-body and collision properties, and the physics configuration is visible in the Property panel.

# Part G: Run the Physics Simulation

Press **Play**. The cube should fall under gravity, collide with the ground plane, and stop when it reaches the ground. Press **Stop** after observing the result.

If the cube does not fall, check that the cube is selected, the rigid-body preset was applied, the ground plane exists, Isaac Sim is playing, and the cube starts above the ground.

Save the completed scene:

```text
Lab1/checkpoints/Lab1_06_final.usda
```

Capture `screenshots/07_cube_with_physics.png` showing the cube in the viewport, the cube selected in the Stage panel, and the rigid-body properties in the Property panel.

### Validation checkpoint G

The cube falls under gravity, collides with the ground plane, and comes to rest. Record the result, observations, and any troubleshooting in the report.

# Required Deliverables

Submit the following checkpoint files:

```text
Lab1_00_blank_stage.usda
Lab1_01_ground_plane.usda
Lab1_02_lit_stage.usda
Lab1_03_cube_scene.usda
Lab1_04_cube_without_physics.usda
Lab1_05_cube_physics.usda
Lab1_06_final.usda
```

Also submit:

```text
screenshots/01_isaac_sim_interface.png
screenshots/02_ground_plane.png
screenshots/03_distant_light.png
screenshots/04_cube_transform.png
screenshots/05_cube_without_physics.png
screenshots/06_cube_physics_properties.png
screenshots/07_cube_with_physics.png
```

Submit a short demonstration video showing the cube before physics, the physics properties, and the cube falling and colliding with the ground plane.

## Report Expectations

Submit one comprehensive formal lab report using the [RAS 545 Lab Report Template](https://docs.google.com/document/d/1HOYJqnCjeE1o-8Ghffh58nG2FxjORW-J/edit?usp=sharing&ouid=109541660202730576301&rtpof=true&sd=true).

The report must contain:

1. Title page.
2. Lab objectives and learning goals.
3. Software and hardware configuration.
4. Procedure for Parts A–G.
5. Results and validation evidence.
6. Observations and troubleshooting.
7. Screenshots after every part, A through G.
8. Explanation of visual geometry versus physical geometry.
9. Key learnings.
10. Conclusion.
11. References.

For each part, include the procedure followed, the corresponding checkpoint filename, the screenshot filename, the observed result, any error and correction, and one key learning. The report must explain why the cube remains stationary without physics and why it falls after the rigid-body and collider preset is added.


# Lab Check-Off

The final check-off is required after Part G. Notify the teaching staff immediately after the final scene is successfully saved and the physics simulation has been compiled, executed, and verified.

The check-off must confirm:

1. Isaac Sim launched successfully.
2. The blank stage was created and saved.
3. A ground plane and distant light exist.
4. The cube exists with the required transform.
5. The cube remained stationary before physics was added.
6. Rigid-body and collision properties were added.
7. The cube fell under gravity and collided with the ground plane.
8. The Part A–G checkpoint files, screenshots, report, and video are available.

The demonstration must show the working simulation, not only screenshots or code.

# Final Validation

Before submission, verify:

- [ ] Isaac Sim launched successfully.
- [ ] A new stage was created and saved.
- [ ] A ground plane exists at approximately the origin.
- [ ] A distant light exists and illuminates the scene.
- [ ] A cube exists and has the required transform.
- [ ] The cube remained stationary before physics was added.
- [ ] Rigid-body and collision properties were added.
- [ ] The cube fell under gravity.
- [ ] The cube collided with the ground plane and came to rest.
- [ ] All Part A–G checkpoint files were saved.
- [ ] Screenshots were captured after every part.
- [ ] The formal report was completed using the template.
- [ ] The demonstration video was recorded.
- [ ] Teaching staff were notified for the final check-off.

## Completion Requirement

The laboratory is complete when the student can demonstrate that a cube was created in Isaac Sim, remained stationary without physics, received rigid-body and collision properties, and then fell and collided with the ground plane under gravity.
