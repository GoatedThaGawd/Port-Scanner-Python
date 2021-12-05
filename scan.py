import socket
import threading
import concurrent.futures
from colorama import *
init()
 
print_lock = threading.Lock()
 
print("will close once it is done scanning")
print("scans from port 1 to 65,000")
print("")
print("")
ip = input("Enter IP to scan: ")
 
def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip,port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " Opened")
    except:
        pass
 
with concurrent.futures.ThreadPoolExecutor(max_workers=450) as executor:
    for port in range(65000):
        executor.submit(scan, ip, port + 1)
