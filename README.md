
This little script allows a Raspberry Pi using the different LSG tools to inform the server it is on the network.
#installation
- sudo apt-get update && sudo apt-get upgrade
- sudo apt-get install git
- git clone https://github.com/FrancoMaxime/lsg-connect
- sudo cp /lsg-connect/LSG-CONNECT.service /etc/systemd/system/
- sudo systemctl daemon-reload
- sudo systemctl enable LSG-CONNECT
- sudo systemctl start LSG-CONNECT
- systemctl status LSG-CONNECT
- sudo reboot


Don't forget to change the RPI_ID with the name of the tray on the lsg-web.
Don't forget to change the LSG_WEB_SERVER with the IP of the LSG_WEB server.
