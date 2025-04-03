import requests
import threading
import webbrowser
import os
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
    import pyfiglet
    
os.system("clear")


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
|{Z}[+] Channel  : {B}JED ~ ARCHIVE |
|{Z}[+] Tool  : {B} Proxy Checker |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')



file=input("Combo dosyasını gir: ")

print("Başlıyor...")

def chk(proxy):
    proxi_Monti = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy,
    }
    try:
        requests.get("https://google.com/", proxies=proxi_Monti,timeout=15)
        print(f"\x1b[1;32m Canlı [=] {proxy}")
        q= open("/sdcard/Monti-Proxy.txt",'a+')
        q.write(proxy+'\n')
    except:
        print("\x1b[1;31m Ölü: "+proxy)
        
total=open(file,'r').readlines()
uz=len(total)

def c1():
    for monti in range(0,uz,10):
        up=total[monti].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
        
def c2():
    for monti in range(1,uz,10):
        up=total[monti].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
        
def c3():
    for monti in range(2,uz,10):
        up=total[monti].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
        
def c4():
    for monti in range(3,uz,10):
        up=total[monti].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
        
def c5():
    for monti in range(4,uz,10):
        up=total[monti].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
        
def c6():
    for monti in range(5,uz,10):
        up=total[monti].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
        
def c7():
    for monti in range(6,uz,10):
        up=total[monti].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
        
def c8():
    for monti in range(7,uz,10):
        up=total[monti].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
        
def c9():
    for monti in range(8,uz,10):
        up=total[monti].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
        
def c10():
    for monti in range(9,uz,10):
        up=total[monti].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
        
a1 = threading.Thread(target=c1)
a2 = threading.Thread(target=c2)
a3= threading.Thread(target=c3)
a4= threading.Thread(target=c4)
a5= threading.Thread(target=c5) 
a6= threading.Thread(target=c6) 
a7 = threading.Thread(target=c7)
a8 = threading.Thread(target=c8)
a9= threading.Thread(target=c9)
a10= threading.Thread(target=c10)
a1.start() 
a2.start() 
a3.start() 
a4.start() 
a5.start() 
a6.start()
a7.start() 
a8.start() 
a9.start() 
a10.start() 
