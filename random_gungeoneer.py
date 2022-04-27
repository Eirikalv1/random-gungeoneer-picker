from random import uniform
from random import randint
import time
from pyfiglet import figlet_format
import colorama
from colorama import Fore
colorama.init(autoreset=True)

namep = ""
names = ["Convict ", "Hunter ", "Marine ", "Pilot ", "Bullet ", "Paradox ", "Gunslinger ", "Robot "]
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
x = 0.01
i = 0.03
k = 0.03

for l in range(20, randint(40,60)):
    name = names[randint(0,len(names)-1)]
    while name == namep:
        name = names[randint(0,len(names)-1)]
    namep = name
    print("\r" + name, end = ' ', flush=True)
    time.sleep(k)

while True:
    name = names[randint(0,len(names)-1)]
    while name == namep:
        name = names[randint(0,len(names)-1)]
    namep = name
    print("\r" + name, end = ' ', flush=True)
    i += uniform(x, x+0.2*x)
    x = x+(0.2*x)
    time.sleep(i)

    if i >= 0.7:
        name = names[randint(0,len(names)-1)].upper()
        while name == namep:
            name = names[randint(0,len(names)-1)].upper()
        namep = name
        color = colors[randint(0,len(colors)-1)]
        print("\r" + color + figlet_format(name), end = ' ', flush=True)
        if name != "PARADOX ":
            color = colors[randint(0,len(colors)-1)]
            if randint(0,1) == 1:
                print(color + "\nWITH CUSTOM COSTUME")
            else:
                print(color + "\nWITH STANDARD COSTUME")
            if randint(0,1) == 1:
                print(color + "AND CUSTOM GUN")
            else:
                print(color + "AND STANDARD GUN")
        break
