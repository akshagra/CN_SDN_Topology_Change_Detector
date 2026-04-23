# Topology Change Detector using SDN

## Author

Name: Akshansh Agrawal

SRN: PES2UG24CS045

Course: Computer Networks

Controller: POX (OpenFlow 1.0)

Emulator: Mininet

---

## Project Overview

This project implements a Topology Change Detection system using Software Defined Networking (SDN).
The controller continuously monitors the network and detects changes such as switch connections, link failures, and topology updates in real time.

All detected changes are displayed on the controller and stored in a log file for analysis.

---

## Objective

* Detect topology changes dynamically
* Monitor switch and link events
* Maintain an updated topology map
* Log all changes with timestamps

---

## Technologies Used

* POX Controller – SDN controller for event handling
* Mininet – Network emulator
* OpenFlow Protocol – Communication between switches and controller
* Python – Implementation language

---

## System Architecture

```
Mininet (Network Emulator)
        |
        v
OpenFlow Switches
        |
        v
POX Controller
        |
        v
Topology Detector Module
        |
        v
Logs + Output
```

---

## Working

1. Mininet creates a virtual network
2. Switches connect to the controller
3. Controller listens for events:

   * ConnectionUp → switch added
   * ConnectionDown → switch removed
   * LinkEvent → link added/removed
4. Topology is updated dynamically
5. Changes are displayed and logged

---

## Setup Instructions

### Install Dependencies

```
sudo apt update
sudo apt install mininet -y
git clone https://github.com/noxrepo/pox.git ~/pox
```

### Add Controller File

```
cp topology_detector_pox.py ~/pox/ext/
```

---

## How to Run

### Terminal 1 (Controller)

```
cd ~/pox
./pox.py log.level --ERROR openflow.discovery topology_detector_pox
```

### Terminal 2 (Mininet)

```
sudo mn --topo tree,depth=2,fanout=2 --controller=remote
```

---

## Testing Commands (Mininet CLI)

```
pingall
link s1 s2 down
link s1 s2 up
switch s1 stop
switch s1 start
```

---

## Expected Output

* Detection of switch join/leave events
* Detection of link addition/removal
* Logs printed in controller terminal
* Logs saved in topology_log.txt

Example:

```
Switch ADDED: 1
Switch ADDED: 2
Link ADDED: (1,2)
Link REMOVED: (1,2)
```

---

## Applications

* Network monitoring
* Fault detection
* Data center management
* SDN-based automation

---

## Limitations

* POX has limited support for newer Python versions
* No graphical visualization
* Suitable for small-scale simulation

---

## Future Improvements

* Add topology visualization using NetworkX
* Build a web dashboard
* Use advanced SDN controllers like Ryu or ONOS

---

## Learning Outcomes

* Understanding SDN architecture
* Event-driven programming
* OpenFlow protocol usage
* Real-time network monitoring

---

## References

* https://mininet.org
* https://github.com/noxrepo/pox
* OpenFlow Documentation
