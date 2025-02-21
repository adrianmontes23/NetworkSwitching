import os
import sys

argument = sys.argv[1]

if argument.lower() == "wifi":
    os.system("netsh interface set interface Ethernet disable")
elif argument.lower() == "eth":
    os.system("netsh interface set interface Ethernet enable")
else:
    print("Invalid argument")
    print("Please use 'wifi' or 'eth' as the argument")

