import random
import string
import os
import colorama
from colorama import Fore, Back, Style

def generate_password(uppercases=True, length=12, digits=True, symbols=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if uppercases else ""
    length = max(length, 10)
    digits = string.digits if digits else ""
    symbols = string.punctuation if symbols else ""
    mix = lowercase_letters + uppercase_letters + digits + symbols
    password = ''.join(random.choice(mix) for _ in range(length))
    return password

def write_file(application_name, password):
    with open("passwords.txt", "a") as file:
        file.write(f"{application_name}: {password}\n")

def get_yes_or_no(prompt):
    while True:
        response = input(prompt).strip().upper()
        if response in ["YES", "Y"]:
            return True
        elif response in ["NO", "N"]:
            return False
        elif response in ["QUIT", "Q"]:
            return None
        else:
            print(Fore.RED + "Please enter 'Yes' (Y) or 'No' (N)." + Style.RESET_ALL)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLACK + Back.WHITE + "P A S S W O R D    G E N E R A T O R" + Style.RESET_ALL)
    
    application_name = input("Name of the application where this password will be used: ")
    while not application_name.strip():
        print(Fore.RED + "Please enter a valid value. This field is required." + Style.RESET_ALL)
        application_name = input("Name of the application where this password will be used: ")

    uppercase_letters = get_yes_or_no("Include uppercase letters? (Yes/No): ")
    if uppercase_letters is None:
        break

    while True:
        length_input = input("Length of the password (minimum 10): ")
        if length_input.isdigit():
            length = int(length_input)
            if length >= 10:
                break
            print(Fore.RED + "Please enter a value of 10 or greater." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)

    include_numbers = get_yes_or_no("Include numbers? (Yes/No): ")
    if include_numbers is None:
        break

    include_symbols = get_yes_or_no("Include symbols/special characters? (Yes/No): ")
    if include_symbols is None:
        break

    password = generate_password(uppercase_letters, length, include_numbers, include_symbols)
   
    print(Fore.GREEN + f"[Success] Password successfully generated for {application_name}, you can find it in passwords.txt: {password}" + Style.RESET_ALL)
    write_file(application_name, password)
    input(Back.YELLOW + "Press ENTER to start again or type 'QUIT' to quit: " + Style.RESET_ALL)