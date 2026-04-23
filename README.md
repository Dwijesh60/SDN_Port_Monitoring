# SDN Simulation Project: The Orange Problem & Port Monitoring
**Course Project | PES University** **Student:** Dwije (PES2UG24CS163)

## 🎯 Overview
This project implements a Software Defined Networking (SDN) solution using the **POX Controller** and **Mininet**. It demonstrates the dynamic management of network flows, security enforcement via traffic filtering, and real-time network health monitoring.

### Key Features:
1. **L2 Learning Switch:** Dynamically populates flow tables to enable efficient packet forwarding.
2. **Orange Filter (Security):** An explicit security policy that identifies and blocks all traffic from **Host 3** (MAC: `00:00:00:00:00:03`).
3. **Port Status Monitoring:** A real-time tool that detects and logs switch port events (Up/Down/Modified), satisfying the requirement for network observability.

---

## 🏗️ System Architecture
* **Control Plane:** POX Controller (Python-based)
* **Data Plane:** Mininet with Open vSwitch
* **Protocol:** OpenFlow 1.0
* **Topology:** Single Switch ($S1$) connected to three Hosts ($H1, H2, H3$).



---

## 🚀 Setup & Execution

### Prerequisites
Ensure your environment (WSL2/Ubuntu) has Mininet and the POX framework installed.

### Steps to Run:
1. **Start the POX Controller:**
   ```bash
   cd ~/pox
   python3 pox.py orange_pox


<img width="1919" height="652" alt="Screenshot 2026-04-14 160532" src="https://github.com/user-attachments/assets/2e46d955-552d-4da6-b579-a5c1bc5a8951" />
