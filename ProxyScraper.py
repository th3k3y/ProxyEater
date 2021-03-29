#Importing required modules.

import requests
import time
from colorama import Fore, Back, Style, init
init()

#Proxy sources (HTTP).
 
urlH = ("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
url2H = ("https://www.proxyscan.io/download?type=http")
url3H = ("https://multiproxy.org/txt_all/proxy.txt")

#Proxy sources (SOCKS4).

url4S4 = ("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
url5S4 = ("https://www.proxyscan.io/download?type=socks4")

#Proxy sources (SOCKS5).

url6S5 = ("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all")
url7S5 = ("https://www.proxyscan.io/download?type=socks5")

#Defining the logo.

def logo():
	print(Fore.MAGENTA)
	print("""                                             
 _____                 _____     _           
|  _  |___ ___ _ _ _ _|   __|___| |_ ___ ___ 
|   __|  _| . |_'_| | |   __| .'|  _| -_|  _|
|__|  |_| |___|_,_|_  |_____|__,|_| |___|_|  
                  |___|  
""") 
	print(Style.RESET_ALL + "Proxy type (case sensitive): HTTP | SOCKS4 | SOCKS5")
	print("\b")                                                             


#Defining the scraper function.
 
def scraper(HTTP_PROXIES):
    rep = requests.get(HTTP_PROXIES)
    proxies_str = str(rep.content, encoding="utf-8")
    lines = proxies_str.split("\r\n")
    dir_url = r"Proxies.txt"
    file = open(dir_url, "a")
    for line in lines:
        file.write(line + "\n")
    file.close()

#Defining the menu function.

def menu():
	print("--------")
	print("\b")
	type = input("[*]Proxy type = ")
	print("\b")
	if type == "HTTP":
		print("--------")
		scraper(urlH),scraper(url2H),scraper(url3H)
		time.sleep(0.1)
		print("\b")
		print(Fore.YELLOW + "HTTP " + Style.RESET_ALL + "proxies has been saved in Proxies.txt")
		print("\b")
		time.sleep(0.1)
		menu()

	if type == "SOCKS4":
		print("--------")
		print("\b")
		scraper(url4S4),scraper(url5S4)
		time.sleep(0.1)
		print(Fore.YELLOW + "SOCKS4 " + Style.RESET_ALL + "proxies has been saved in Proxies.txt")
		print("\b")
		time.sleep(0.1)
		menu()

	if type == "SOCKS5":
		print("--------")
		print("\b")
		scraper(url6S5),scraper(url7S5)
		time.sleep(0.1)
		print(Fore.YELLOW + "SOCKS5 " + Style.RESET_ALL + "proxies has been saved in roxies.txt")
		print("\b")
		time.sleep(0.1)
		menu()
	else:
		print("--------")
		time.sleep(0.1)
		print("\b")
		print(Fore.RED + "Invalid proxy type." + Style.RESET_ALL)
		print("\b")
		menu()
logo()
menu()

