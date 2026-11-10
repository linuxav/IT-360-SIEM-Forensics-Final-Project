import re
import csv
import sys
from config import *
import requests
import json

def APIConfig():
    config = load_config()
    ai_key = config["AIAPI_KEY"]
    return ai_key

def runMode(modeInput):
    if modeInput.lower() == "-local":
        return "local"
    elif modeInput.lower() == "-ai":
        return "ai"
    else:
        return "error"

def localSearch(Filepath):

    with open(Filepath,"r") as file: #read txt file and store its contents
        text = file.read()

    #search file contents for IPV4 Addresses, remove duplicate entries, output as a list 
    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b" 
    matches = set(re.findall(pattern, text)) 

    return matches

def AISearch(Filepath, ai_key):
     
     with open(Filepath,"r") as file: #read txt file and store its contents
        text = file.read()

        url = 'http://sushi.it.ilstu.edu:8080/api/chat/completions'
        headers = {
        'Authorization': f'Bearer {ai_key}',
        'Content-Type': 'application/json'
        }
    
        data = {
        "model": "translategemma:latest",
        "messages": [
            {
                "role": "user",
                "content": f"Analyze this text and return only a list of ip addresses found within separated by commas:\n{text}"
            }
            ]
        }

        response = requests.post(url, headers=headers, json=data)
    
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code} - {response.text}"



def csvout(input):
    #output to .csv file, creating the file if it does not exist
    try:
        with open("IPFilterOutput.csv","x") as output:
            writer = csv.writer(output)
            writer.writerow(input)
    except FileExistsError:
        with open("IPFilterOutput.csv","w") as output:
            writer = csv.writer(output)
            writer.writerow(input)

def Main(arguments):
    ai_key = APIConfig()
    searchMode = None
    IPList = None
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
        IPList = response.split(", ")
    else:
        if searchMode != None:
            print("Error: unkown search mode")

    if IPList != None:
        csvout(IPList)



Main(sys.argv)