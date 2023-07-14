from colorama import Fore
from pystyle import Colorate, Colors, Center
from pynput.keyboard import Controller
from datetime import timedelta

import os
import time
import pyautogui
import threading

keyboards = Controller()
current_option = 0


###### MISC UTILS ######
def title():
    os.system("cls")
    os.system("title Rage Utils -- V1.0")
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_red, """

██████╗  █████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝ ██╔════╝
██████╔╝███████║██║  ███╗█████╗  
██╔══██╗██╔══██║██║   ██║██╔══╝  
██║  ██║██║  ██║╚██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                 
    Made by professedray4
    """, 2)))


def timer():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        formatted_time = str(timedelta(seconds=elapsed_time))
        print(Fore.BLUE + f"Elapsed time: {formatted_time}", end='\r')
        time.sleep(1)


def countdown(seconds):
    while seconds > 0:
        if seconds == 1:
            print("1 second until script starts")
        else:
            print(f"{seconds} seconds until script starts")
        time.sleep(1)
        seconds -= 1
    os.system("cls")
    title()

def alert(message):
    pyautogui.alert(text=message, title="Made by professedray4 ;3")


###### CAR AFK ######

def send_a():
    pyautogui.keyDown('a')


def send_d():
    pyautogui.keyDown('d')


def car_main():
    countdown(5)
    timer_thread = threading.Thread(target=timer)  ## Dont mess with unless u know threading ;3
    a_thread = threading.Thread(target=send_a)
    d_thread = threading.Thread(target=send_d)

    timer_thread.start()
    a_thread.start()
    d_thread.start()

    timer_thread.join()
    a_thread.join()
    d_thread.join()


###### ANTI AFK ######
def anti_afk():
    keys = ['w', 'a', 's', 'd']
    duration = .7
    rounds = 0
    countdown(5)
    while True:
        print(Fore.RED + f"Number of rounds completed: {rounds}", end='\r')
        for key in keys:
            keyboards.press(key)
            time.sleep(duration)
            keyboards.release(key)
            time.sleep(15)
        rounds += 1

###### E ######
def e():
    rounds = 0
    countdown(5)
    while True:
        print(Fore.MAGENTA + f"> Pressing [E] x{rounds}")
        keyboards.press("e")
        time.sleep(7)  # How long it needs to hold for
        keyboards.release("e")
        time.sleep(1)  # small break before going again
        rounds += 1

###### OIL ######
### IF UR MONITOR IS NOT 1920 X 1080 GET NEW COORDS

def oil():
    alert("IF MONITOR IS NOT 1920 X 1080 YOU MUST GET NEW COORDS")
    countdown(10)
    while True:
        timer()
        pyautogui.mouseDown(269, 752)  # moves mouse to these coords (first circle u need to hold)
        time.sleep(5)
        pyautogui.mouseUp(269, 752)
        # Second
        pyautogui.mouseDown(366, 750)
        time.sleep(5)
        pyautogui.mouseUp(366, 750)
        # third
        pyautogui.mouseDown(467, 750)
        time.sleep(5)
        pyautogui.mouseUp(467, 750)
        # fourth
        pyautogui.mouseDown(577, 751)
        time.sleep(5)
        pyautogui.mouseUp(577, 751)
        time.sleep(2)  # give game a sec
        # repeat


###### GYM BOT ######
def workout():
    countdown(5)
    while True:
        print("Working out")
        pyautogui.press("e")
        time.sleep(5)


###### START ######
def main():
    os.system("cls")
    os.system("title Rage Utils -- V1.0")
    title()
    selection()


def login(kitty):
    print(Fore.BLUE + "Entering password...")
    prompt = pyautogui.password(text='Please enter a password', title='Made by ProfessedRay4', default='', mask='*')
    if prompt == kitty:
        prompt("Correct password! Discord: https://discord.gg/8nRQbGYDZD")
        print(Fore.GREEN + "Correct password!")
        main()
    else:
        pyautogui.alert(text="Incorrect password. Please try again or dm me on discord (professedray4)",
                        title="Incorrect password")
        login(
            "VSBMSUtFIEJJRyBPSUxFRCBVUCBCTEFDSyBNRU4gVFdFUktJTkcgQUxMIE9WRVIgVVIgU0NSRUVOIFdJVEggVEhFSVIgUFBTIE9VVA==")


###### SELECTION ######

def selection():
    ask = input(
        Center.XCenter(Colorate.Vertical(Colors.red_to_purple, "> Please enter the number you would like to run:\n1) Car afk\n2) Anti afk\n3) Oil\n4) E\n5) Gym bot\nType [help] for info about commands \n>", 2)))
    if ask == "1":
        print(Fore.MAGENTA + "> [Car afk] was chosen")
        car_main()
    elif ask == "2":
        print(Fore.MAGENTA + "> [AFK script] was chosen")
        anti_afk()
    elif ask == "3":
        print(Fore.MAGENTA + "> [Oil script] was chosen")
        oil()
    elif ask == "4":
        print(Fore.MAGENTA + "> [E script] was chosen")
        e()
    elif ask == "5":
        print(Fore.MAGENTA + "> [Gym bot] was chosen")
        workout()
    elif ask == "help":
        print(Fore.RED + "Info about the commands:\n"
                         "1) Car afk: For this script, just in your car in a garage (preferably in house/apartment) and then run this script, it holds [a] and [d] keys down to prevent you from getting kicked\n"
                         "2) Oil: Self explanatory, but go to a oil quarry and click e, then let it do it's thing ||||IMPORTANT WILL NOT STOP IF YOU GET CAPTCHA\n"
                         "3) E: Literary just holds e for the required time to fish/mine (if you have lvl 2 change how long it holds it if you want)\n"
                         "4) Gym: Simple gym bot that will click [e] every 5 seconds ||||IMPORTANT ADMINS MAY TP TO U AND WILL BLOCK U IF U DO NOT RESPOND")
        countdown(10)
        os.system("cls")
        selection()
    else:
        print(Fore.LIGHTRED_EX + "> INCORRECT OPTION, PLEASE MAKE SURE YOU PUT THE CORRESPONDING NUMBER, NOT THE NAME OF THE SCRIPT")
        countdown(5)
        os.system("cls")
        selection()


title()
login("VSBMSUtFIEJJRyBPSUxFRCBVUCBCTEFDSyBNRU4gVFdFUktJTkcgQUxMIE9WRVIgVVIgU0NSRUVOIFdJVEggVEhFSVIgUFBTIE9VVA==")
