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
  - Microchip PIC
  - PCB design
  - Analog and digital sensing
  - I2C and UART
  - Cadence Allegro
  - Surface-mount assembly
repository_url: "https://github.com/Tatwik19/Team205-Watching-Distance"
schematic_url: "https://github.com/Tatwik19/Team205-Watching-Distance/files/8578224/FINALSCHEMATICBRD.pdf"
poster_url: "https://github.com/Tatwik19/Team205-Watching-Distance/files/8597608/Poster.pdf"
---

## Project Overview

Watching Distance is a wearable depth-perception aid for people who experience impaired depth perception after a stroke. The device measures object distance and displays the result in meters. An MPU-6050 gyroscope detects the raise-and-point interaction.

[Repository]({{ page.repository_url }}) · [PCB schematic]({{ page.schematic_url }}) · [Project poster]({{ page.poster_url }})

## Hardware at a Glance

| Component | Model | Interface / role |
|---|---|---|
| Microcontroller | Microchip **PIC18F27Q43-I/SO** | MCC, ADC, I2C, UART, GPIO |
| Distance sensor | **QSE114**, **GP2S700HCP**, **QED223** | Analog sensing → ADC |
| Inertial sensor | **MPU-6050** | I2C gyroscope |
| Display | **OD-358R** | Digital serial display |
| Display drivers | **MM5452V**, **AS1115-BSST** | Display control |
| Shift register | **SN74LS674DW** | Serial output expansion |
| Signal conditioning | **LM358** | Analog amplification |
| Wireless module | Wi-Fi module | UART / serial |
| Voltage regulator | **AP7361-33E-13** | 3.3 V display rail |
| PCB | Cadence Allegro | Surface-mount layout and routing |

**Protocols:** I2C · UART · ADC · serial shift-register interface · GPIO

## My Contributions

- Integrated the PIC, analog distance sensor, MPU-6050, display, Wi-Fi module, and digital I/O.
- Contributed to the schematic and Cadence Allegro PCB design.
- Developed the raise-and-measure interaction using gyroscope data.
- Supported firmware debugging, hardware revisions, testing, and documentation.

## Results

The team built and tested a compact wearable embedded system that converted live distance data into immediate local feedback. The design demonstrated analog sensing, I2C motion sensing, wireless communication, regulated power distribution, and a functioning custom PCB.

## Project Artifacts

- [GitHub repository]({{ page.repository_url }})
- [PCB schematic]({{ page.schematic_url }})
- [Project poster]({{ page.poster_url }})

![Watching Distance prototype]({{ page.featured_image }})
<!--
-->

<!-- Detailed engineering notes retained below for reference but hidden from the rendered portfolio page.

Watching Distance is a wearable assistive-device prototype for people who retain motor function but experience impaired depth perception after a stroke. The device measures the distance to an object and reports the value in meters on a small display, giving the user an additional cue when reaching for or navigating around nearby objects.

[View repository]({{ page.repository_url }}) · [PCB schematic]({{ page.schematic_url }}) · [Project poster]({{ page.poster_url }})

## Design Approach

The prototype combines distance measurement, inertial sensing, a compact visual display, and wireless embedded control. The inertial sensor acts as an intent cue: measurement is enabled when the user raises and points the device, reducing unnecessary operation when the wearable is lowered.

The project requirements were informed by a conversation with an occupational therapist. The design focuses on simple interaction and direct distance feedback.

## User Need

The project was motivated by the difficulty some stroke survivors experience when judging depth even after motor function has returned. The design provides an additional, low-friction cue through a compact wearable interface. A distance value presented directly on the device supports reaching and near-field navigation while leaving the user's visual attention available for the surrounding environment.

The requirements were informed by discussion with an occupational therapist. That input shaped the interaction around a simple raise-and-measure behavior, direct feedback, and a compact wearable form.

## System Architecture

The prototype combines five functional blocks:

1. **Distance sensing** measures the separation between the device and a nearby object.
2. **Inertial sensing** detects how the user is holding or raising the device and provides the measurement trigger.
3. **Embedded control** processes sensor inputs and coordinates the device behavior.
4. **Display output** presents the measured distance in meters in a compact, readable format.
5. **Wireless communication** supports embedded-system communication and development during the prototype stage.

The resulting signal flow is:

~~~text
User raises and points device
          ↓
Inertial sensing enables measurement
          ↓
Distance sensor acquires range
          ↓
Embedded controller processes value
          ↓
