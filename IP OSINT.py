import os
import sys
import time
import requests
from colorama import Fore, Style, init

# Colorama ko initialize kar rahe hain (Windows/Linux dono ke liye)
init(autoreset=True)

def clear_screen():
    """Terminal screen ko clear karne ke liye"""
    os.system('cls' if os.name == 'nt' else 'clear')

def hacker_print(text, delay=0.03, color=Fore.GREEN):
    """Hacker style me dheere-dheere type hone wala effect"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_banner():
    """Cool Hacker Style Banner"""
    clear_screen()
    banner = f"""
{Fore.GREEN}================================================================
     _    ____    _____ ____    _    ____ _  _______ ____  
    | |  |  _ \  |_   _|  _ \  / \  / ___| |/ / ____|  _ \ 
    | |  | |_) |   | | | |_) |/ _ \| |   | ' /|  _| | |_) |
    | |__|  __/    | | |  _ < / ___ \ |___| . \| |___|  _ < 
    |____|_|       |_| |_| \_/_/   \_\____|_|\_\_____|_| \_\\
                                                   
               >> [ CODED BY: SURAZZ__69 ] <<
               >> [ INSTA: @SURAZZ__69 ]            <<
================================================================
    """
    print(banner)

def track_ip(ip_address):
    """IP Address track karne ka main function"""
    hacker_print(f"\n[*] Connecting to secure database...", 0.04, Fore.YELLOW)
    time.sleep(1)
    
    # API Endpoint (Agar IP khali chhodoge toh ye aapki khud ki public IP track karega)
    url = f"http://ip-api.com/json/{ip_address}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'success':
            hacker_print("\n[+] BYPASSING FIREWALL... ACCESS GRANTED!", 0.02, Fore.GREEN)
            time.sleep(0.5)
            hacker_print("=========================================", 0.01, Fore.GREEN)
            hacker_print(f" TARGET IP    : {data.get('query')}", 0.03)
            hacker_print(f" COUNTRY      : {data.get('country')} ({data.get('countryCode')})", 0.03)
            hacker_print(f" REGION/STATE : {data.get('regionName')}", 0.03)
            hacker_print(f" CITY         : {data.get('city')}", 0.03)
            hacker_print(f" ZIP CODE     : {data.get('zip')}", 0.03)
            hacker_print(f" LATITUDE     : {data.get('lat')}", 0.03)
            hacker_print(f" LONGITUDE    : {data.get('lon')}", 0.03)
            hacker_print(f" ISP          : {data.get('isp')}", 0.03)
            hacker_print(f" ORGANIZATION : {data.get('org')}", 0.03)
            hacker_print("=========================================", 0.01, Fore.GREEN)
        else:
            hacker_print(f"\n[-] ERROR: Invalid IP Address or Private IP requested.", 0.04, Fore.RED)
            
    except requests.exceptions.ConnectionError:
        hacker_print("\n[-] CONNECTION ERROR: Check your internet connection, agent.", 0.04, Fore.RED)

# Main Loop
if __name__ == "__main__":
    while True:
        display_banner()
        hacker_print("[?] Target ka IP address dalo (Ya apni IP ke liye 'Enter' maro):", 0.02, Fore.CYAN)
        target_ip = input(f"{Fore.WHITE}┌──[root@localhost]─[~]\n└──$ ").strip()
        
        track_ip(target_ip)
        
        hacker_print("\n[?] Kya kisi aur ko track karna hai? (y/n):", 0.02, Fore.CYAN)
        choice = input(f"{Fore.WHITE}└──$ ").lower().strip()
        if choice != 'y':
            hacker_print("\n[*] Exiting system... Goodbye, agent.", 0.05, Fore.YELLOW)
            time.sleep(1)
            clear_screen()
            break
