# coding=utf-8
# Fitur :- Anti CTRL + C
#        - Hide Password

from os import system as anonk
import getpass as gp
import sys,time

G = '\x1b[0;32m'
GL = '\x1b[32;1m'
B = '\x1b[0;36m'
P = '\x1b[35;1m'
BL = '\x1b[36;1m'
R = '\x1b[31;1m'
W = '\x1b[37;1m'
H = '\x1b[30;1m'
Y = '\x1b[33;1m'
YL = '\x1b[1;33m'

def load():
   titit = [
    '    ', ' .  ', ' .. ', ' ...', ' .. ', ' .  ', '    ']
   for o in titit:
      print '\r\x1b[36;1m[\x1b[37;1m+\x1b[36;1m]\x1b[31;1m Sedang Mengecek' + str(o),
      sys.stdout.flush()
      time.sleep(0.7)

def unotresei():
    uno = [
     '\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19','           ','\x1b[31;1mUNOTRESEI\x1b[37;1m19']
    for i in uno:
      print '\r\x1b[32;1m              CREATED BY  ' + str(i),
      sys.stdout.flush()
      time.sleep(0.10)



def polo(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10.0 / 100)

logo = '''\x1b[37;1m

           ███        ▄████████  ▄█       
       ▀█████████▄   ███    ███ ███       
          ▀███▀▀██   ███    █▀  ███       
           ███   ▀   ███        ███       
           ███     ▀███████████ ███       
           ███              ███ ███       
           ███        ▄█    ███ ███▌    ▄ 
          ▄████▀    ▄████████▀  █████▄▄██ \x1b[1;33mv3
\x1b[36;1m
               TERMUX SECURITY LOGIN
'''

#yang diubah cuma ini jangan yang lain
x = 'Username'
y = 'Password'


def main():
    try:
       anonk('clear')
       print logo
       unotresei()
       user = raw_input('\n\n{}[{}+{}]{} Username : {}'.format(BL,W,BL,GL,W))
       pasw = gp.getpass('{}[{}+{}]{} Password : {}'.format(BL,W,BL,GL,W))
       load()
       if user == x and pasw == y:
           print '{}\nLogin Succes {}✓'.format(W,GL)
           time.sleep(5)
       else:
           print '{}\nLogin Gagal {}x'.format(W,R)
           time.sleep(2)
           main()
    except KeyboardInterrupt:
           main()


if __name__ == '__main__':
        main()
