import requests
import socket
import time

RPI_ID = "Plateau1"
LSG_WEB_IP = "http://0.0.0.0:5000/tray/connect"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

RPI_IP = s.getsockname()[0]

data = {"name" : RPI_ID, "ip" : RPI_IP}

while True:
	x = requests.post(LSG_WEB_IP, data)
	print(x)
	time.sleep(30)
