class Menu:
    def __init__(self):
        self.options = []
        self.options.append(('sc', 'msf payload for powershell format create'))
        self.options.append(('og', 'merge psh_format file to output_file'))
        self.options.append(('ob', 'obfucate the payload'))
        self.options.append(('exe', 'Output exe file'))
        self.options.append(('msf', 'start listener with msf'))
        self.options.append(('web',"Python SimpleHttpServer"))
        self.options.append(('exit','exit'))
        self.allowinput=[option[0] for option in self.options]
