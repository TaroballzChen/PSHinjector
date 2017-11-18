import os
import sys
from core.Menu import Menu
from core.ui import UI
from module.create_operation import operation
from module.msfvenom_create.msfvenom import msfvenom_payload_create
from module.webserver.SimpleServer import webserver
from module.exe_package.exe_package import exe
from module.listener.listener import msflistener
from module.obfuscation.obfuscation import obfuscation_module

if __name__ == '__main__':

    if not os.path.exists('output/'):
        os.mkdir('output')

    if not os.path.exists('temp/'):
        os.mkdir('temp')

    #textfile:
    msfconsole_rc = ""
    payload = ""
    tempfile = ""

    #initialize
    exit_flag = False
    ui = UI()
    menu = Menu()
    #Menu initial
    while not exit_flag:
        ui.banner()
        menu_show = ui.showmenu(menu.options)
        outfileshow = ui.showoutfilepath(payload)
        choice = input('>>>')
        if choice in menu.allowinput:
            if choice == 'sc':
                mod = msfvenom_payload_create()
                msfconsole_rc = mod.msfrc
                mod.run_action()
                tempfile = mod.tempfile
                input('\033[92mplese type ENTER to Continue\033[0m')
            if choice == 'og':
                mod = operation()
                mod.input_tempfile=tempfile
                payload = mod.create_payload()
                input('\033[92mplese type ENTER to Continue\033[0m')
            if choice == 'web':
                mod = webserver()
                input('\033[92mplese type ENTER to Continue\033[0m')
            if choice == 'exe':
                mod = exe()
                mod.infile = payload
                mod.run_action()
            if choice == "msf":
                mod = msflistener()
                mod.values['source'] = msfconsole_rc
                mod.run_action()
            if choice == "ob":
                mod = obfuscation_module()
                mod.run_action()
                input('\033[92mplese type ENTER to Continue\033[0m')
            if choice == 'exit':
                sys.exit()