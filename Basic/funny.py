import time as t
from multiprocessing.resource_sharer import stop
import os

os.system('cls||clear')

def nuke_mars():
    os.system('cls||clear')
    print("Nuke to mars inbound...")
    x = 0
    while x < 10:
        print(x)
        t.sleep(1)
        x = x + 1
    print("Mars is no longer")

def nuke_china():
    os.system('cls||clear')
    print("Nuke to China inbound...")
    x = 0
    while x < 10:
        print(x)
        t.sleep(1)
        x = x + 1
    print("China is no longer")

def nuke_PIS():
    os.system('cls||clear')
    print("Nuke to PIS inbound...")
    x = 0
    while x < 10:
        print(x)
        t.sleep(1)
        x = x + 1
    print("PIS is no longer")

def main():

    nuke = int(input("What to nuke ? 💀\n 1) Mars\n 2) China\n 3) PIS\n == "))
    
    if nuke == 1: nuke_mars()
    if nuke == 2: nuke_china()
    if nuke == 3: nuke_PIS()

    main()
main()