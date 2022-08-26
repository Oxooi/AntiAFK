import os
from re import S
import sys
import bot
import keyboard
from turtle import back
from time import sleep
from colorama import init, Fore, Back, Style


# Settings of Keyboard
azerty = ["z", "q", "s", "d"]
qwerty = ["w", "a", "s", "d"]

# Global variables
# BOT = bot.Bot()
toggle_button = '.'       # Toggle button to trigger the bot
default_layout = azerty   # Default layout for the keyboard
state = False

# Main function


def main():
    banner = f"""
 {Fore.CYAN}█████╗ ███╗   ██╗████████╗██╗       █████╗ ███████╗██╗  ██╗
██╔══██╗████╗  ██║╚══██╔══╝██║      ██╔══██╗██╔════╝██║ ██╔╝
███████║██╔██╗ ██║   ██║   ██║█████╗███████║█████╗  █████╔╝ 
{Fore.LIGHTMAGENTA_EX}██╔══██║██║╚██╗██║   ██║   ██║╚════╝██╔══██║██╔══╝  ██╔═██╗ 
██║  ██║██║ ╚████║   ██║   ██║      ██║  ██║██║     ██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝      ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝{Fore.RESET}
{Style.BRIGHT}<-----(Bot made by: Oxooi [https://github.com/Oxooi])----->{Style.RESET_ALL}"""

    print(banner + "\n")
    print(f'+----------------------------------------------------------------------------------+')
    print('|                       # Welcome to the AntiAFK bot #                             |')
    print('| This bot will automatically press the keys you specify when you are not in-game  |')
    print('| There few pre-defined keys combinations for games that you can use:              |')
    print('|                    You can also type your own key combination                    |')
    print(f'+----------------------------------------------------------------------------------+\n')
    print(f'{Style.BRIGHT}{Fore.RESET}Default layout is: {Fore.LIGHTBLUE_EX}{default_layout}{Fore.RESET}{Style.BRIGHT}\n')
    print(f'{Style.BRIGHT}[1] {Fore.LIGHTCYAN_EX}Sea Of Thieves{Fore.RESET}')
    print(f'[2] {Fore.LIGHTBLUE_EX}Minecraft{Fore.RESET}')
    print(f'[3] {Fore.LIGHTMAGENTA_EX}Custom Mapping{Fore.RESET}')
    print(f'[4] {Fore.LIGHTGREEN_EX}Change Keyboard Layout{Fore.RESET}')
    print(f'[0] {Fore.LIGHTRED_EX}Exit{Fore.RESET}{Style.RESET_ALL}')

    print('\n')

    choice = input(f'{Style.BRIGHT}[*] Enter your choice : {Style.RESET_ALL}')
    match choice:
        case '1':
            # Do stuff for Sea of Thieves
            print(f'{Fore.LIGHTCYAN_EX}You have chosen Sea Of Thieves{Fore.RESET}')
            sleep(1)
            sot()
        case '2':
            # Do stuff for Minecraft
            print(f'{Fore.LIGHTBLUE_EX}You have chosen Minecraft{Fore.RESET}')
        case '3':
            # Do stuff for Custom Mapping
            print(f'{Fore.LIGHTMAGENTA_EX}You have chosen Custom Mapping{Fore.RESET}')
        case '4':
            # Do stuff for Changing Keyboard Layout
            print(
                f'\n[*] Available keys are: {Fore.BLUE}(FR) {azerty}{Fore.RESET} and {Fore.RED}(ENG) {qwerty}{Fore.RESET}')

            choicelayout = input(
                f'[*] Enter your choice ({Fore.BLUE}FR{Fore.RESET}/{Fore.RED}ENG{Fore.RESET}) : ')
            if choicelayout == 'FR' or choicelayout == 'fr':
                globals()['default_layout'] = azerty
                print(
                    f'{Fore.LIGHTGREEN_EX}You\'ve change the default layout with {Fore.LIGHTBLUE_EX}{default_layout}{Fore.RESET}')
                back()
            elif choicelayout == 'ENG' or choicelayout == 'eng':
                globals()['default_layout'] = qwerty
                print(
                    f'{Fore.LIGHTGREEN_EX}You\'ve change the default layout with {Fore.LIGHTBLUE_EX}{default_layout}{Fore.RESET}')
                back()
            else:
                print(f'{Fore.LIGHTRED_EX}Invalid choice{Fore.RESET}')
                sleep(1)
                back()


def back():
    print('\nBack to the main menu')
    sleep(1)
    os.system('cls')
    main()


def sot():
    os.system('cls')
    banner = f""" {Fore.LIGHTCYAN_EX}
███████╗███████╗ █████╗      ██████╗ ███████╗    ████████╗██╗  ██╗██╗███████╗██╗   ██╗███████╗███████╗
██╔════╝██╔════╝██╔══██╗    ██╔═══██╗██╔════╝    ╚══██╔══╝██║  ██║██║██╔════╝██║   ██║██╔════╝██╔════╝
{Fore.CYAN}███████╗█████╗  ███████║    ██║   ██║█████╗         ██║   ███████║██║█████╗  ██║   ██║█████╗  ███████╗
 ╚════██║██╔══╝  ██╔══██║    ██║   ██║██╔══╝         ██║   ██╔══██║██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ╚════██║
 ███████║███████╗██║  ██║    ╚██████╔╝██║            ██║   ██║  ██║██║███████╗ ╚████╔╝ ███████╗███████║
 {Fore.BLUE}╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝
{Fore.RESET}
{Style.BRIGHT}    <------------------------------------------------------------------------------------>
    """
    print(banner)
    print(
        f'{Fore.LIGHTCYAN_EX}[1] {Fore.LIGHTBLUE_EX}Forward & Backward{Fore.RESET}')
    print(
        f'{Fore.LIGHTCYAN_EX}[2] {Fore.LIGHTBLUE_EX}Left & Right{Fore.RESET}')
    print(f'{Fore.LIGHTCYAN_EX}[3] {Fore.LIGHTBLUE_EX}Jump{Fore.RESET}')
    print(f'{Fore.LIGHTCYAN_EX}[4] {Fore.LIGHTBLUE_EX}Auto-Row{Fore.RESET}')
    print(f'{Fore.LIGHTCYAN_EX}[0] {Fore.LIGHTRED_EX}Exit{Fore.RESET}')
    print('\n')
    choice = input('Enter your choice : ')
    match choice:
        case '1':
            # Do stuff for Forward & Backward
            print(f'{Fore.LIGHTBLUE_EX}You have chosen Forward & Backward{Fore.RESET}')
            fw_bw()
        case '2':
            # Do stuff for Left & Right
            print(f'{Fore.LIGHTBLUE_EX}You have chosen Left & Right{Fore.RESET}')
        case '3':
            # Do stuff for Jump
            print(f'{Fore.LIGHTBLUE_EX}You have chosen Jump{Fore.RESET}')
        case '4':
            # Do stuff for Auto-Row
            print(f'{Fore.LIGHTBLUE_EX}You have chosen Auto-Row{Fore.RESET}')
        case '0':
            # Do stuff for Exit
            print(f'{Fore.LIGHTRED_EX}You have chosen to exit{Fore.RESET}')
            back()

def fw_bw():
    keyboard.wait('.')
    globals()['state'] = True
    while globals()['state'] == True:
        keyboard.press(default_layout[0])
        sleep(0.5)
        keyboard.release(default_layout[0])
        sleep(0.5)
        keyboard.press(default_layout[2])
        sleep(0.5)
        keyboard.release(default_layout[2])
        sleep(0.5)
    # print(default_layout[0])


if __name__ == '__main__':
    main()
