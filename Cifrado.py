#!/usr/bin/python

import sys
import os
import webbrowser
import platform
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def __limpiar():
    if os.name == 'nt':
            os.system('cls')
    else:
            os.system('clear')




def menu():

    __limpiar()
    print '''

                                       
\033[1;33m                         (       (                 (         
\033[1;33m                         )\  (   )\ )  (       )   )\ )      
\033[1;33m                       (((_) )\ (()/(  )(   ( /(  (()/(  (   
\033[1;33m                       )\___((_) /(_))(()\  )(_))  ((_)) )\  
\033[1;33m                      ((/ __|(_)(_) _| ((_)((_)_   _| | ((_) 
\033[1;33m                       | (__ | | |  _|| '_|/ _` |/ _` |/ _ \ 
\033[1;33m                        \___||_| |_|  |_|  \__,_|\__,_|\___/
                                                             
                        \033[1;34m-----------------------------------                    
                        \033[1;34mHecho por:\033[1;m Jey Zeta
                        \033[1;34mVersion:\033[1;m Beta 1.0
                        \033[1;34m-----------------------------------
          '''
    print '''
                        \033[1;32m      +--=[ 1.- Cesar    ]=--+
                        \033[1;32m      +--=[ 2.- Vigenere ]=--+
                        \033[1;32m      +--=[ 3.- About    ]=--+
        '''

    while True:


        d = raw_input("\033[1;35mCifrado > \033[1;m")

        if d == "1":
            subprocess.call(['python','cesar/cesar.py'])
        if d == "2":
            subprocess.call(['python','vigenere/vigenere.py'])
        if d == "3":
            webbrowser.open('https://www.facebook.com/HackingEnVivo/')
            
menu()
