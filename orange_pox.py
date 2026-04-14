from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.addresses import EthAddr

log = core.getLogger()

class OrangeController (object):
    def __init__ (self, connection):
        self.connection = connection
        connection.addListeners(self)
        self.mac_to_port = {}

    def _handle_PortStatus (self, event):
        """
        Logic for Criteria 3 & Port Monitoring Tool (Image 13)
        Detects when a link is physically pulled or a port is disabled.
        """
        if event.added:
            action = "ADDED"
        elif event.deleted:
            action = "DELETED"
        elif event.modified:
            action = "MODIFIED/LINK TOGGLED"
        else:
            action = "UNKNOWN"
            
        log.info("--- PORT MONITOR: Port %s on Switch %s is %s ---", 
                 event.port, event.dpid, action)

    def _handle_PacketIn (self, event):
        packet = event.parse()
        if not packet: return

        # 1. LEARN source MAC
        self.mac_to_port[packet.src] = event.port

        # 2. THE ORANGE FILTER (Scenario: Blocked)
        if packet.src == EthAddr("00:00:00:00:00:03"):
            log.info("--- ORANGE ALERT: Security Policy Blocking Host 3 (%s) ---", packet.src)
            return 

        # 3. FORWARDING LOGIC (Scenario: Allowed)
        if packet.dst in self.mac_to_port:
            port = self.mac_to_port[packet.dst]
            log.info("Normal Flow: %s -> Output Port %s", packet.dst, port)
            
            msg = of.ofp_flow_mod()
            msg.match = of.ofp_match.from_packet(packet)
            msg.actions.append(of.ofp_action_output(port = port))
            self.connection.send(msg)
        else:
            # Flood if destination is unknown
            msg = of.ofp_packet_out()
            msg.data = event.ofp
            msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
            self.connection.send(msg)

def launch ():
    def start_switch (event):
        log.info("Switch %s has connected. Monitoring Active.", event.dpid)
        OrangeController(event.connection)
    
    core.openflow.addListenerByName("ConnectionUp", start_switch)
