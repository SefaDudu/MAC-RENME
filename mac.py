import subprocess
import sys, os

def getMACAddr(command):
    runARP = subprocess.Popen(
        args=command,
        stdout=subprocess.PIPE,
        shell=True
    )
    
    return runARP.communicate()[0]

def pingIP():
    runPING = subprocess.Popen(
        args= "ping -n 1 " + sys.argv[1],
        stdout=subprocess.PIPE,
        shell=True
    )
    return runPING.communicate()[0]


pingIP()
getMAC = [getMACAddr("arp -a")]