Display presents distance in meters
~~~

## Interaction Model

The inertial sensor acts as an intent cue. When the user raises and points the device, the system enables distance measurement; when the device is lowered or not being used, unnecessary sensing and display updates can be reduced. The feedback loop is deliberately direct:

~~~text
Point → measure → display → adjust position
~~~

## Electronics and PCB Design

The electrical design was captured in a dedicated schematic and assembled into a compact wearable prototype. The schematic documents the connections between the controller, distance-sensing circuitry, inertial sensor, display, power distribution, and wireless interface.

The PCB and enclosure-oriented integration required attention to:

- compact placement of the controller and sensor interfaces;
- stable power and ground connections across sensing and display circuits;
- accessible sensor orientation for measuring the user's viewing direction;
- readable display placement during use; and
- reliable interconnects during repeated prototype testing.

The complete circuit context is available in the [PCB schematic]({{ page.schematic_url }}), while the design motivation and prototype summary are documented in the [project poster]({{ page.poster_url }}).

## Technical Implementation

### Embedded controller

The device is organized around a programmable Microchip PIC microcontroller. The controller manages analog sensor acquisition, I2C peripherals, serial communication, display updates, wireless data transfer, timing, and digital status signals. Microchip Code Configurator (MCC) was used to generate and configure the peripheral drivers used by the firmware.

### Sensors and onboard devices

| Device | Function | Interface or signal type |
|---|---|---|
| Distance sensor | Measures the distance to the object in front of the device | Analog signal acquired through the PIC ADC |
| MPU-6050 inertial sensor | Provides gyroscope data for the raise-and-point interaction | I2C register reads and writes |
| Local display | Presents the measured distance in meters | I2C |
| Wireless module | Sends measurement and gyroscope data outside the device | UART/serial communication and Wi-Fi |
| Shift register | Expands or manages serially controlled output signals | Serial interface |
| LEDs and status signals | Indicate message reception and device state | Digital GPIO |

The design combines analog acquisition with digital peripheral buses. The PIC samples the distance-sensor output through its ADC, reads the inertial sensor through I2C, updates the display through I2C, and uses serial communication for the wireless subsystem. This mixed-signal architecture allowed the prototype to combine a compact analog sensing path with digital motion and communication functions.

### Firmware and signal-processing flow

The firmware coordinates the following functions:

1. Initialize the PIC peripherals, display, inertial sensor, ADC, and serial interfaces.
2. Read the analog distance sensor and convert the ADC result into a usable distance value.
3. Read gyroscope registers over I2C to identify the device's movement and orientation.
4. Format distance information for the local display.
5. Send distance and gyroscope values through the Wi-Fi communication path.
6. Toggle an LED when a communication message is received to support debugging and validation.
7. Use software service routines and interrupt-driven serial support while testing the communication path.

The final prototype produced gyroscope values. Angular-velocity and temperature readings were not completed. Testing also identified noise and inconsistent measurements, establishing calibration and complementary or Kalman filtering as the next signal-processing priorities.

### Electrical interfaces

The design uses a mixture of digital buses and discrete digital signals:

| Interface | Role in the prototype |
|---|---|
| I2C | Register-level communication with the MPU-6050 and display |
| ADC | Samples the analog distance-sensor output |
| UART/serial | Exchanges data with the wireless subsystem |
| Serial shift-register interface | Controls additional digital outputs |
| Digital GPIO | LEDs, enables, status, and other discrete control signals |
| Power and ground rails | Provide regulated supply and a common reference for the controller and peripherals |

### Power architecture and hardware revisions

The prototype used regulated power rails. One regulator powered the PIC, distance-sensing circuitry, and wireless module. After the display was changed, an additional 3.3 V regulator provided a separate supply path for the display-related circuitry and shift register. The replacement display drew approximately 500 mA, making power integrity a central part of the hardware revision.

Several hardware revisions were made during integration:

- The inertial sensor address/configuration pin was tied low because only one sensor was used.
- External I2C pull-up resistors were removed because the inertial-sensor breakout already included pull-ups; adding another set in parallel would have reduced the effective resistance.
- The original display was replaced with a better-documented, more suitable display.
- An unnecessary external pull-up connection for a display pin was omitted because the pin was already pulled high internally.
- The additional 3.3 V regulator was added after the display change to reduce communication and power-delivery problems.

## Schematic and PCB Workflow

The circuit was developed from a complete schematic before board integration. The design workflow included:

