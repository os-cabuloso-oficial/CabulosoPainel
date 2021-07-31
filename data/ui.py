import os, sys, time
from colorama import Fore, Style
from random import choice
clean=('cls' if os.name == 'nt' else 'clear')
C= "\033[97;1m"
G = "\033[92;1m"
P = "\033[1;35m"
result=f'''{P}\n________           _________       ___.         .__                      
\_____  \   ______ \_   ___ \_____ \_ |__  __ __|  |   ____  __________  
 /   |   \ /  ___/ /    \  \/\__  \ | __ \|  |  \  |  /  _ \/  ___/  _ \ 
/    |    \\___ \  \     \____/ __ \| \_\ \  |  /  |_(  <_> )___ (  <_> )
\_______  /____  >  \______  (____  /___  /____/|____/\____/____  >____/ 
        \/     \/          \/     \/    \/                      \/       '''
def banner():
    cor = [Fore.RED]
    banner = r"""
====================
☯️ - Painel Privado dos Cabuloso! ☯️
===================="""
    n = 0
    for char in banner:
        sys.stdout.write(f"{choice(cor)}{char}{Style.RESET_ALL}")
        sys.stdout.flush()
        n +=1
        time.sleep(0.007)

def clear():
	os.system(clean)

def menu(ms0):
	clear();banner();print(result+ms0)
	return input(f'\n{C}===> {P}')

def error():
	text='Caractere(s) não reconhecido(s)';clear();banner();print(f'\n{C}====================\n[{P}Error!{C}] {text}\n====================');time.sleep(3)
	
def dialog1():
	clear();banner();print(result)
	return input(f'\n{C}===> {P}')

def dialog2(msg):
	clear();banner()
	return input(f'{result}\n{C}====================\n{msg}\n====================\n{C}{G}Deseja fazer uma nova consulta?\n{C}[{G}1{C}] Sim\n[{G}2{C}] Nao\n===> {P}')
