from threatflare.core.IPFilter import *
import re
import csv
import sys
from threatflare.core.config import *
import requests
import json
from threatflare.modules.abuseipdb import *

def Main(arguments):
    config = load_config()
    ai_key = config["AIAPI_KEY"]
    searchMode = None
    IPList = None
    maliciousCount = 0
    ErrorCount = 0
    if len(arguments) < 2:
        print("Error: no file selected")
    elif len(arguments) > 3:
        print("Error: unknown arguments")
    elif len(arguments) == 2:
        searchMode = "local"
    elif len(arguments) == 3:
        searchMode = runMode(arguments[2])


    if searchMode == "error":
        print("Error: unkown search mode")
    elif searchMode == "local":
        IPList = localSearch(arguments[1])
    elif searchMode == "ai":
        response = str((AISearch(arguments[1], ai_key))).replace("\n", "")
        IPList = set(response.split(", "))
    else:
        if searchMode != None:
            print("Error: unkown search mode")

    if IPList != None:
        tempReport = ""
        ipCount = 0
        for item in IPList:
            ipCount += 1
            report, control = ipdbCheck(item)
            if control == 1:
                maliciousCount += 1
                tempReport = (f"{tempReport}" + f"{report}\n\n")
            elif control == 2:
                tempReport = (f"{tempReport}" + f"{report}\n\n")
            elif control == 0:
                ErrorCount += 1
                tempReport = (f"{tempReport}" + f"Error checking IP {item}: {report}\n\n")
        print(f"Scanned {ipCount} IP addresses: \nDetected {maliciousCount} malicious IPs, {ErrorCount} Errors")
        FinalReport = f"Scanned {ipCount} IP addresses: \nDetected {maliciousCount} malicious IPs, {ErrorCount} Errors\n\n{tempReport}"
        try:
            with open("ReportOutput.txt","x") as output:
                output.write(FinalReport)
        except FileExistsError:
            with open("IPFilterOutput.csv","w") as output:
                output.write(FinalReport)
    else:
        print("No IP Addresses found. No report will be generated.")





Main(sys.argv)