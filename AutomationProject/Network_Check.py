import json
import subprocess
import platform

def ping_host(host):
    # Determine the ping argument based on the OS (-n on Windows, -c on Unix)
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    
    try:
        # Run ping command with a 3-second timeout
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=3
        )
        return result.returncode == 0
    except subprocess.SubprocessError:
        return False

def main():
    inventory_file = "inventory.json"
    output_file = "output.json"

    # Step 1: Read device information from inventory.json
    try:
        with open(inventory_file, "r") as f:
            devices = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading {inventory_file}: {e}")
        return

    results = []
    print("=" * 50)
    print("STARTING NETWORK STATUS CHECK")
    print("=" * 50)

    # Step 2: Check each device
    for device in devices:
        hostname = device.get("hostname", "Unknown")
        ip = device.get("ip_address", "")
        
        is_up = ping_host(ip)
        status = "UP" if is_up else "DOWN"

        device_result = {
            "hostname": hostname,
            "ip_address": ip,
            "device_type": device.get("device_type", "Unknown"),
            "status": status
        }
        results.append(device_result)

        # Step 3: Display results on screen
        print(f"Device: {hostname:<20} | IP: {ip:<15} | Status: {status}")

    # Step 4: Save results to output.json
    try:
        with open(output_file, "w") as f:
            json.dump(results, f, indent=4)
        print("\n" + "=" * 50)
        print(f"Results successfully saved to {output_file}")
        print("=" * 50)
    except IOError as e:
        print(f"Error saving results to {output_file}: {e}")

if __name__ == "__main__":
    main()