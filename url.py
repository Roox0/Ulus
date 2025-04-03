import os
from pyfiglet import Figlet
from termcolor import colored
import webbrowser
import os
import time
from datetime import datetime
import sys

    



GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
RESET = "\033[0m" 

class Tool:
    def __init__(self):
        self.display_logo()

    @staticmethod
    def display_logo():
        figlet = Figlet(font='starwars')  
        logo_text = figlet.renderText('ROOX')
        logo_colored = colored(logo_text, color='blue', attrs=['bold'])
        print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {logo_colored}
    ~ Sahibi        : @Roox_00
    ~ Kanalımız :  JED ~ ARCHIVE
 
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')

    @staticmethod
    def process_file(file_path):
        if not os.path.isfile(file_path):
            print(f"{RED}  Dosya Bulunmadı!{RESET}")
            return

        print(f"{GREEN}  Dosya okuma işlemi başlatıldı...{RESET}")
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        valid_lines = []
        invalid_lines = []

        for line in lines:
            if 'http://' in line or 'https://' in line:
                parts = line.strip().split(':')
                if len(parts) == 4:
                    _, _, username, password = parts
                    valid_lines.append(f"{username}:{password}\n")
                else:
                    invalid_lines.append(line.strip())
            else:
                invalid_lines.append(line.strip())
        
        if valid_lines:
            print(f"{GREEN}  Geçerli bilgiler işleniyor...{RESET}")
            with open(file_path, 'w') as file:
                file.writelines(valid_lines)
            print(f"{GREEN}  Başarıyla güncellendi{RESET}")
        else:
            print(f"{RED}  Geçerli bilgi bulunamadı{RESET}")
        
        if invalid_lines:
            print(f"{YELLOW}  Hatalı veya geçersiz formatta satırlar{RESET}")
            for invalid in invalid_lines:
                print(f"{RED}  - {invalid}{RESET}")


tool_instance = Tool()


file_name = input(f"{GREEN} DOSYA YOLU GİR PRENSES {RED}: {YELLOW}")
tool_instance.process_file(file_name)
