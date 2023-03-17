import os
import sys
import time

os.system("clear")
print("""\033[1;32m
 /$$      /$$ /$$   /$$ /$$$$$$ /$$$$$$$$
| $$$    /$$$| $$  /$$/|_  $$_/|__  $$__/
| $$$$  /$$$$| $$ /$$/   | $$     | $$   
| $$ $$/$$ $$| $$$$$/    | $$     | $$   
| $$  $$$| $$| $$  $$    | $$     | $$   
| $$\  $ | $$| $$\  $$   | $$     | $$   
| $$ \/  | $$| $$ \  $$ /$$$$$$   | $$   
|__/     |__/|__/  \__/|______/   |__/   
- By ./RN509X7 -                                         
""")
while True:

    pilihan = input("\033[1;31mmk\033[0m\033[1;37mit\033[0m \033[1;32m> ")
    if pilihan == "help":
        print("""
payload : Payload for Exploit
open payload : set payload for exploit

clear : Clear Tools

tools : Show Tools 
open tools : Open Tools
        """)
    elif pilihan == "open tools https://github.com/Pymmdrza/Ethereum_PrivateKey_Address_Generator":
         os.system("python tools/t2.py")
    elif pilihan == "open tools https://github.com/rn509/AccountEmpas-main-":
         os.system("python tools/t1.py")
    elif pilihan =="open payload mkit/payload/qr":
         os.system("python module/m2.py")
    elif pilihan =="open tools https://github.com/htr-tech/zphisher":
         os.system("python tools/t3.py")
    elif pilihan == "tools":
         print("""
|===================|
|====== Tools ======|
|=====================================================================|
| https://github.com/rn509/AccountEmpas-main-                               |
| https://github.com/Pymmdrza/Ethereum_PrivateKey_Address_Generator   |
| https://github.com/htr-tech/zphisher                                |
======================================================================|
         """)
    elif pilihan == "payload":
         print("""
|=================|
|==== PayLoad ====|
|=================|
| mkit/payload/cp | Cracking Password SSH
| mkit/payload/qr | Import Url To QR CODE
===================
         """)
    elif pilihan == "clear":
         os.system("clear")
         print("""
 /$$      /$$ /$$   /$$ /$$$$$$ /$$$$$$$$
| $$$    /$$$| $$  /$$/|_  $$_/|__  $$__/
| $$$$  /$$$$| $$ /$$/   | $$     | $$   
| $$ $$/$$ $$| $$$$$/    | $$     | $$   
| $$  $$$| $$| $$  $$    | $$     | $$   
| $$\  $ | $$| $$\  $$   | $$     | $$   
| $$ \/  | $$| $$ \  $$ /$$$$$$   | $$   
|__/     |__/|__/  \__/|______/   |__/   
- By ./RN509X7 -                                         
""")
    elif pilihan == "open payload mkit/payload/cp":
         os.system("python module/m1.py")
    else:
         print("Commands Not Found. Type ( help ) For Options")
