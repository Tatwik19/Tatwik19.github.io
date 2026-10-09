---
title: "Lab 1: Cell Power, Safety, and Network Setup"
lab_number: 1
lab_series: automation
course: "RAS 598: Industrial Robotics & Smart Factory Automation"
status: under-preparation
summary: "Build the IIoT workcell foundation: safe 24 VDC power, an E-stop input, an isolated Ethernet network, and a first Modbus TCP exchange with a Micro850 PLC."
description: "The first automation laboratory establishes the power, safety, controller, network, and Modbus foundation used by the remaining workcell labs."
topics:
  - 24 VDC control wiring
  - Emergency-stop circuits
  - Allen-Bradley Micro850 and CCW
  - Ethernet and static IP configuration
  - Modbus TCP
  - Python and pymodbus
layout: lab
permalink: /labs/lab-01-automation/
date: 2026-10-08
author_profile: false
classes: wide
hide_page_metadata: true
---

> **Status:** This laboratory is under preparation. Complete all energized wiring and controller work only with instructor approval and the equipment-specific wiring diagram in front of you.

**Course:** RAS 598: Industrial Robotics & Smart Factory Automation  
**Platform:** Allen-Bradley Micro850, Connected Components Workbench (CCW), Windows laptop, Ethernet switch, Python, and Wireshark

## Start Here

This laboratory establishes the shared foundation for the automation workcell. Later labs will add robots, sensors, conveyors, vision, and supervisory software to the same controller and network. Work with the cell laptop and Micro850 only; do not connect the cell switch to a building or campus network.

Complete the laboratory in order:

1. Read the safety requirements and inspect the equipment.
2. Build and verify the 24 VDC distribution with power removed.
3. Wire and validate the normally closed emergency-stop input.
4. Cable the isolated Ethernet network and assign static addresses.
5. Configure the Micro850 in CCW and confirm an Ethernet connection.
6. Create the Modbus TCP variables and mapping.
7. Download a temporary test program and verify it from Python.
8. Monitor the PLC from a second client and inspect the exchange in Wireshark.

## Lab Objective

By the end of this lab, the cell should have a fused 24 VDC supply, a functioning E-stop input wired to the PLC, and a dedicated Ethernet network on which a Python script can read and write data in the Micro850. The PLC coordinates the cell; small Python bridge programs later translate between the PLC job/status registers and each device's native protocol.

## Learning Outcomes

- Explain why a workcell uses a dedicated, static-address Ethernet network.
- Build and check low-voltage DC distribution using correct polarity, common, wire color, and fuse practices.
- Explain why an E-stop input is normally closed and how a broken wire appears to the controller.
- Configure a Micro850 project and Ethernet settings in CCW.
- Distinguish a Modbus register number from its zero-based protocol address.
- Read coils and holding registers and write a test register using Python and pymodbus.
- Use a second client and Wireshark to observe polling, responses, and an addressing error.

## Safety and Workcell Rules

> **Important:** This page is an instructional summary, not a substitute for the instructor-approved schematic or manufacturer's documentation.

- Keep the mains side of the power supply de-energized; only the instructor may connect or modify mains wiring.
- Disconnect power before changing field wiring. Check continuity and polarity before the first power-on.
- Use the specified fuse, wire colors, terminals, and current limits for the assigned cell.
- Do not bypass the E-stop, defeat a guard, or energize an actuator to troubleshoot communication.
- This training cell implements a PLC-monitored software stop. Production equipment also requires an appropriately rated hardware safety circuit or safety relay.
- Do not connect the isolated cell switch to the building, campus, or home network.

## Equipment and Software

### Hardware

- Allen-Bradley Micro850 controller with Ethernet and digital I/O
- 24 VDC power supply, inline fuse holder, WAGO-style connectors, and labeled wiring
- Red mushroom E-stop with a normally closed contact block
- Ethernet switch and Cat5e-or-better patch cables
- Windows cell laptop and USB programming cable
- Multimeter, wire stripper, ferrule crimper, screwdriver, labels, and marker

### Software

- Connected Components Workbench (CCW), Standard Edition
- Python 3.10 or newer
- pymodbus 3.6 or newer
- Wireshark

~~~text
pip install "pymodbus>=3.6"
~~~

## Part A: Power, E-Stop, and Cell I/O

### A1. Build the 24 VDC distribution

With the supply unplugged, use the approved cell diagram to distribute the fused 24 VDC supply to the Micro850 and its I/O. The reference cell uses a common 0 V return and sourcing field devices. Verify every terminal name on the actual controller; terminal names in the handout are generic.

