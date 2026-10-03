import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ROUTER_IP = "10.10.20.48"
USERNAME = "developer"
PASSWORD = "C1sco12345"

def configure_loopback():
    url = f"https://{ROUTER_IP}:443/restconf/data/ietf-interfaces:interfaces/interface=Loopback100"
    
    headers = {
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json"
    }
    
    payload = {
        "ietf-interfaces:interface": {
            "name": "Loopback100",
            "description": "Configured via RESTCONF API",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.16.100.1",
                        "netmask": "255.255.255.255"
                    }
                ]
            }
        }
    }

    try:
        print(f"Sending configuration for Loopback100 to {ROUTER_IP}...")
        
        response = requests.put(
            url,
            auth=(USERNAME, PASSWORD),
            headers=headers,
            data=json.dumps(payload),
            verify=False,
            timeout=10
        )
        
        print(f"HTTP Status Code: {response.status_code}")
        if response.status_code in [201, 204]:
            print("Status: Configuration successful!\n")
        else:
            print(f"Status: Configuration failed. Response: {response.text}\n")
            return

        print("Retrieving and verifying Loopback100 configuration...")
        verify_response = requests.get(
            url,
            auth=(USERNAME, PASSWORD),
            headers={"Accept": "application/yang-data+json"},
            verify=False,
            timeout=10
        )
        
        if verify_response.status_code == 200:
            print("Verification successful! Retrieved payload:")
            print(json.dumps(verify_response.json(), indent=2))
        else:
            print(f"Verification failed with status code {verify_response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"[Error] Connection failed: {e}")

if __name__ == "__main__":
    configure_loopback()