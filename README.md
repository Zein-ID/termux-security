# termux-security

Help for you


pkg install python2 -y
pkg install nano -y
git clone https://github.com/Zein-ID/termux-security
cd termux-security
cp login.py $HOME
cd
nano login.py

ubah variabel x menjadi username kalian
ubah variabel y menjadi password kalian
Contoh : x = 'Zein-ID'
         y = 'Programmer'

Jika sudah lanjut :

cd ../usr/etc
nano bash.bashrc
tulis : python2 login.py diatas PS1='\$
cd
login

Dan Enjoyyyyyyyyyy
