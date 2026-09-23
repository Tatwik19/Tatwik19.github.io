---
title: "Watching Distance: Wearable Depth-Perception Aid"
collection: portfolio
date: 2022-04-30
project_period: "Jan 2022 – Apr 2022"
summary: "Developed a wearable embedded prototype that measures object distance and presents it on a compact display for users with impaired depth perception after stroke."
role: "Embedded-system integration, PCB development, and prototyping"
featured_image: "https://user-images.githubusercontent.com/96451759/166118037-aef595fe-bed9-4bc8-a2e5-96a3eada7e6c.jpg"
featured_image_alt: "Watching Distance wearable embedded-system prototype"
technologies:
  - Embedded systems
  - PCB design
  - Distance sensing
  - Inertial sensing
  - Wireless communication
repository_url: "https://github.com/Tatwik19/Team205-Watching-Distance"
schematic_url: "https://github.com/Tatwik19/Team205-Watching-Distance/files/8578224/FINALSCHEMATICBRD.pdf"
poster_url: "https://github.com/Tatwik19/Team205-Watching-Distance/files/8597608/Poster.pdf"
---

## Project Overview

Watching Distance is a wearable assistive-device prototype for people who retain motor function but experience impaired depth perception after a stroke. The device measures the distance to an object and reports the value in meters on a small display, giving the user an additional cue when reaching for or navigating around nearby objects.

[View repository]({{ page.repository_url }}) · [PCB schematic]({{ page.schematic_url }}) · [Project poster]({{ page.poster_url }})

## Design Approach

The prototype combines distance measurement, inertial sensing, a compact visual display, and wireless embedded control. The inertial sensor acts as an intent cue: measurement is enabled when the user raises and points the device, reducing unnecessary operation when the wearable is lowered.

The project requirements were informed by a conversation with an occupational therapist, which kept the design focused on simple interaction and direct distance feedback rather than a complex user interface.

## My Contributions

- Supported the embedded architecture and integration of sensing, display, and wireless functions.
- Contributed to schematic and PCB development.
- Helped prototype the raise-to-measure interaction using inertial data.
- Participated in system testing and documentation for the final poster and design package.

## Outcome

The team produced a wearable proof of concept that translated live sensor data into an immediately readable distance value. The project demonstrated a practical human-centered use of embedded sensing while identifying the need for additional clinical evaluation, ergonomic refinement, and broader user testing before any real-world assistive deployment.

![Watching Distance prototype]({{ page.featured_image }})
