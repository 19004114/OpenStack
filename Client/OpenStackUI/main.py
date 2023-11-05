import os.path

from getmac import get_mac_address as gma
import mysql.connector
import hashlib
import pyautogui
import time
import os,sys
from PIL import Image

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

def open_remote_desktop(username, server_address):
    pyautogui.hotkey('win', 'r')
    pyautogui.write('mstsc')
    pyautogui.press('enter')
    pyautogui.write(server_address)
    time.sleep(0.5)

    button = pyautogui.locateOnScreen(Image.open(resource_path('button.png')))
    print(button)
    if button:
        pyautogui.click(button)
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write(username)
        pyautogui.press('enter')
    else:
        print("'Show Options' button not found")

def check_data():
    mac = gma().replace(":","-")
    #mac = "2903890128309283"
    mac_addr = hashlib.shake_256(mac.encode('utf-8')).hexdigest(10)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="openstack"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM quyentruycap WHERE mac_addr = %s", (mac_addr,))
    result = mycursor.fetchone()

    return result

def show_error():
    pyautogui.alert("Không tìm thấy địa chỉ IP","Lỗi")

if check_data():
    username = check_data()[4]
    password = check_data()[5]
    server_address = check_data()[6]
    open_remote_desktop(username,server_address)
else:
    show_error()