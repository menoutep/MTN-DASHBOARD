import os
import pandas as pd

import re       
from os import listdir
from os.path import isfile, join
print(os.getcwd())


def renomme(service):
    pathfile="D:\zabre"
    if service =="momo":
        pathfile = pathfile+"\momo"
    elif service == "smsc":
        pathfile = pathfile+"\smsc"
    elif service == "evd":
        pathfile = pathfile+"\evd"
    os.chdir(pathfile)

    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    for fichier in fichiers:
        x=re.search("^sms.", fichier) 
        if x:
            print(fichier)
            date = fichier[15:23]
            print(date)
            jour = fichier[21:23]
            print(jour)
            file_newname_newfile = os.path.join(pathfile, service+"_del_succes."+date+".csv")
            print(file_newname_newfile)
            file_oldname= os.path.join(pathfile, fichier)
            os.rename(file_oldname, file_newname_newfile)
    #os.chdir(homepath)
    return 0
renomme("momo")