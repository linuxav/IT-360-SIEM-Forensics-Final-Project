import requests
from core import load_config

def check_ip_test():
    url = 'https://httpbin.org/get'
    config = load_config()
    api_key = config["ABUSEIPDB_KEY"]

    headers = {
        'Key': api_key,
        'Accept': 'application/json',
        'User-Agent': 'ThreatFlare-SIEM-Forensics-Tool/1.0'
    }

    target_ip = input("Target IP: ")
    
    querystring = {
        'ipAddress': target_ip,
        'maxAgeInDays': '90',
        'verbose': True
    }

    try:
        # Make the request to httpbin
        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code == 200:
            print("--- HTTPBIN TEST SUCCESSFUL ---")
            response_data = response.json()
            
            # Httpbin returns a dictionary showing what headers and arguments it saw
            print("\nHeaders received by server:")
            print(response_data.get('headers'))
            
            print("\nQuery parameters received by server:")
            print(response_data.get('args'))
            
        else:
            print(f"Failed to connect to httpbin. Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred during testing: {e}")
