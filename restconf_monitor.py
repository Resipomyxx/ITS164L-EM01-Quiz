import requests
import urllib3

# Disable insecure request warnings for sandbox self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- REPLACE THESE VARIABLES ONCE SANDBOX IS ACTIVE ---
ROUTER_IP = "10.10.20.48"
USERNAME = "developer"  
PASSWORD = "C1sco12345" 
# ------------------------------------------------------

def get_interfaces():
    # RESTCONF resource URL for interfaces
    url = f"https://{ROUTER_IP}:443/restconf/data/ietf-interfaces:interfaces"
    
    headers = {
        "Accept": "application/yang-data+json"
    }

    try:
        print(f"Connecting to {ROUTER_IP}...")
        # Send HTTP GET request using RESTCONF
        response = requests.get(
            url,
            auth=(USERNAME, PASSWORD),
            headers=headers,
            verify=False,
            timeout=10
        )
        
        # Display the HTTP status code
        print(f"HTTP Status Code: {response.status_code}\n")
        
        # Handle unsuccessful HTTP responses
        response.raise_for_status() 

        # Retrieve and parse interface information
        data = response.json()
        interfaces = data["ietf-interfaces:interfaces"]["interface"]

        # Display interface name and enabled status
        print(f"{'Interface Name':<25} | {'Enabled Status'}")
        print("-" * 45)
        for interface in interfaces:
            name = interface.get("name", "N/A")
            enabled = interface.get("enabled", "N/A")
            print(f"{name:<25} | {enabled}")

    except requests.exceptions.RequestException as e:
        # Handle a failed connection
        print("\n[Error] Connection Failed. Ensure you are connected to the DevNet VPN and the IP is correct.")
        print(f"Details: {e}")

if __name__ == "__main__":
    get_interfaces()