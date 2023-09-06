#!/usr/bin/env python3
#*- coding: utf-8 -*--
#Coded by Morbius.os

AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'

import os
import time 
import requests
try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install bs4')
import sys

Mor = '\033[95m'
Cyan = '\033[96m'
KoyuMavi = '\033[36m'
Mavi = '\033[94m'
Yeşil = '\033[92m'
Sarı = '\033[93m'
Kırmızı = '\033[91m'
Kalın = '\033[1m'
AltıÇizili = '\033[4m'
Bitir = '\033[0m'#
Beyaz ='\033[1;37m'

def banner():
    print(f"""
{Mor} __  __            _     _             {Sarı}____  _ _                            
{Mor}|  \/  | ___  _ __| |__ (_)_   _ ___  {Sarı}/ ___|(_) |_ ___                        
{Mor}| |\/| |/ _ \| '__| '_ \| | | | / __| {Sarı}\___ \| | __/ _ \                        
{Mor}| |  | | (_) | |  | |_) | | |_| \__ \  {Sarı}___) | | ||  __/                        
{Mor}|_|  |_|\___/|_|  |_.__/|_|\__,_|___/ {Sarı}|____/|_|\__\___|                        
{KoyuMavi}
          ____                  _
         / ___|___  _ __  _   _(_) ___ _ __
        | |   / _ \| '_ \| | | | |/ _ \ '__|
        | |__| (_) | |_) | |_| | |  __/ |
         \____\___/| .__/ \__, |_|\___|_|
                   |_|    |___/
            
{Beyaz}{Kalın}Author: {Yeşil}{AUTHOR}
{Beyaz}{Kalın}Github: {Yeşil}{GİTHUB}
{Beyaz}{Kalın}Instagram: {Yeşil}{INSTAGRAM}{Beyaz}
""")

banner()
http = 'http://'
https = 'https://'

url = input(f'Kopyalamak İstediğiniz Sitenin Linkini Giriniz: {Yeşil}')
if url == 'q':
    sys.exit()

if url.startswith(http) or url.startswith(https):
    pass
else:
    while True:
        print(f'{Kırmızı}{Kalın}Lütfen Site Linkini Düzgün Giriniz!(örnek > https://example.com)')
        url2 = input(f'{Beyaz}Lütfen Kopyalamak İstediğiniz Sitenin Linkini Düzgün Bir Şekilde Giriniz: {Yeşil}')
        if url2.startswith(http) or url2.startswith(https):
            pass
        if url2 == 'q':
            sys.exit()
            
dosya_naame = input(f'{Beyaz}Siteyi Kopyaladığınız Dosyaya Bir İsim Girin: {Yeşil}')
dosya_yolu = input(f'{Yeşil}{dosya_naame}{Beyaz} İsimli Dosyanızı Hangi Klasöre Kaydetmek İstersiniz ({Yeşil}/var/www/html/example.html {Beyaz}Şeklinde Yazınız, Eğer Dosya Yolu Belirtmek İstemiyorsanız {Yeşil}"0"{Beyaz} Yazınız): {Yeşil}')
if dosya_yolu == "0":
    dosya_yolu = ""

if dosya_naame in ".html":
    pass
else:
    dosya_naame = dosya_naame+'.html'

response = requests.get(url)
html_content = response.content
çorbaaa = BeautifulSoup(html_content, 'html.parser')

with open(dosya_yolu+dosya_naame, 'w', encoding='utf-8') as file:
        file.write(str(çorbaaa))
        if dosya_yolu == "0":
            print(f'{Beyaz}Dosyanız {Yeşil}{dosya_naame}{Beyaz}ismi ile {Yeşil}{dosya_yolu}{Beyaz} dosyasının altına kayıt edildi.')
        else:
            print(f'{Beyaz}Dosyanız {Yeşil}{dosya_naame}{Beyaz}ismi ile kayıt edildi.')