Before powering the cell, check supply polarity, continuity, fuse placement and rating, the 24 V/0 V distribution points, and exposed conductors.

### A2. Wire the E-stop input

Wire the E-stop's normally closed contact to the assigned PLC input. In the program it is represented as EStop_OK:

| Condition | Expected state |
|---|---|
| E-stop released | EStop_OK = TRUE |
| E-stop pressed | EStop_OK = FALSE |
| Broken wire or loose terminal | EStop_OK = FALSE |

The normally closed arrangement is fail-oriented: loss of continuity must not look like an all-clear condition.

### A3. Record the fixed I/O allocation

Create an I/O map from the approved wiring diagram. Later labs depend on this fixed allocation.

| Signal | Role in the cell | Record |
|---|---|---|
| EStop_OK | E-stop healthy, normally closed input | PLC input address |
| Carrier_Datum | Carrier datum or axis-home sensor | PLC input address |
| Vac_Present | Vacuum controller status | PLC input address |
| Cmd_Word | Device job/command register | Modbus holding-register address |
| Status_Word | Device status register | Modbus holding-register address |

### A4. Verify the first power-on

Power on only after the instructor checks the wiring. Record the measured voltage at the PLC terminals.

| Check | Expected result |
|---|---|
| PLC power indicator | On |
| PLC supply voltage | Approximately 24 VDC, within equipment specification |
| E-stop released | EStop_OK is on/true |
| E-stop pressed | EStop_OK is off/false |

**Checkpoint A:** The PLC is powered and the E-stop input follows the button state.

## Part B: Network Plan and Cabling

### B1. Use an isolated static-address network

The reference cell uses a private 192.168.10.x subnet with a 255.255.255.0 mask and no gateway. Static addresses keep the cell predictable; DHCP is not used because a device address must not change after a restart.

The reference handout uses 192.168.10.10 for the Micro850 and reserves separate addresses for the laptop, robot controllers, and future device servers. Record the actual values provided for your workstation.

### B2. Cable the cell

1. Place the switch next to the PLC and power it using its approved adapter.
2. Connect the laptop and Micro850 to separate switch ports.
3. Label both ends of each cable, such as PLC and Laptop.
4. Confirm that the link indicator is lit on every used port.
5. Leave the switch disconnected from all outside networks.

### B3. Configure the laptop

Open the Ethernet adapter's IPv4 properties and assign the static address provided by the instructor. Use the same subnet as the PLC, a 255.255.255.0 mask, and no gateway unless instructed otherwise. Confirm the setting with ipconfig.

**Checkpoint B:** The laptop and PLC are connected through the isolated switch and have compatible static addresses.

## Part C: Configure the Micro850 in CCW

Create a new CCW project for the assigned controller. Add the correct Micro850 model and firmware revision, configure the Ethernet driver and PLC address, then:

1. Create a project named IIoT_Workcell.
2. Add the assigned Micro850 controller.
3. Set the controller IP address and subnet mask.
4. Build the project and resolve all errors.
5. Browse for the PLC over Ethernet in the Connection Browser.
6. Download the project and accept the remote-program prompt.
7. Place the controller in Remote Run only after the wiring check is complete.

**Checkpoint C:** CCW shows the expected controller connected over Ethernet and the project is downloaded without build errors.

## Part D: Create the Temporary Test Program

Create global variables for the E-stop and first Modbus test registers. For the initial round-trip test, echo Cmd_Word into Status_Word.

~~~iecst
(* TEMPORARY test for Lab 1: echo the command into its status *)
(* Delete this program before starting Lab 3 *)
Status_Word := Cmd_Word;
~~~

Build, download, and run the project. In CCW's Global Variables view, observe EStop_OK. Press and release the E-stop and record the transitions.

**Checkpoint D:** The E-stop state is visible in the running controller and the temporary echo program is active.

## Part E: Map and Test Modbus TCP

The Micro850 acts as the Modbus TCP server. Python bridge programs, Ignition, dashboards, and loggers act as clients. Modbus uses coils for bit values and holding registers for integer values.

> **Addressing rule:** Documentation and SCADA tools may show register 400001, but Python pymodbus uses the zero-based protocol address 0. Thus 400002 is protocol address 1.

| PLC variable | Modbus representation | Python protocol address | Purpose |
|---|---|---:|---|
| EStop_OK | Coil 000006 | 5 | Read E-stop state |
| Cmd_Word | Holding register 400001 | 0 | Write a test command |
| Status_Word | Holding register 400002 | 1 | Read the echoed status |
| Step_Mirror | Holding register 400031 | 30 | Later state monitoring |

