import glob
import os.path
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
drvApp = []
drvReg = []
drvOfnc = []
drvName = ""
session = ""

def logParse():
    fileName =  glob.glob('output_*.log')
    f = open(fileName[0], encoding="utf8")
    for line in f:
        if "Name: Practice" in line:
            session = "P"
        elif "Name: Qualifying 1" in line:
            session = "Q1"
        elif "Name: Qualifying 2" in line:
            session = "Q2"
        elif "Name: Qualify" in line:
            session = "Q"
        elif "Name: Warm Up" in line:
            session = "W"
        elif "Name: Race" in line:
            session = "R"
        elif "is running" in line:
            drvCheck = re.search('\((.*)\)', line)
            drvName = str(drvCheck.group(1))
            #print(drvName.group(1))
            if drvName not in drvApp:
                drvApp.append(drvName)
                #print(drvName)
        elif "TROUT_DRS: Penalty" in line:
            drvCheck = re.search('\((.*)\)', line)
            drvName = str(drvCheck.group(1))
            penCheck = re.search('\,(.*)\"', line)
            penName = str(penCheck.group(1))
            drvOfnc.append(drvName + penName)
            print(drvName + " " + penName + " " + session)
    f.close()

def regParse():
    f = open('reg.txt', encoding="utf8")
    for line in f:
        if '[' in line:
            linef= line.replace('\n', '')
            drvReg.append(linef)
            #print(line)
    #print(drvReg)
    f.close()
def runParse():
    for x in drvApp:
        if not any(x in s for s in drvReg):
            drvOfnc.append(x + "DRS not working")
            print(x + "DRS not working")
    #print(drvOfnc)


regParse()
runParse()
logParse()