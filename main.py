import os
import sys

argument = sys.argv[1]

if argument.lower() == "wifi":
    print("Wifi")
    os.system("netsh interface set interface Ethernet disable")
elif argument.lower() == "eth":
    print("Ethernet")
    os.system("netsh interface set interface Ethernet enable")
else:
    print("Invalid argument")
    print("Please use 'wifi' or 'eth' as the argument")

