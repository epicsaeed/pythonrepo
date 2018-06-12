from socket import *
import sys,time
from time import gmtime, strftime

#specifying port limit
host = ''
max_port = 5000
min_port = 1

#scans target
def scan_host(host,port,r_code=1):
    try:
        s = socket(AF_INET,SOCK_STREAM)

        code = s.connect_ex((host,port))
        
        if code == 0:
            r_code = code
        s.close()
    except Exception as e:
        pass

    return r_code

#asking user for url/IP
try:
    host = input("[*] Enter Targert Host Address: ")
except KeyboardInterrupt:
    print("\n\n[*] User Requested An Interrupt.\n[*] Shutting down....")

hostip = gethostbyname(host)

print("[*] Scanning Started at ", strftime("%H:%M:%S", gmtime()),"\n[*] Scanning host: ",hostip)

for port in range(min_port,max_port):
    try:
        response = scan_host(host,port)
        if response == 0:
            print("[*] Port ",port,": Open")
    except Exception as e:
        pass

print("[*] Scanning Ended at ", strftime("%H:%M:%S", gmtime()))