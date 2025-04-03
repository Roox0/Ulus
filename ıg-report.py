import os
import requests
import random
import time
from termcolor import colored
import threading
import webbrowser
import sys



def get_random_ip():
    try:
        url = 'https://api64.ipify.org?format=json'
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            ip_address = response.json()['ip']
            return ip_address
        else:
            print(colored(f"IP adresi alınırken hata oluştu. Durum Kodu: {response.status_code}", "red"))
            return None
    except requests.RequestException as e:
        print(colored(f"IP adresi alınırken hata oluştu. Hata: {e}", "red"))
        return None



def send_report(username, name, reported_username, reported_name, email_list):
    user_agent = "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844"
    url = "https://help.instagram.com/contact/653100351788502"
    head = {
        "Host": "help.instagram.com",
        "Content-Length": "715",
        "X-FB-LSD": "AVq5uabXj48",
        "X-ASBD-ID": "129477",
        "Sec-Ch-UA-Mobile": "?1",
        "User-Agent": user_agent,
        "Sec-Ch-UA": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
        "Sec-Ch-UA-Platform": "\"Android\"",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": url,
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": f"{url}/contact/723586364339719",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5",
        "Cookie": "ig_nrcb=1"
    }

    while True:
        random_email = random.choice(email_list)
        random_ip = get_random_ip()
        if not random_ip:
            continue

        ts1 = str(int(time.time()))
        data = f'jazoest=2931&lsd=AVq5uabXj48&Field258021274378282={reported_username}&Field735407019826414={reported_name}&Field506888789421014[year]=2014&Field506888789421014[month]=11&Field506888789421014[day]=11&Field294540267362199=Parent&inputEmail={random_email}&support_form_id=723586364339719&support_form_locale_id=en_US&support_form_hidden_fields=%7B%7D&support_form_fact_false_fields=[]&__user=0&__a=1&__req=6&__hs=19552.BP%3ADEFAULT.2.0..0.0&dpr=1&__ccg=GOOD&__rev=1007841948&__s=s4c6vz%3Anapxo9%3An9ncx2&__hsi=7255652935514227640&__dyn=7xe6E5aQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXw5ux60Vo1upE4W0OE2WxO2O1Vwooa81VohwnU1e42C220qu1Tw40wdq0Ho2ewnE3fw6iw4vwbS1Lw4Cwcq&__csr=&__spin_r=1007841948&__spin_b=trunk&__spin_t={ts1}'

        try:
            res = requests.post(url, data=data, headers=head, timeout=10).status_code
            if res == 200:
                print(f'[+] Durum Kodu : {res}')
                print(colored("Rapor başarıyla gönderildi.", "red"))
                print(colored(f"Kullanılan e-posta: {random_email}", "green"))
                print(colored(f"Kullanılan IP adresi: {random_ip}", "green"))
                print(colored(f"{colored(reported_name, 'yellow')} ({colored(reported_username, 'blue')}) e-posta ile raporlandı {random_email}.", "cyan"))
                print(colored("RAPOR BAŞARILI OLARAK GÖNDERİLDİ REAPER Š1K€R", "blue"))
            else:
                print(f"[!] Rapor gönderilirken bir hata oluştu Durum Kodu: {res}")
                print(colored(f"Kullanılan e-posta: {random_email}", "red"))

        except requests.RequestException as e:
            print(f" İstek sırasında bir hata oluştu: {e}")
            print(colored(f"Kullanılan e-posta: {random_email}", "red"))

def start_reporting():
    reported_username = input("Raporlamak istediğiniz kullanıcı adı girin: ")
    reported_name = input("Raporlamak istediğiniz kişinin ismini girin: ")
    num_emails = int(input("Raporlamak için kullanılacak e-posta sayısını girin: "))


    
    email_list = []
    for i in range(num_emails):
        email = input(f"E-posta {i+1} girin: ")
        email_list.append(email)

    num_threads = int(input("Kullanmak istediğiniz threades sayısını girin (10-25 arasi yaz: "))
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=send_report, args=("", "", reported_username, reported_name, email_list))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print(f'=======================================')
    start_reporting()
