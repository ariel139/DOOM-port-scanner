import socket 
from IPy import IP


print("""
You are using the DOOM Port scanner.

This tool is for educational purpose ONLY!!!!

1. You can change the range of the ports you want to scan.
2. You can change the speedof the scan
3. you can scan a list of targets by using ', ' after each target
4. You can scan both URL links and both IP's 


""")
# ip adresess
targets = input("enter targets or URL's ")

# min range of ports 
min_port = int(input("enter min number of ports "))

# max range of ports 
max_port = int(input("enter max number of ports "))
try:
    speed = int(input("Enter the speed you want to scan in (try using a Irrational number, deffult is 0.1) "))
except:
    speed = 0.1    




def multi_targets(ip):
    converted_ip = check_ip(ip)
    # using loop to scan the port
    print(f'scaning port for {ip}')
    for port in range(min_port,max_port +1):
        scan_port(converted_ip,port)
                
# check if the ip is URL link or ip
def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        socket.gethostbyname(ip)    
        return ip

def get_data_from_port(soc):
    return soc.recv(1024)
# scan port function
def scan_port(ip, port):
    try:
        sc = socket.socket()
        sc.settimeout(speed)
        sc.connect((ip, port))
        try:
            data = get_data_from_port(sc)
            
            print(f'[+] port {port} is on and recived data is: {data}')
        except:
            print(f'[+] {port} port is open')    

    except:
        print('scaning ports...')
# converted ip adress to link and int ip

if ', ' in targets:
    for ip_add in targets.split(','):
        multi_targets(ip_add.strip(' '))
else:
    multi_targets(targets)
