
import socket 
import termcolor

# Function to display ASCII banner
def display_banner():
    banner = """
 ######                      ######                                    
 #     #  ####  #####  ##### #     # #####   ####  #####  ######   #   
 #     # #    # #    #   #   #     # #    # #    # #    # #        #   
 ######  #    # #    #   #   ######  #    # #    # #####  #####  ##### 
 #       #    # #####    #   #       #####  #    # #    # #        #   
 #       #    # #   #    #   #       #   #  #    # #    # #        #   
 #        ####  #    #   #   #       #    #  ####  #####  ######           by  niharx7    
                                                                       
    """
    print(termcolor.colored(banner, 'blue'))

def scan(target , ports):
    display_banner()
    print('\n' + '-'*40)
    print(f'Starting scan for {target}...')
    open_ports = []
    for port in range(1, ports + 1):
        banner = scan_port(target, port)
        if banner:
            open_ports.append((port, banner))
    print(f'\nScan complete for {target}.')
    if open_ports:
        print('\nOpen ports:')
        for port, banner in open_ports:
            print(termcolor.colored(f"    [+] Port {port}: {banner}", 'green'))
        print(f"\nTotal open ports found: {len(open_ports)}")
    else:
        print(termcolor.colored("\nNo open ports found.", 'red'))
    print('-'*40)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        sock.settimeout(2)
        sock.send(b"Hello\r\n")
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except Exception as e:
        return None

targets = input("[*] Enter Targets To Scan: ")
ports = int(input("[*] Enter No Of Ports To Scan: "))
if ',' in targets:
    print(termcolor.colored("[+] Scanning Multiple Targets", 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets, ports)
