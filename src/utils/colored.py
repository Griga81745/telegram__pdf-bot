from colorama import Style, Fore, init
init(autoreset=True); init(wrap=False)


def colored_info(info: str, message: str) -> None:
  print(f'{Fore.WHITE}[{Fore.MAGENTA}{info}{Fore.WHITE}] {Style.BRIGHT}{Fore.GREEN}➜{Style.RESET_ALL} {message}')


def colored_error(message: str) -> None:
  print(f'{Fore.WHITE}[{Fore.MAGENTA}error{Fore.WHITE}] {Style.BRIGHT}{Fore.RED}➜{Style.RESET_ALL} {message}')
