import os 
import os 
from xlrd import open_workbook 
from xlutils.copy import copy
from xlwt.Worksheet import Worksheet

import subprocess
import re
from datetime import date as d
from datetime import timedelta


pathfile = "D:\ZABRE\Downloads"##changer par les chemins correspondant sur la machine qui execute le script
homepath=os.getcwd()

os.chdir(pathfile)
def copyOne(filename):
    print(filename)
    print("tott")
    file = open(filename, "r")
    qos=0
    for line in file:
        # cette ligne permet d'afficher chaque ligne du fichier texte si vous ne desiserz pas afficher le fichier texte, supprimez simplement cette ligne  
        
        x=re.search("DAILY QoS", line) 
        if x:
            date=filename[11:21]
            print(date)
            qos = re.sub(date+" DAILY QoS: ","",line)
            print(qos)
        
        
    file.close()
    return qos
def colle(file,num_sheet,start_r,end_r,start_col,end_col,copie_):
    wb=open_workbook(file,formatting_info=True)
    wb_cp=copy(wb)
    sheet_cp=wb_cp.get_sheet(num_sheet)
    i=0
    try:
        for a_ in range(start_r,end_r):
            for b_ in range(start_col,end_col):
                cell=copie_
                Worksheet.write(sheet_cp,a_,b_,cell)
                        
                i+=1
    except:
        print("...")

    wb_cp.save(file)
  
    return 0
def copyPasteApp(file_input,file,num_sheet,start_r,end_r,start_col,end_col):
    xx=copyOne(file_input)
    
    colle(file,num_sheet,start_r,end_r,start_col,end_col,xx)

"""  
statcloud1 = "statscloud_"+date+"_drapp1"
statcloud2 = "statscloud_"+date+"_drapp2"
statcloud3 = "statscloud_"+date+"_drapp3"
statcloud4 = "statscloud_"+date+"_drapp4"
statcloud5 = "statscloud_"+date+"_drapp5"
file_output ="MTN CDI Daily Report1"
jour = date[8:10]
jour=int(jour)
line_start_output=jour + 4
line_end_output=line_start_output + 1
copyPasteApp(statcloud1,"MTN CDI Daily Report1.xls",1,line_start_output,line_end_output,2,3)
copyPasteApp(statcloud2,"MTN CDI Daily Report1.xls",1,line_start_output,line_end_output,3,4)
copyPasteApp(statcloud3,"MTN CDI Daily Report1.xls",1,line_start_output,line_end_output,4,5)
copyPasteApp(statcloud4,"MTN CDI Daily Report1.xls",1,line_start_output,line_end_output,5,6)
copyPasteApp(statcloud5,"MTN CDI Daily Report1.xls",1,line_start_output,line_end_output,6,7)

"""



