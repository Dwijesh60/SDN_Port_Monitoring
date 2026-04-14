# SDN Simulation Project: The Orange Problem
**Individual Project | Mininet & POX Controller**

##  Problem Overview
The "Orange Problem" is a Software Defined Networking (SDN) challenge designed to demonstrate the separation of the control plane and data plane. The goal is to create a smart controller that manages a network topology, implements a security "firewall" to isolate specific traffic, and monitors the physical state of network ports.

### Objectives:
* **Dynamic Learning:** Implement an L2 Learning Switch that populates flow tables based on source MAC addresses.
* **Security Filtering:** Create an explicit flow rule (The Orange Filter) to block all traffic from a specific untrusted host (**Host 3**).
* **Network Monitoring:** Detect and log port status changes (Up/Down events) in real-time.

---

##  System Architecture
* **Controller:** POX (Python-based OpenFlow Controller)
* **Emulator:** Mininet
* **Protocol:** OpenFlow 1.0
* **Topology:** Single Open vSwitch ($S1$) connected to three Hosts ($H1, H2, H3$).

---

##  Setup & Execution

### 1. Prerequisites
Ensure your environment (Ubuntu/WSL2) has Mininet and POX installed:
