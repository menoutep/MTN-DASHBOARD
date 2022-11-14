from invoke import task
import sys
from main_functions import pathfile, homepath, date, driver
import os
import re
import time

from os import listdir
from os.path import isfile, join
@task
def build(c):
    tata=0
    while tata!=16:
        os.chdir(pathfile)
        fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
        tata=0
        for fichier in fichiers:
            x=re.search(date, fichier)
            print(date)
            print(fichier)
            print(x)
            if x: 
                
                tata+=1
                print(tata)
           
        os.chdir(homepath)
       
        c.run("python code_final.py")
    
    driver.quit()
    c.run("python fic_vas.py")
    c.run("python xml2xls.py")
    
    time.sleep(20)
    c.run("python renomage.py")
    time.slepp(5)
    c.run("python dashboard.py")
    
    sys.exit()