# AbuseIPDB API implementation

import os
import sys
import requests
from core import load_config

def ipdbCheck():
    url = 'https://api.abuseipdb.com/api/v2/check'
    config = load_config()
    api_key = config["ABUSEIPDB_KEY"]
    out_file = config["LOG_FILE"] #TODO: implement file input and looping thru said file

    # IP Address being investigated
    target_ip = input("Target IP: ")

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
        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code == 200:
            ip_data = response.json()['data']
            
            # 4. Read the target metrics
            score = ip_data['abuseConfidenceScore']
            total_reports = ip_data['totalReports']
            country = ip_data.get('countryName', 'Unknown')
            
            print(f"IP Evaluated: {target_ip}")
            print(f"Abuse Confidence Score: {score}%")
            print(f"Total Times Reported: {total_reports}")
            print(f"Country of Origin: {country}")
            
            if score > 50:
                print("This IP has a high confidence score for malicious activity!")
            else:
                print("This IP appears relatively clean.")
                
        else:
            print(f"Failed to check IP. Status Code: {response.status_code}")
            print(response.json())

    except Exception as e:
        print(f"An error occurred: {e}")