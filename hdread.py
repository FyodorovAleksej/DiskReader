import os
import subprocess
import re
#call linux shell command (lspci) with output in file "/log.txt" for getting all PCI devices
subprocess.call("sudo hdparm -I /dev/sda > " + os.getcwd() + "/log.txt", shell=True)
#open temp file "/log.txt"
logfile = open(os.getcwd() + "/log.txt")
#create keys of information about hd disk
keys = ["Model Number", "Firmware Revision", "Serial Number", "Transport", "DMA", "PIO"]
#create dictianory with information about parameteres of hd disk
dictianory = {k: None for k in keys}
for i in logfile:
    for j in keys:
        #if find substring (key + ":") in current line
        if ((j + ":") in i):
            #getting substring after the key of information
            temp = i.split(j)[1]
            #ignore ":" in substring
            if (":" in temp):
                temp = temp.split(":")[1]
            #ignore "\t" in substring
            if ("\t" in temp):
                temp = temp.split("\t")[1]
            #ignore "\n" in current line
            if ("\n" in temp):
                temp = temp.split("\n")[0]
            #ignore spaces before information
            while (temp[0] == ' '):
                temp = temp[1:]
            #ignore spaces after information
            while (temp[-1] == ' '):
                temp = temp[:-2]
            #saving information in dictianory
            dictianory[j] = temp
#closing file
logfile.close()
subprocess.call("df -hm | grep /dev/sda > " + os.getcwd() + "/log.txt", shell=True)
logfile = open(os.getcwd() + "/log.txt")
result = re.split(r" +", logfile.read())
memdict = {"all": None, "free": None, "used": None}
memdict["all"] = result[1]
memdict["used"] = result[2]
memdict["free"] = result[3]
tempDict = {"Memory": memdict}
dictianory.update(tempDict)
#print result dictianory
for k in dictianory.keys():
    print(k + " : ")
    print(dictianory[k])
#remove temp file "/log.txt"
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.getcwd() + "/log.txt")
os.remove(path)

