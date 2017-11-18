import os

class color:
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

class UI:
    version = "2.0"

    def __init__(self):
        pass

    def clearscreen(self):
        os.system('clear')

    def banner(self):
        self.clearscreen()
        print("                                                                        ")
        print("\033[91m_____________________  __   _____       ________     _____              ")
        print("___  __ \_  ___/__  / / /   ___(_)____________(_)______  /______________")
        print("__  /_/ /____ \__  /_/ /    __  /__  __ \____  /_  _ \  __/  __ \_  ___/")
        print("_  ____/____/ /_  __  /     _  / _  / / /___  / /  __/ /_ / /_/ /  /    ")
        print("/_/     /____/ /_/ /_/      /_/  /_/ /_/___  /  \___/\__/ \____//_/     ")
        print("                                        /___/                           \033[0m")
        print("\033[94m    PSH injector autoscript       by           OnetTeam  Taroballz      \033[0m")
        print("-----------------------------------------------------------------------------")

    def showmenu(self,options):
        print('\033[1mselect an option:\033[0m',end='\n')
        for option in options:
            print(''.join(['\t\033[94m[+]\033[0m','%s\t----> %s'%option,]))
        else:
            print("----------------------------------------------------------------------------")

    def showoutfilepath(self,outfile):
        print('\033[1mYour output file path is:\033[0m \n\033[92m%s\033[0m'%outfile)
        print("------------------------------------------------------------------------------")

