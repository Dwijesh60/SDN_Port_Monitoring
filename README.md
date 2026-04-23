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
   ```
2. **Launch the Mininet Topology:**
   ```bash
   sudo mn --topo single,3 --mac --controller remote,ip=127.0.0.1,port=6633
   ```

---

## 🧪 Testing & Validation

### Scenario 1: Trusted Communication (Normal)
* **Command:** `h1 ping -c 3 h2`
* **Result:** 0% packet loss. 
* **Observation:** The controller installs a flow rule in the switch, and subsequent packets bypass the controller for line-rate forwarding.

### Scenario 2: The Orange Alert (Blocked)
* **Command:** `h3 ping -c 3 h1`
* **Result:** 100% packet loss.
* **Observation:** The controller detects the restricted MAC address and triggers an `ORANGE ALERT`, dropping the packet.

### Scenario 3: Port Monitoring (Failure)
* **Command:** `link s1 h1 down`
* **Observation:** The POX console logs: `--- PORT MONITOR: Port 1 on Switch 1 is MODIFIED/LINK TOGGLED ---`.
* **Validation:** Demonstrates real-time detection of physical link failures.

---

## 📈 Performance Analysis
| Metric | Result | Analysis |
| :--- | :--- | :--- |
| **Throughput (iperf)** | [Your Value] Gbps | Demonstrates hardware-level speed after flow installation. |
| **Latency (First Ping)** | ~3-5ms | Represents the Control Plane processing delay. |
| **Latency (Subsequent)** | ~0.08ms | Represents the Data Plane forwarding speed. |


<img width="1919" height="652" alt="Screenshot 2026-04-14 160532" src="https://github.com/user-attachments/assets/26c0347b-03d4-4e61-99c0-cd292d32e5b9" />

<img width="1919" height="1079" alt="Screenshot 2026-04-14 161334" src="https://github.com/user-attachments/assets/88e25e59-083b-42d3-818c-752eaf7c9fc4" />

<img width="1919" height="1079" alt="Screenshot 2026-04-14 161855" src="https://github.com/user-attachments/assets/082980b7-e132-4953-a11e-52618933cdb9" />

<img width="935" height="262" alt="Screenshot 2026-04-14 162214" src="https://github.com/user-attachments/assets/a78ebbb3-5eea-4073-b539-c26d8313c510" />

<img width="780" height="230" alt="Screenshot 2026-04-14 163842" src="https://github.com/user-attachments/assets/3a6a5716-fb52-4200-a8f5-18a70ef13889" />

<img width="1725" height="322" alt="Screenshot 2026-04-14 163433" src="https://github.com/user-attachments/assets/0e7d47ae-3860-4831-a2be-f852df3bbb27" />

<img width="780" height="230" alt="Screenshot 2026-04-14 163842" src="https://github.com/user-attachments/assets/e851bd18-96c3-4801-a452-66408e76e883" />



## 📚 References
* McKeown, N., et al. (2008). "OpenFlow: Enabling Innovation in Campus Networks."
* POX Controller Documentation: [noxrepo.github.io](https://noxrepo.github.io/pox-doc/html/)
```
