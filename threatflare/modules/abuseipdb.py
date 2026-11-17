# AbuseIPDB API implementation

import os
import sys
import requests
from threatflare.core.config import load_config

def ipdbCheck(target_ip):
    url = 'https://api.abuseipdb.com/api/v2/check'
    control = 0
    
    config = load_config()
    api_key = config["ABUSEIPDB_KEY"]
    
    headers = {
        'key': api_key,
        'Accept': 'application/json'
    }

    # Optional filters
    querystring = {
        'ipAddress': target_ip,
        'maxAgeInDays': '90',
        'verbose': True
    }

    # 3. Make a GET request to the API
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        
        if response.status_code == 200:
            ip_data = response.json()['data']
            
            # 4. Read the target metrics
            score = ip_data['abuseConfidenceScore']
            total_reports = ip_data['totalReports']
            country = ip_data.get('countryName', 'Unknown')
            
            ipOutput = (f"IP Evaluated: {target_ip}")
            scoreOutput = (f"Abuse Confidence Score: {score}%")
            reportCount = (f"Total Times Reported: {total_reports}")
            countryOutput = (f"Country of Origin: {country}")
            
            if score > 50:
                rating = ("This IP has a high confidence score for malicious activity!")
                control = 1
            else:
                rating =("This IP appears relatively clean.")
                control = 2

            finalOutput = (f"{ipOutput}\n" + f"{scoreOutput}\n" + f"{reportCount}\n" + f"{countryOutput}\n" + f"{rating}\n")
            return finalOutput, control
                
        else:
            finalOutput = (f"Failed to check IP. Status Code: {response.status_code}")
            return finalOutput, control

    except Exception as e:
        finalOutput = (f"An error occurred: {e}")
        return finalOutput, control