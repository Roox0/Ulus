import time
import os
import webbrowser
import os
import sys
from datetime import datetime
import requests



print('bir hata var çözemedim')


def Roox_31_cekme():
    valentia_yarak = [
        "...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n████████████████████\n▓▓▓▓▓▓█░░░░░░░░░░░░░███\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░█░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░██\n███████████████████\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀▀▀▀▀▀▀▀",
        "...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n████████████████████\n▓▓▓▓▓▓█░░░░░░░░░░░░░███\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░█░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░██\n███████████████████",
        "...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n████████████████████\n▓▓▓▓▓▓█░░░░░░░░░░░░░███\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░█░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░██\n███████████████████\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀",
    ]

    for i in range(20):
        for frame in valentia_yarak:
            os.system('cls' if os.name == 'nt' else 'clear')  
            print(frame)
            time.sleep(0.3)

if __name__ == "__main__":
    Roox_31_cekme()
