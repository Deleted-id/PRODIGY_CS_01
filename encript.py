#!/usr/bin/python

# importing required libraries and modules 
from colorama import Fore, Style
import pyfiglet
from modules import *
from os import system as run

# defining pyfiglet format as format
format = pyfiglet.figlet_format

# defining colores
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
reset = Style.RESET_ALL


# simple banner to make it look good
def banner():
    print(red+format("Encript")+reset)
    print(blue+"------------------------------------\n"+reset)

# main method
def main():
    banner()
    menutext = "[1] Encrypt text\n[2] Decrypt text\n[00] Exit\n\t=>"
    text = input(blue+"Enter text : ")
    count = int(input("Shift count : "+reset))
    choice = int(input(green+menutext+reset))
    if choice == 1:
        et = encrypt_text(text, count)
        print("Encrypted text =>",red,et,reset)
    elif choice == 2:
        dt = decrypt_text(text, count)
        print("Decrypted text =>",red,dt,reset)
    else:
        run("exit")

# calling the main method 
if __name__ == "__main__":
    main()