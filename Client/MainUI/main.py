import requests
from getmac import get_mac_address as gma
import os
import hashlib
import pyautogui
import UI


mac = gma().replace(":","-")
mac_addr = hashlib.shake_256(mac.encode('utf-8')).hexdigest(10)
response = requests.get('http://localhost:5000/get_access/'+mac_addr)
data = response.json()
#response = requests.get('https://w3schools.com/python/demopage.htm')

#print(response.text)

def show_error():
    pyautogui.alert("Không tìm thấy địa chỉ IP", "Lỗi")

print(mac_addr)
print(data['ip_addr'])

if response != None:
    UI.run()
else:
    show_error()

