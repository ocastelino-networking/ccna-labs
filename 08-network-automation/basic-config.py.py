# Simple network automation simulation

routers = ["Router1", "Router2", "Router3"]

for router in routers:
    print(f"Connecting to {router}...")
    print("Configuring interface g0/0")
    print("Assigning IP address 192.168.1.1")
    print("Interface enabled")
    print(f"{router} configuration complete\n")
