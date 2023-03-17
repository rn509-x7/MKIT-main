import qrcode
import sys
import time
import os

print("""
| ================= |
|  mkit/payload/qr  |
| ================= |
     """)
     
while True:
    pilihan = input("\033[1;31mmk\033[0m\033[1;37mit\033[0m \033[1;32m> ")
    
    if pilihan =="set url":
        text = input("URL : ")
        print(f"URL => {text}")
    elif pilihan =="exploit":
        img = qrcode.make(text)
        img_file = "qrcode.png"
        img.save(img_file)
        print("Done")
        print("QR code In File => ", os.path.abspath(img_file))
    elif pilihan =="help":
        print("""
        set url : Set Your URL
        exploit : Run Exploit
        """)
