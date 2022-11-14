import os 
from os import listdir
from os.path import isfile, join
from datetime import date as d
from datetime import timedelta
import time
import re
from os import listdir
from os.path import isfile, join
from delsucces import copyPasteDel
pathfile = "D:\ZABRE\Downloads"



def renomme(service):
    pathfile ="D:\ZABRE\Downloads"
    if service == "momo":
        pathfile = pathfile + "\momo"
    elif service == "evd":
        pathfile = pathfile + "\evd"
    elif service == "smsc":
        pathfile = pathfile + "\smsc"
    os.chdir(pathfile)
    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    for fichier in fichiers:
        x=re.search("^sms.", fichier) 
        if x:
            print(fichier)
            date = fichier[11:19]
            
            jour = fichier[17:19]
           

            file_newname_newfile = os.path.join(pathfile, service+"_del_succes."+date+".csv")
            file_oldname= os.path.join(pathfile, fichier)
            os.rename(file_oldname, file_newname_newfile)
            """
            time.sleep(1)
            s=re.search("^smsc.", fichier)
            print(s)
            e=re.search("^evd.", fichier)
            m=re.search("^momo.", fichier)
            print(fichier)
            
            date = fichier[-8:]
            jour = date[7:9]
            print(date)
            print(jour)
            jour = int(jour)
            line_start_output=jour + 1
            line_end_output=line_start_output + 1
            
            
            if s:
                date = fichier[:]
                jour = date[7:9]
                print(date)
                print(jour)
                jour = int(jour)
                line_start_output=jour + 1
                line_end_output=line_start_output + 1
                copyPasteDel(fichier,"MTN CDI Daily Report1.xls",9,line_start_output,line_end_output,1,7)
            elif m:
                copyPasteDel(fichier,"MTN CDI Daily Report1.xls",9,line_start_output,line_end_output,8,13)
            elif e:
                copyPasteDel(fichier,"MTN CDI Daily Report1.xls",9,line_start_output,line_end_output,14,19)
            """
    return 0

#renomme("smsc")
renomme("evd")  
renomme("momo") 