import threading
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

processes = int(input(f'{bcolors.OKCYAN}NUM PROCESSES: {bcolors.ENDC}'))


def ping():
    while True:
        try:
            os.system(f'ping localhost -l 65500')
        except Exception as e:
            print(f'{bcolors.FAIL}{e}{bcolors.ENDC}')


for i in range(0, processes):
    try:
        threading.Thread(target=ping).start()
        print(f'{bcolors.OKGREEN}STARTING THREAD {i + 1}{bcolors.ENDC}')
    except:
        print(f'{bcolors.FAIL}ERROR STARTING THREAD {i + 1}{bcolors.ENDC}')
