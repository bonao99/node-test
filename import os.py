import os

hostnames = [
    "192.168.50.192",
    "192.168.50.199",
    "192.168.50.200",
    "192.168.50.201",

]

for hostname in hostnames:
    response = os.system('ping -c 1 ' + hostname)
    if response == 0:
        print(hostname, 'is up')
    else:
        print(hostname, 'is down')