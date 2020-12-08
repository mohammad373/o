import os
import time
import sys
import socket
from colorama import Fore

def __ip__():
    os.system("clear")
    try:
        print(Fore.GREEN + "Helloe . Welcome ;)")
        time.sleep(2)
        try:
            print(Fore.YELLOW + "[!] - Pleass 5 Sec Latter ...")
            time.sleep(1)
            print(Fore.YELLOW + "[!] - Pleass 4 Sec Latter ...")
            time.sleep(1)
            print(Fore.YELLOW + "[!] - Pleass 3 Sec Latter ...")
            time.sleep(1)
            print(Fore.YELLOW + "[!] - Pleass 2 Sec Latter ...")
            time.sleep(1)
            print(Fore.YELLOW + "[!] - Pleass 1 Sec Latter ...")
            time.sleep(1)
        except:
            pass

        s1 = socket.gethostname()
        s2 = socket.gethostbyname(s1)
        print(Fore.GREEN + "\n[+] - Your Ip ==> " + Fore.BLUE + s2)
        time.sleep(5)
    except:
        try:
            print(Fore.YELLOW + "\nGood Bay ;)")
            sys.exit()
        except:
            pass
__ip__()
