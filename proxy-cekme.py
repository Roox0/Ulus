import requests
api = requests.get("https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=ipport&format=text")
if api.status_code == 200:
 with open("/storage/emulated/0/Download/log/proxy3.txt", "w") as wizard:
  wizard.write(api.text)
 print(f"\x1b[1;32m✅ Proxy Başarıyla Çekildi.\n👀 Proxy Türü: HTTP, SOCKS4    ")
else:
 print("⛔ Proxy Çekilemedi.")
