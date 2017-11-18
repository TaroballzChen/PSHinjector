import os
import shutil

class obfuscation_module:
    def __init__(self):
        self.pwd = os.getcwd()
        self.obf_module_path = './module/obfuscation/Invoke-Obfuscation'
        self.obfuscation_command = './powershell -c \"Import-Module ./Invoke-Obfuscation.psd1;Invoke-Obfuscation\"'
        if os.path.isdir(self.obf_module_path):
            self.renewchoice = input("Do you want to renew DBO's Invoke-Obfuscation project from github(Y/n)")
            if self.renewchoice == 'Y' or self.renewchoice == 'y' or self.renewchoice == '':
                shutil.rmtree('./module/obfuscation/Invoke-Obfuscation')
                self.download_requirement()
                print('\033[92m' + '[*]' + '\033[0m'+'Update obf_module sucessfully !!')
            else:
                pass
        else:
            self.download_choice = input("Do you want to download DBO's Invoke-Obfuscation project from github(Y/n)")
            if self.download_choice == 'Y' or self.renewchoice == 'y' or self.renewchoice == '':
                os.system('gnome-terminal -- sh -c "cd ./module/obfuscation;git clone https://github.com/danielbohannon/Invoke-Obfuscation.git"')
                self.download_requirement()
                print('\033[92m' + '[*]' + '\033[0m'+'Download obf_module sucessfully !!')
            else:
                pass

    def download_requirement(self):
        os.system('gnome-terminal -- sh -c "cd ./module/obfuscation;git clone https://github.com/danielbohannon/Invoke-Obfuscation.git"')
        os.system('wget https://github.com/PowerShell/PowerShell/releases/download/v6.0.0-beta.9/powershell-6.0.0-beta.9-x86_64.AppImage')
        os.system('chmod a+x powershell-6.0.0-beta.9-x86_64.AppImage')
        shutil.move('./powershell-6.0.0-beta.9-x86_64.AppImage','%s/powershell' % self.obf_module_path)

    def run_action(self):
        if os.path.isdir(self.obf_module_path):
            print('\033[93m\033[1mPlease set obf_outfile path as same as origin_file path\033[0m\033[0m')
            os.chdir(self.obf_module_path)
            os.system('gnome-terminal -- %s'%self.obfuscation_command)
            os.chdir(self.pwd)
        else:
            pass