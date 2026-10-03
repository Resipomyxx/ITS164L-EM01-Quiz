"""Simple Cisco network inventory tool."""


devices = [
    {
        "hostname": "CORE-RTR-01",
        "management_ip": "192.168.10.1",
        "device_type": "Cisco ISR 4331 Router",
        "location": "Main Office - Server Room",
        "status": "Up",
    },
    {
        "hostname": "DIST-SW-01",
        "management_ip": "192.168.10.10",
        "device_type": "Cisco Catalyst 9300 Switch",
        "location": "Main Office - Network Room",
        "status": "Up",
    },
    {
        "hostname": "BRANCH-RTR-01",
        "management_ip": "192.168.20.1",
        "device_type": "Cisco ISR 1111 Router",
        "location": "Branch Office - Comms Cabinet",
        "status": "Down",
    },
]


def display_devices(device_list):
    """Display the supplied devices in a readable format."""
    for device in device_list:
        print(f"Hostname       : {device['hostname']}")
        print(f"Management IP  : {device['management_ip']}")
        print(f"Device Type    : {device['device_type']}")
        print(f"Location       : {device['location']}")
        print(f"Status         : {device['status']}")
        print("-" * 50)


def operational_devices(device_list):
    """Return devices that are currently operational."""
    return [device for device in device_list if device["status"].lower() == "up"]


def main():
    """Display the complete inventory and operational device summary."""
    print("=" * 50)
    print("CISCO NETWORK INVENTORY")
    print("=" * 50)

    print("\nALL DEVICES")
    print("-" * 50)
    display_devices(devices)

    up_devices = operational_devices(devices)
    print("\nOPERATIONAL DEVICES (STATUS: UP)")
    print("-" * 50)
    display_devices(up_devices)

    print(f"\nOperational device count: {len(up_devices)} of {len(devices)}")


if __name__ == "__main__":
    main()
