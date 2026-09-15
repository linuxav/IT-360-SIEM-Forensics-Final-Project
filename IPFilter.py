import re
import csv
import sys

def filterip(Filepath):

    with open(Filepath,"r") as file: #read txt file and store its contents
        text = file.read()

    #search file contents for IPV4 Addresses, remove duplicate entries, output as a list 
    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b" 
    matches = set(re.findall(pattern, text)) 

    return matches


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


def Main(Filepath):
    csvout(filterip(Filepath))

Main(sys.argv[(len(sys.argv)-1)])
