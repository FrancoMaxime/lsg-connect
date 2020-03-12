import requests
import socket
import time

RPI_ID = "Plateau1"
LSG_WEB_IP = "http://192.168.1.4:5000/tray/connect"

count = 30

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

RPI_IP = s.getsockname()[0]

data = {"name" : RPI_ID, "ip" : RPI_IP}

while True:
	if count == 30:
		count = 0
		x = requests.post(LSG_WEB_IP, data)
		print(x)
	count += 1
	time.sleep(1)
