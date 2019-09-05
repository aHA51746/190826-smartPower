import subprocess
import re
import os
import time


class SmartPower():

    def __init__(self):
        self.count = 0

    def getState(self,ip):
        p = subprocess.Popen(['ping.exe', ip, '-w', '1', '-n', '3'],
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                shell = True)
        out = p.stdout.read().decode('gbk')
        loss  = re.search('\w*%\w*', out)[0]
        return loss

    def shutDown(self):
        os.system('shutdown -s')

    def run(self):
        ip = '192.168.123.1'
        print('start smart_Power')
        print(time.asctime( time.localtime(time.time() ) ) )
        print()
        while True:
            if self.count >10:
                self.shutDown()
                print('This computer will shutdown in 1min.')
                break
            loss =  self.getState(ip)
            if loss == '100%':
                self.count += 1
                print('lost connect,%d times.' %self.count)
                print(time.asctime( time.localtime(time.time() ) ) )
            elif self.count >0:
                self.count = 0
                print('connect success')
                print()
            time.sleep(60)

    def main(self):
        self.run()

if __name__ == "__main__":
     s1 = SmartPower()
     s1.run()
                             

