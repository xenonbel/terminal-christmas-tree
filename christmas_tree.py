from random import randint
from colorama import Fore, init
import os
import sys
import time
import shutil

init(autoreset=True)

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
white = Fore.WHITE
purple = Fore.MAGENTA
cyan = Fore.CYAN
brown = "\033[38;5;52m"

def func():
    symbols = ['*', '.', '+', 'o', 'O', '@', '^', '~', '°', '·', '%',
         '$', '№', '&', '8', '0', '3', '{', '}', '✶', '❄', '❉']
    colors = [red, blue, white, yellow, purple, cyan]
    randnum = randint(0, len(symbols) - 1)

    symbol=symbols[randnum]

    if randint(1, 100) <= 60:
        color_idx = randint(0, len(colors) - 1)
        return f"{colors[color_idx]}{symbol}"
    else:
        return f"{green}{symbol}"


def christmas_tree():

    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write("\033[?25l")

    (cols, lines)=shutil.get_terminal_size()
    n = int((lines * 9) / 10)

    if ((n * 2) > cols):
        n = int(cols/2)
    
    min_height = 15
    max_height = 25

    height = n 
    if height < min_height:
        height = min_height
    elif height > max_height:
        height = max_height

    tree_char = '*'

    try:
        while True:
            start_time = time.perf_counter()
            sys.stdout.write("\033[H")

            star_padding = (cols - 1) // 2
            print(' ' * star_padding + f"{yellow}★")

            for i in range(1, height + 1):
                    current_width = 1 + (i - 1) * 2
                    left_padding = (cols-current_width) // 2

                    if left_padding < 0:
                        left_padding = 0
                
                    line = ' ' * left_padding
                    for _ in range(current_width):
                        if randint(1, 100) <= 50:
                            line += func()
                        else:
                            line += f"{green}{tree_char}"
            
                    print(line)
            
            trunk_width = 10
            trunk_height = 4
            trunk_spaces = (cols - trunk_width) // 2

            for _ in range (trunk_height):
                trunk_line = ' ' * trunk_spaces + f"{brown}{'#' * trunk_width}"
                print(trunk_line)

            text = [ 
                    " _   _                            _   _                __   __                ____   ___ ____   __   _ ",
                    "| | | | __ _ _ __  _ __  _   _   | \ | | _____      __ \ \ / /__  __ _ _ __  |___ \ / _ \___ \ / /_ | |",
                    "| |_| |/ _` | '_ \| '_ \| | | |  |  \| |/ _ \ \ /\ / /  \ V / _ \/ _` | '__|   __) | | | |__) | '_ \| |",
                    "|  _  | (_| | |_) | |_) | |_| |  | |\  |  __/\ V  V /    | |  __/ (_| | |     / __/| |_| / __/| (_) |_|",
                    "|_| |_|\__,_| .__/| .__/ \__, |  |_| \_|\___| \_/\_/     |_|\___|\__,_|_|    |_____|\___/_____|\___/(_)",
                    "            |_|   |_|    |___/                                                                         "
                    ]

            text_padding = (cols - 120) // 2

            if text_padding < 0:
                text_padding = 0

            for line in text:
                print(' ' * text_padding + f"{yellow}" + line)

            end_time = time.perf_counter()
            sleep_time = 0.4 - (end_time - start_time)

            if sleep_time > 0:
                time.sleep(sleep_time)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    christmas_tree()
