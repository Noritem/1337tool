#Importent Imports
from pystyle import System
from requests import get
import requests
from os import system
from colorama import Fore, init, Style

#Change The Console Title
mytitle = "1337 - Toolstown"
system("title "+mytitle)



#Only Change This To Your Banner
banner = f"""{Fore.RED}
                        ██╗██████╗ ██████╗ ███████╗    ████████╗ ██████╗  ██████╗ ██╗     
                        ███║╚════██╗╚════██╗╚════██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                        ╚██║ █████╔╝ █████╔╝    ██╔╝       ██║   ██║   ██║██║   ██║██║     
                        ██║ ╚═══██╗ ╚═══██╗   ██╔╝        ██║   ██║   ██║██║   ██║██║     
                        ██║██████╔╝██████╔╝   ██║         ██║   ╚██████╔╝╚██████╔╝███████╗
                        ╚═╝╚═════╝ ╚═════╝    ╚═╝         ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝{Style.RESET_ALL}
                                                {Fore.MAGENTA}By ! Smash#1337{Style.RESET_ALL}                                                                                                                
"""


# for Time Show Like [12:33]
import time
import datetime
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


#Main Menu
def mainanswer():
    System.Clear()
    print(f'{banner}')
    print('\n')
    print(f'                            [1] > {Fore.RED}DC Account Checker{Style.RESET_ALL}          [3] > {Fore.MAGENTA}Nitro Generator{Style.RESET_ALL}')
    print(f'                            [2] > {Fore.RED}IP Lockup{Style.RESET_ALL}                   [4] > {Fore.MAGENTA}Soon{Style.RESET_ALL}')
    print('\n')
    print('\n')



    answer = input('\033[1;00m[\033[91m>\033[1;00m]\033[91m\033[00m Choose : ')
    if answer == '1':
        Maine()
    if answer == '2':
        ip()
    if answer == '3':
        nitro()        
    else:
        print('Incorrect selection, please choose a number')
        mainanswer()

#Nitro Genarator
def nitro():
    import random, string, requests
    System.Clear()
    print(banner)
    print()

    f=open("Valid Nitro.txt", "w", encoding='utf-8')
    
    while True:
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
        if r.status_code == 200:
            print(f"[{update_time()}] {Fore.GREEN}[+{Fore.RESET} discord.gift/{code}")
            f.write(f"discord.gift/{code}\n")
        else:
            print(f"[{update_time()}] {Fore.RED}[-]{Fore.RESET}  discord.gift/{code}")  

#Simple IP Lookup
def ip():
    System.Clear()
    print(banner)
    print()
    ip = input("\nEnter IP > ")

    try:
        getip = requests.get(url = f"https://geo.leadboxer.com/GeoIpEngine/{ip}?jsonp")
        data = getip.json()

        req2 = requests.get(url ="https://stevemorse.org/jcal/proxycode.php?&noCacheIE=1650908121322")
        dat = req2.text
        callback = dat[14:][:7]

        print()
        print(Fore.RED + "Country: " + data['countryName'])
        print(Fore.LIGHTRED_EX + "Continent: " + data['continent'])
        print(Fore.LIGHTCYAN_EX + "Postal Code: " + data['postalCode'])
        print(Fore.CYAN + "Latitude: " + data['latitude'])
        print(Fore.BLUE + "Longitude: " + data['longitude'])
        print(Fore.LIGHTGREEN_EX + "City: " + data['city'])

        lat = data['latitude']
        lon = data['longitude']

        req3 = requests.get(url = f"https://stevemorse.org/jcal/latlonlocal.php?cookie=&hidden=&doextra=&code={callback}&protocol=https%3A&time=1650908121321&addr2latlon=0&address=&city=&state=&zip=&country=US&latlon2addr=1&latitude={lat}4&longitude={lon}")
        source = req3.text

        left = "<br><br><i>MapQuest</i><br>"
        right = "<br><br><br><img src"
        print(Fore.GREEN + "Adress: " + source[source.index(left)+len(left):source.index(right)])
        input("\nPress enter to exit...")
    except:
        print(Fore.LIGHTRED_EX + "\nFailed... Try again !")
        input("\nPress enter to exit...")
    mainanswer()


def MassCheck(combolist):
    System.Clear()
    print(banner)
    print()

    with open(combolist , 'r') as f:
        content = f.read().split('\n')

    File = open("HIT.txt" , 'w')


    for token in content:
        mass = get("https://discordapp.com/api/v9/users/@me?verified", headers={"authorization": token}).status_code

        if mass == 200:
            print(f"[{update_time()}] {Fore.GREEN}[+] {Fore.RESET}{token} ",)
            File.write(token+ '\n')
        if mass == 401:
            print(f"[{update_time()}] {Fore.RED}[-]{Fore.RESET} {token}")

    print()
    System.Clear()
    print(banner)
    print(f"[{update_time()}] {Fore.YELLOW}[+]{Fore.RESET} Checking Finished Valid Token are in HIT.txt")
    print(f"[{update_time()}] {Fore.YELLOW}[~]{Fore.RESET} By Smash#1337 & TeamGambo - Mike#1337")
    mainanswer()

def Maine():
    System.Clear()
    print(banner)
    print()
    combolist = input(f"{Fore.YELLOW}[~] {Fore.RESET}Drag The Path of Your ComboList > ")
    MassCheck(combolist)
    

mainanswer()