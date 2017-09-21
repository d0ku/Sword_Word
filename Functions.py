import os

def clear_screen():
    if os.name == 'posix':
        os.system("clear")
    elif os.name == 'nt':
        os.system("cls")

def return_all_dictionaries(location):
    temp=os.listdir(location)

    dictionaries=list(filter(lambda x: ".txt" in x,temp))

    for x in dictionaries:
        temp.remove(x)
    temporal=[]
    for x in temp:
        temporal=return_all_dictionaries(location+"/"+x)
        for y in temporal:
            dictionaries.append(x+"/"+y)
        temporal=[]

    return dictionaries

class Colors:
    if os.name == 'posix':
        HEADER = '\033[95m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        ENDCOLOR = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    if os.name=='nt':
        HEADER = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        ENDCOLOR = ''
        BOLD = ''
        UNDERLINE = ''

