from re import S
from urllib import response
from webbrowser import get
import requests
from colorama import Fore, Style, init
from random import choice
from time import sleep
import ascii_magic
import pyfiglet
import os

init()

f_style = 'cosmic'


def print_blue(s):
    print(Fore.BLUE, Style.BRIGHT, s, Style.RESET_ALL)

def print_red(s):
    print(Fore.RED, Style.BRIGHT, s, Style.RESET_ALL)

def print_yellow(s):
    print(Fore.YELLOW, Style.BRIGHT, s, Style.RESET_ALL)

def print_green(s):
    print(Fore.GREEN, Style.BRIGHT, s, Style.RESET_ALL)

def get_participants(people):       #Let's me print a better message than 'participants: 1'
    people = int(people)
    if people == 1:
        return "Probably somthing you'll want to do alone"    
    else:
        return f"Somthing that might be fun with {people - 1} friend{'s' if people - 1 > 1 else ''}"

def pokemon_appears():
    os.system('cls' if os.name == 'nt' else '')
    poke = choice(list(range(1,151)))
    url = f'https://pokeapi.co/api/v2/pokemon/{poke}'
    response = requests.get(url)
    pokemon = response.json()
    sleep(1)
    poke_pic = ascii_magic.from_url(pokemon["sprites"]['other']['official-artwork']["front_default"], columns= 60)
    ascii_magic.to_terminal(poke_pic)
    print_red('\nA wild pokemon appeared')
    name = input("\nTo catch it, call out it's name: ").lower()
    os.system('cls' if os.name == 'nt' else '')
    poke_name = pyfiglet.figlet_format(name, font = f_style)
    print_blue(f'\n\n\n\n{poke_name}')
    sleep(2)
    os.system('cls' if os.name == 'nt' else '')
    congrats = pyfiglet.figlet_format('WOW !', font = f_style)
    print('\n\n', congrats, sep='')
    sleep(2)
    if name == pokemon['name']:
        you = pyfiglet.figlet_format('\tYou', font = f_style)
        rock =pyfiglet.figlet_format('Rock !', font = f_style)
        print_green(you+'\n'+rock)
        print(f'\n\nYou Successfully caught {name.title()}')
    else:
        you2 = pyfiglet.figlet_format('\tYou', font = f_style)
        suck =pyfiglet.figlet_format('Suck !', font = f_style)
        print_red(you2+'\n'+suck)
        print(f"\n\nThis pokemon's name is {pokemon['name'].title()} not {name.title()}")








def get_activity():
    print_yellow("**Please note it is hard to find activities when the minimum is greater than $100**")
    while True:
        min = input("\nWhat would you like your minimum price range to be?: $").strip()
        max = input("\nWhat would you like your maximum price range to be?: $").strip()
        if not min.isdigit() or not max.isdigit():
            print_yellow("One of your range entries was not a integer please only enter whole numbers")
            continue
        min = int(min)/100
        max = int(max)/100

        url = f'http://www.boredapi.com/api/activity?minprice={min}&maxprice={max}'
        response = requests.get(url)
        data = response.json()
        if min > max: 
            print_yellow("\nYour minimum cannot be greater than your maximum")
            continue
        elif not response.ok:
            print_yellow("\nThere was a problem finding an activity try adjusting your range")
            continue
        elif 'error' in data:
            print_yellow("\nThere was a problem finding an activity try adjusting your range")
            continue
        else:
            while True:
                os.system('cls' if os.name == 'nt' else '')
                print()
                url = f'http://www.boredapi.com/api/activity?minprice={min}&maxprice={max}'
                response = requests.get(url)
                data = response.json()
                print_blue(data['activity'])
                print_red(f"This is a {data['type']} activity")
                print_yellow(get_participants(data['participants']))
                print_green(f"And will cost roughly ${data['price']*100}")
                print()
                suprise = choice([True,False,False,False,False])
                if suprise:
                    print_red('\n\n BUT WAIT...')
                    sleep(2)
                    pokemon_appears()

                again = input(f"\nWould you like to see another activity in the price range of ${min*100}-{max*100}: (Y/N) ").lower()
                if again == 'y':
                    continue
                else:
                    break
        again = input("Would you like to try a different price range: (Y/N) ").lower()
        if again == 'y':
            continue
        else:
            break

        
    
                
                
get_activity()



