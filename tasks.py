from invoke import task
import sys
from isis import pathfile, homepath, date, driver
import os
import re
import time
import keyboard
from os import listdir
from os.path import isfile, join
@task
def build(c):
    tata=0
    os.chdir(pathfile)
    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    while tata!=8:
        tata=0
        for fichier in fichiers:
            x=re.search(date, fichier)
            print(date)
            print(fichier)
            if x:
                
                print("ok")
                tata+=1
                print(tata)

        os.chdir(homepath)
        c.run("python code_final.py")
    print("sortit")
    keyboard.press_and_release('Ctrl + c')
    driver.quit()
    sys.exit()
    
        
    

