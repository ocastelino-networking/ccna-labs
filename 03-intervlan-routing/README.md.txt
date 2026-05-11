# Inter-VLAN Routing (Router-on-a-Stick)

## Objective
Enable communication between multiple VLANs using a single router interface.

---

## Scenario
- VLAN 10 = Sales
- VLAN 20 = HR
- VLAN 30 = IT

Each VLAN is isolated at Layer 2, but must communicate through a router.

---

## Key Concept
Router-on-a-Stick uses:
- One physical router interface
- Multiple logical subinterfaces
- 802.1Q tagging

---

## Skills Learned
- Subinterface configuration
- VLAN tagging (802.1Q)
- Inter-VLAN communication

---

## Outcome
Devices in different VLANs can communicate via routing.