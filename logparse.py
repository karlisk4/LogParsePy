import glob
import os.path
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
drvApp = []
drvReg = []
drvOfnc = []
drvName = ""
fileName =  glob.glob('server_*.log')
#print (fileName)
f = open(fileName[0], encoding="utf8")
for line in f:
    
    if "is running" in line:
        drvCheck = re.search('\((.*)\)', line)
        drvName = str(drvCheck.group(1))
        #print(drvName.group(1))
        if drvName not in drvApp:
            drvApp.append(drvName)
            #print(drvName)
f.close()
f = open('reg.txt', encoding="utf8")
for line in f:
    if '[' in line:
        linef= line.replace('\n', '')
        drvReg.append(linef)
        #print(line)
#print(drvReg)
for x in drvApp:
    if not any(x in s for s in drvReg):
        drvOfnc.append(x)
print(drvOfnc)