### E1. Run a Python round-trip test

Save this as lab1_modbus_test.py. Replace the PLC address only if the instructor assigned another address.

~~~python
from pymodbus.client import ModbusTcpClient
import time

PLC_IP = "192.168.10.10"
client = ModbusTcpClient(PLC_IP, port=502)
if not client.connect():
    raise SystemExit("Could not reach the PLC: check Parts B and C")

print("Connected to", PLC_IP)
estop = client.read_coils(5, count=1)
print("EStop_OK:", estop.bits[0])
client.write_register(0, 7)
time.sleep(0.2)
status = client.read_holding_registers(1, count=1)
print("Status_Word (echo):", status.registers[0])
client.write_register(0, 0)
client.close()
~~~

Run:

~~~text
python lab1_modbus_test.py
~~~

With the E-stop released, expected output includes EStop_OK: True and Status_Word (echo): 7. Press the E-stop and repeat; the coil should report False.

### E2. Demonstrate the addressing trap

Change the status read to protocol address 2 and run the script. The requested register is outside the mapping, so the PLC should return a Modbus exception or error result. Record the error, then restore address 1.

**Checkpoint E:** Python can read the E-stop coil, write a command value, read the echoed status, and explain the one-address offset.

## Part F: Polling and Multiple Clients

Save a second script as lab1_monitor.py and run it in a separate Command Prompt:

~~~python
import time
from pymodbus.client import ModbusTcpClient

PLC_IP = "192.168.10.10"
REGS = {"Cmd_Word": 0, "Status_Word": 1, "Step_Mirror": 30}
client = ModbusTcpClient(PLC_IP, port=502)
if not client.connect():
    raise SystemExit("Could not reach the PLC")

try:
    while True:
        values = []
        for name, address in REGS.items():
            result = client.read_holding_registers(address, count=1)
            value = "ERR" if result.isError() else result.registers[0]
            values.append(f"{name}={value}")
        result = client.read_coils(5, count=1)
        value = "ERR" if result.isError() else result.bits[0]
        values.append(f"EStop_OK={value}")
        print("  ".join(values))
        time.sleep(0.5)
except KeyboardInterrupt:
    client.close()
~~~

While the monitor is running, execute the test script from a second terminal. Confirm that both clients communicate with the PLC and that the monitor observes the command/status transition.

## Part G: Inspect the Modbus Exchange

Use Wireshark on the cell Ethernet adapter to capture the TCP conversation with the PLC on port 502. Apply this filter:

~~~text
tcp.port == 502
~~~

Identify one read request, its response, transaction identifier, function code, and protocol address. Explain why the server sends responses only after a client request and why a value shorter than the polling interval can be missed.

## Troubleshooting

| Symptom | First checks |
|---|---|
| PLC power indicator is off | Measure at PLC terminals; check polarity and fuse. |
| E-stop input never changes | Check input common, NC contact continuity, and wiring. |
| ping times out | Check adapter, static address, PLC address, cable, and link lights. |
| CCW cannot find the PLC | Browse the Ethernet driver rather than the USB driver. |
| Python cannot connect but ping works | Confirm PLC mode and downloaded Modbus mapping. |
| A register read fails | Check the zero-based protocol address and mapping. |
| Python raises TypeError | Run pip show pymodbus and use 3.6 or newer. |

## Required Deliverables

- Power, polarity, continuity, and E-stop checklist.
- Annotated network diagram and final static IP table.
- CCW project/configuration evidence showing an Ethernet connection.
- I/O and Modbus map with documentation and Python addresses.
- Terminal capture showing the Python round trip and E-stop state change.
- Wireshark capture or annotated packet screenshots.
- Troubleshooting note for the intentionally induced addressing error.
- Short reflection on how the PLC, bridge scripts, and device protocols interact.

## Checkpoint Summary

| Checkpoint | Evidence |
|---|---|
| A | Verified 24 VDC distribution and E-stop behavior |
| B | Isolated switch, labeled cables, and compatible static addresses |
| C | CCW project built and downloaded over Ethernet |
| D | Running temporary echo program and live E-stop variable |
| E | Python read/write round trip and address-offset exercise |
| F | Two simultaneous Modbus clients with continuous polling |
| G | Wireshark evidence and request/response explanation |

## Looking Ahead

Delete the temporary echo program before beginning Lab 3. The next automation labs will build on this controller, fixed I/O allocation, static network, and command/status handshake as robots, sensors, conveyors, HMI/SCADA, and digital-twin services are added to the cell.
