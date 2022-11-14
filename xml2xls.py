from xlrd import open_workbook 
import xlwt
import os
from datetime import date as d
from datetime import timedelta
from xlutils.copy import copy
import xml.etree.ElementTree as ET
from xlwt import Worksheet

pathfile = "D:\ZABRE\Downloads"
os.chdir(pathfile)

def convertxml(file_input,file_output):      
    tree = ET.parse(file_input)
    root = tree.getroot()
    root=root[0][0]
    wb= xlwt.Workbook()
    sheet = wb.add_sheet('feuille1')
    wb.save(file_output)
    wb=open_workbook(file_output)
    
    wb_=copy(wb)
    sheet=wb_.get_sheet(0)
    i=0
    for childs in root:
        i+=1  
        j=0
        for child in childs:
            j+=1
            text=child.text
            child=" ".join(text.split())            
            Worksheet.write(sheet,i,j,text)
    wb_.save(file_output)

pathfile = "D:\ZABRE\Downloads"
os.chdir(pathfile)
####################gestion des dates#############
today = d.today()
yesterday = today - timedelta(days = 1)
date = yesterday
date=str(date)
date_start = date[0:8]+"01 00"
jour = date[8:10]

if len(jour)==1:
    jour = "0"+jour
date_end = date[0:8]+jour+" 23"

v_an = date[0:4]
p2pTrafficStatistics="p2pTrafficStatistics"+date+".xls"
a2pTrafficStatistics="a2pTrafficStatistics"+date+".xls"
p2aTrafficStatistics="p2pTrafficStatistics"+date+".xls"
ewpmomTraffic="ewpmomTraffic"+date+".xls"
seamlessTraffic="seamlessTraffic"+date+".xls"

ewpmomWise = "ewpmomWise"+date+".xls"

try: 
    ewpmomWise=convertxml(ewpmomWise,ewpmomWise)
except:
    print("quelque chose c'est mal passé au moment de convertir le ewpmomWise en xls")

seamlessWise="seamlessWise"+date+".xls" 
 
try: 
    seamlessWise=convertxml(seamlessWise,seamlessWise)
except:
    print("quelque chose c'est mal passé au moment de convertir le seamlessWise en xls")
 

trafficWise ="trafficWise"+date+".xls"
try: 
    trafficWise=convertxml(trafficWise,trafficWise)
except:
    print("quelque chose c'est mal passé au moment de convertir le trafficWiseWise en xls")

WAVECIWise = "WAVECIWise"+date+".xls"

try: 
    WAVECIWise=convertxml(WAVECIWise,WAVECIWise)
except:
    print("quelque chose c'est mal passé au moment de convertir le WAVECIWise en xls")

WAVECI2Wise="WAVECI2Wise"+date+".xls" 
 
try: 
    WAVECI2Wise=convertxml(WAVECI2Wise,WAVECI2Wise)
except:
    print("quelque chose c'est mal passé au moment de convertir le WAVECI2Wise en xls")
 