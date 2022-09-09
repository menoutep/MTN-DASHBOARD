from invoke import task
import sys
from main_functions import pathfile, homepath, date, driver
import os
import re
import time
import keyboard
from os import listdir
from os.path import isfile, join
@task
def build(c):
    tata=0
    while tata!=8:
        os.chdir(pathfile)
        fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
        tata=0
        for fichier in fichiers:
            x=re.search(date, fichier)
            print(date)
            print(fichier)
            print(x)
            if x: 
                print("ok")
                tata+=1
                print(tata)
            if tata==8:
                c.run("exit()")
                time.sleep(2)
                print("ctl")      
                break
        os.chdir(homepath)
        c.run("python code_final.py")
    c.run("exit()")
    print("sortit")
    #keyboard.press_and_release('Ctrl + c')
    driver.quit()
    c.run("python xml2xls.py")
    time.sleep(20)
    c.run("python dashboard.py")
    sys.exit()
    