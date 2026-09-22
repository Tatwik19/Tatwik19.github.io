---
title: "Lab 2: Six-Degree-of-Freedom Robot"
lab_number: 2
course: "RAS 545: Robotics Systems I"
status: under-preparation
summary: "A planned Isaac Sim laboratory focused on six-degree-of-freedom robot modeling, manipulation, and control."
topics:
  - Isaac Sim
  - Robot manipulation
  - Six-degree-of-freedom systems
layout: lab
permalink: /labs/lab-02-isaac-sim/
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

> **Status:** This laboratory is under preparation. The scope and deliverables will be finalized before release.

## Planned Scope

This laboratory is planned as the bridge between the introductory physics exercise in Lab 1 and the ROS 2 mobile-robot integration sequence in Lab 3.

Planned topics include:

- Importing and validating a six-degree-of-freedom robot model.
- Configuring joints, actuators, and rigid-body properties.
- Building a basic manipulation or trajectory workflow.
- Connecting simulation results to robotics concepts such as coordinate frames, kinematics, and control.

## Planned Deliverables

The final checkpoint files, screenshots, report requirements, and validation procedure will be published when the laboratory is complete.