1. Define the controller, sensor, display, wireless, power, and connector blocks.
2. Assign digital buses, GPIO signals, power rails, and ground returns.
3. Check signal direction and pin compatibility at each device boundary.
4. Capture the schematic and create the PCB design in Cadence Allegro.
5. Place the controller and high-use peripherals for a compact wearable layout.
6. Route power, ground, digital buses, and timing-sensitive distance signals.
7. Add design-rule checks, silkscreen references, test access, and assembly information.
8. Review the board against the schematic before fabrication and assembly.

Cadence Allegro was used for the PCB design workflow, including component placement, copper routing, footprints, design-rule checking, and manufacturing documentation. The project produced a functioning custom PCB with a surface-mount-oriented layout. Breakout boards supported component-level prototyping and integration. The layout required attention to component footprints, pad geometry, polarity markings, silkscreen readability, reflow-compatible placement, and inspection access.

### Surface-mount assembly considerations

The surface-mount implementation reduced board area and supported the wearable form factor, but it also introduced practical manufacturing constraints:

- use the correct footprint and land pattern for every SMD package;
- keep polarized components and IC pin 1 clearly marked;
- avoid silkscreen overlap with pads or component bodies;
- maintain appropriate clearance around fine-pitch and connector areas;
- provide accessible test points for power, ground, I2C, GPIO, and serial signals;
- inspect solder joints for bridges, opens, tombstoning, and insufficient wetting; and
- verify power and continuity before installing or enabling the remaining peripherals.

This hardware workflow connected the electrical schematic to a functioning custom board. The report identifies future miniaturization steps: correcting the replacement-display footprint, using a smaller sensor breakout or bare sensor IC, using surface-mount LEDs, and reducing board area through tighter routing and thinner traces within fabrication rules.

## Design Decisions

| Design decision | Reason |
|---|---|
| Direct distance value on a local display | Immediate feedback without a phone or external screen |
| Inertial raise-to-measure interaction | Reduces unintended measurements and provides a simple physical trigger |
| Wearable form factor | Keeps the sensing and feedback system available while the user moves or reaches |
| Embedded processing | Keeps the core interaction local and responsive |
| Modular prototype electronics | Allows sensing, display, wireless, and control elements to be revised independently |
| Separate regulated display rail | Supports the high-current display and reduces interference with the controller and sensing electronics |
| Integrated sensor pull-ups | Avoids excessive parallel pull-up resistance on the I2C bus |

## My Contributions

- Supported the embedded architecture and integration of sensing, display, and wireless functions.
- Contributed to schematic and PCB development.
- Helped prototype the raise-to-measure interaction using inertial data.
- Participated in system testing and documentation for the final poster and design package.

## Testing and Outcome

The team built and tested a wearable embedded system that translated live sensor data into an immediately readable distance value. Testing covered the complete interaction path: raising and pointing the device, acquiring a distance measurement, processing the signal, and presenting the result on the display.

The prototype demonstrated:

- distance measurement integrated into a wearable device;
- inertial sensing used as an interaction trigger;
- local display feedback in meters;
- coordinated embedded sensing and output;
- a documented schematic and assembled PCB-level design; and
- a complete design package suitable for technical review.

The final prototype enclosure target was approximately **40 mm × 40 mm × 15 mm**, making packaging and power distribution important constraints alongside firmware functionality.

## Next Development Priorities

Testing established the following development priorities:

- evaluate the device with a broader set of users and real-world tasks;
- characterize measurement accuracy across surfaces, angles, and distances;
- improve ergonomics, weight distribution, and comfort for longer use;
- refine the display for different visual abilities and lighting conditions;
- add robust fault handling for invalid or noisy measurements;
- improve the analog distance-sensor calibration and add complementary or Kalman filtering;
- replace blocking delays with nonblocking firmware so sensing, display, and communication can run more seamlessly;
- add low-power behavior after a period without motion;
- explore bidirectional Bluetooth or a mobile application for future patient-facing features; and
- complete clinical, safety, and accessibility evaluation before deployment.

## Project Artifacts

| Artifact | Purpose |
|---|---|
| [GitHub repository]({{ page.repository_url }}) | Source files and project documentation |
| [PCB schematic]({{ page.schematic_url }}) | Electrical design and component interconnections |
| [Project poster]({{ page.poster_url }}) | Design motivation, architecture, results, and presentation summary |

![Watching Distance prototype]({{ page.featured_image }})
