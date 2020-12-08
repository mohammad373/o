# o
import os
import requests
import sys
import time
import socket
from colorama import Fore

def __targert__():
    os.system("clear")
    try:
        time.sleep(1.2)
        print(Fore.YELLOW + "Helloe . Welcome Back ;)")
        time.sleep(1.3)
        target = input(Fore.GREEN + "\nEnter Your Address Target ==>  ")
        time.sleep(2)
        if target == "" or None:
            try:
                time.sleep(2)
                print(Fore.RED + "\n[!] - Error : Your Targrt Is None ;(")
                time.sleep(1.2)
                q = input(Fore.YELLOW + "\nAre Your Clear The Page ?  1 : yes   2 : no")
                if q == "1":
                    try:
                        time.sleep(1)
                        os.system("clear")
                        sys.exit()
                    except:
                        pass
                if q == "2":
                    try:
                        time.sleep(1)
                        print(Fore.BLUE + "\nOk Good Bay ;)")
                        sys.exit()
                    except:
                        pass
            except:
                pass
        s = socket.gethostbyname(target)
        r = requests.get("https://who.is/whois-ip/ip-address/" + s).text
        try:
            print(Fore.GREEN + "Your Ip Target ==> " + s)
            time.sleep(1)
            print(Fore.GREEN + "Your City Target ==> " + r["City"])
        except:
            pass
    except:
        pass
__target__()
