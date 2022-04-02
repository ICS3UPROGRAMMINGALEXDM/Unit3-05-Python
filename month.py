#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: uses a switch case workaraound to display strings that
# correspond with the user's number
import colorama
from colorama import Fore, Back, Style


def switch_month(month):
    months = {
        1: Fore.BLUE + Style.BRIGHT + "{} represents January".format(month),
        2: Fore.RED + Style.BRIGHT + "{} represents February".format(month),
        3: Fore.GREEN + Style.BRIGHT + "{} represents March".format(month),
        4: Fore.MAGENTA + Style.BRIGHT + "{} represents April".format(month),
        5: Fore.MAGENTA + Style.BRIGHT + "{} represents May".format(month),
        6: Fore.CYAN + Style.BRIGHT + "{} represents June".format(month),
        7: Fore.YELLOW + Style.BRIGHT + "{} represents July".format(month),
        8: Fore.YELLOW + Style.BRIGHT + "{} represents August".format(month),
        9: Fore.GREEN + Style.BRIGHT + "{} represents September".format(month),
        10: Fore.CYAN + Style.BRIGHT + "{} represents October".format(month),
        11: Fore.BLUE + Style.BRIGHT + "{} represents November".format(month),
        12: Fore.RED + Style.BRIGHT + "{} represents December".format(month),
    }
    return months.get(month, "Error {} does not represent a month".format(month))


def main():
    user_month = int(input("Enter your month's number: "))

    print(switch_month(user_month))


if __name__ == "__main__":
    main()
