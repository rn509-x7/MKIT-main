import os
import sys
import time

os.system("clear")

print("""\033[1;92m
██ ███    ██ ███████ ████████  █████  ██      ██          
██ ████   ██ ██         ██    ██   ██ ██      ██          
██ ██ ██  ██ ███████    ██    ███████ ██      ██          
██ ██  ██ ██      ██    ██    ██   ██ ██      ██          
██ ██   ████ ███████    ██    ██   ██ ███████ ███████     
- By RN509X7 -
""")
pilih = input ("Do You Want To Install This Tools (y/n) => ")

if pilih =="y":
      os.system("apt install hydra")
      os.system("pip3 install requests")
      os.system("apt install git")
      os.system("pip3 install qrcode")
      os.system("python3 mkit.py")
if pilih =="n":
      print("Thanks For running This Tools :)")
      
