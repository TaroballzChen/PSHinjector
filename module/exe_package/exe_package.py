import os

class exe:
    # def __init__(self):
    #     self.path = os.getcwd()
    #     self.toEXE = self.path + "/module/ps1toEXE/"
    #     self.infile = ''
    #     self.filename = input('type exe basename: ')
    #
    #
    # def generate_exe(self):
    #     input('gnome-terminal -- sh -c "cd %s; pwsh ./PS1toEXE.ps1 -inputFile %s -outputFile %s/output/%s.exe -sta -noConsole"'
    #               %(self.toEXE,
    #                 self.infile,
    #                 self.path,
    #                 self.filename,
    #                 ))
    #
    # def run_action(self):
    #     self.generate_exe()

    def __init__(self):
        self.path = os.getcwd()
        self.PS1toexe = 'gnome-terminal -- firefox https://ps2exe.azurewebsites.net/'
        self.infile = ''

    def generate_exe(self):
        if os.path.isfile(self.infile):
            os.system(self.PS1toexe)
            os.system('gnome-terminal -- gedit %s'%self.infile)
        else:
            print('\033[93m\033[1mFile NOT Found Error!!\033[0m\033[0m')

    def run_action(self):
        self.generate_exe()


