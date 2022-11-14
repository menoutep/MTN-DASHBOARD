import os
import re 
from appqos import copyPasteApp
from cp_function import copyPaste
from scp import copyBlock,searchcopy
from delsucces import copyPasteDel
from peak import copyPasteTps
from datetime import date as d
from datetime import timedelta
from os import listdir
from os.path import isfile, join
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
ewpmomWise = "ewpmomWise"+date+".xls"
seamlessTraffic="seamlessTraffic"+date+".xls"
seamlessWise = "seamlessWise"+date+".xls"
WAVECITraffic="WAVECITraffic"+date+".xls"
WAVECI2Traffic="WAVECI2Traffic"+date+".xls"
WAVECIWise = "WAVECIWise"+date+".xls"
WAVECI2Wise = "WAVECI2Wise"+date+".xls"
tpsussd = "tpsussd"+date+".xls"
tpsim ="tpsim"+date+".xls"
tpssms="tpssms"+date+".xls"
trafficWise ="trafficWise"+date+".xls"
date_ = re.sub("-","",date)
ussd = "ussdqos" + date + ".xls"
smsc="smsc_del_sucess."+date_+".csv"
evd="evd_del_sucess."+date_+".csv"
momo="momo_del_sucess."+date_+".csv"
statcloud1 = "statscloud_"+date+"_drapp1"
statcloud2 = "statscloud_"+date+"_drapp2"
statcloud3 = "statscloud_"+date+"_drapp3"
statcloud4 = "statscloud_"+date+"_drapp4"
statcloud5 = "statscloud_"+date+"_drapp5"
line_end_input=int(jour)+3
line_end_output=int(jour)+38


copyPaste(p2pTrafficStatistics,0,3,line_end_input,0,1,"MTN CDI Daily Report1.xls",1,38,line_end_output,1,2)#date


copyPaste(p2pTrafficStatistics,0,3,line_end_input,4,5,"MTN CDI Daily Report1.xls",1,38,line_end_output,2,3)#p2P total
copyPaste(p2pTrafficStatistics,0,3,line_end_input,1,2,"MTN CDI Daily Report1.xls",1,38,line_end_output,3,4)
copyPaste(p2pTrafficStatistics,0,3,line_end_input,2,3,"MTN CDI Daily Report1.xls",1,38,line_end_output,4,5)#p2p success
copyPaste(p2pTrafficStatistics,0,3,line_end_input,5,6,"MTN CDI Daily Report1.xls",1,38,line_end_output,5,6)##p2p failure
    ##p2p success without exclusion




copyPaste(a2pTrafficStatistics,0,3,line_end_input,4,5,"MTN CDI Daily Report1.xls",1,38,line_end_output,7,8)#date#p2P total
copyPaste(a2pTrafficStatistics,0,3,line_end_input,1,2,"MTN CDI Daily Report1.xls",1,38,line_end_output,8,9)
copyPaste(a2pTrafficStatistics,0,3,line_end_input,2,3,"MTN CDI Daily Report1.xls",1,38,line_end_output,9,10)#p2p success
copyPaste(a2pTrafficStatistics,0,3,line_end_input,5,6,"MTN CDI Daily Report1.xls",1,38,line_end_output,10,11)##p2p failure
    ##p2p success without exclusion


copyPaste(p2aTrafficStatistics,0,3,line_end_input,4,5,"MTN CDI Daily Report1.xls",1,38,line_end_output,12,13)#date#p2P total
copyPaste(p2aTrafficStatistics,0,3,line_end_input,1,2,"MTN CDI Daily Report1.xls",1,38,line_end_output,13,14)
copyPaste(p2aTrafficStatistics,0,3,line_end_input,2,3,"MTN CDI Daily Report1.xls",1,38,line_end_output,14,15)#p2p success
copyPaste(p2aTrafficStatistics,0,3,line_end_input,5,6,"MTN CDI Daily Report1.xls",1,38,line_end_output,15,16)##p2p failure
    ##p2p success without exclusion



line_end_input=int(jour)+5

copyPaste(trafficWise,0,5,line_end_input,5,6,"MTN CDI Daily Report1.xls",1,38,line_end_output,6,7)#p2pwise
copyPaste(trafficWise,0,5,line_end_input,9,10,"MTN CDI Daily Report1.xls",1,38,line_end_output,16,17)#a2pwise
copyPaste(trafficWise,0,5,line_end_input,13,14,"MTN CDI Daily Report1.xls",1,38,line_end_output,11,12)#p2awise

#######epwmom et seamless#####
line_end_input=int(jour)+4
line_end_output=int(jour)+2 
copyPaste(ewpmomTraffic,0,4,line_end_input,0,1,"MTN CDI Daily Report1.xls",2,2,line_end_output,0,1)#date
copyPaste(ewpmomTraffic,0,4,line_end_input,9,10,"MTN CDI Daily Report1.xls",2,2,line_end_output,1,2)#date#p2P total
copyPaste(ewpmomTraffic,0,4,line_end_input,6,7,"MTN CDI Daily Report1.xls",2,2,line_end_output,2,3)
copyPaste(ewpmomTraffic,0,4,line_end_input,8,9,"MTN CDI Daily Report1.xls",2,2,line_end_output,3,4)#p2p success
copyPaste(ewpmomTraffic,0,4,line_end_input,10,11,"MTN CDI Daily Report1.xls",2,2,line_end_output,4,5)##p2p failure

line_end_input=int(jour)+5
copyPaste(ewpmomWise,0,5,line_end_input,6,7,"MTN CDI Daily Report1.xls",2,2,line_end_output,5,6)##p2p success without exclusion


line_end_input=int(jour)+4

try:
    copyPaste(seamlessTraffic,0,4,line_end_input,0,1,"MTN CDI Daily Report1.xls",3,2,line_end_output,0,1)#date
    copyPaste(seamlessTraffic,0,4,line_end_input,9,10,"MTN CDI Daily Report1.xls",3,2,line_end_output,1,2)#date#p2P total
    copyPaste(seamlessTraffic,0,4,line_end_input,6,7,"MTN CDI Daily Report1.xls",3,2,line_end_output,2,3)
    copyPaste(seamlessTraffic,0,4,line_end_input,8,9,"MTN CDI Daily Report1.xls",3,2,line_end_output,3,4)#p2p success
    copyPaste(seamlessTraffic,0,4,line_end_input,10,11,"MTN CDI Daily Report1.xls",3,2,line_end_output,4,5)##p2p failure
except:
    print("quelque chose c'est mal passer au moment de copier les info de seamlesstraffic dans le MTN DAILY REPORT")
line_end_input=int(jour)+5

try:
    copyPaste(seamlessWise,0,5,line_end_input,6,7,"MTN CDI Daily Report1.xls",3,2,line_end_output,5,6)#p2p success without exclusion
except:
    print("quelque chose c'est mal passer au moment de copier les info de seamlessWise dans le MTN DAILY REPORT")

line_end_input=int(jour)+3
line_end_output=int(jour)+2 
copyPaste(WAVECITraffic,0,4,line_end_input,0,1,"MTN CDI Daily Report1.xls",7,2,line_end_output,0,1)
copyPaste(WAVECITraffic,0,4,line_end_input,9,10,"MTN CDI Daily Report1.xls",7,2,line_end_output,1,2)#date#p2P total
copyPaste(WAVECITraffic,0,4,line_end_input,6,7,"MTN CDI Daily Report1.xls",7,2,line_end_output,2,3)
copyPaste(WAVECITraffic,0,4,line_end_input,8,9,"MTN CDI Daily Report1.xls",7,2,line_end_output,3,4)#p2p success
copyPaste(WAVECITraffic,0,4,line_end_input,10,11,"MTN CDI Daily Report1.xls",7,2,line_end_output,4,5)
line_end_input=int(jour)+4
copyPaste(WAVECIWise,0,5,line_end_input,6,7,"MTN CDI Daily Report1.xls",7,2,line_end_output,5,6)##p2p success without exclusion
line_end_input=int(jour)+4
line_end_output=int(jour)+2 
copyPaste(WAVECI2Traffic,0,4,line_end_input,0,1,"MTN CDI Daily Report1.xls",7,2,line_end_output,7,8)
copyPaste(WAVECI2Traffic,0,4,line_end_input,9,10,"MTN CDI Daily Report1.xls",7,2,line_end_output,8,9)#date#p2P total
copyPaste(WAVECI2Traffic,0,4,line_end_input,6,7,"MTN CDI Daily Report1.xls",7,2,line_end_output,9,10)
copyPaste(WAVECI2Traffic,0,4,line_end_input,8,9,"MTN CDI Daily Report1.xls",7,2,line_end_output,10,11)#p2p success
copyPaste(WAVECI2Traffic,0,4,line_end_input,10,11,"MTN CDI Daily Report1.xls",7,2,line_end_output,11,12)
line_end_input=int(jour)+5
copyPaste(WAVECI2Wise,0,5,line_end_input,6,7,"MTN CDI Daily Report1.xls",7,2,line_end_output,12,13)

searchcopy(ussd,0,"MTN CDI Daily Report1.xls")
copyBlock(ussd,0,"MTN CDI Daily Report1.xls")
jour=int(jour)
line_end_output=jour + 6
copyPasteTps(tpssms,"MTN CDI Daily Report1.xls",1,5,line_end_output,8,9)
copyPasteTps(tpsussd,"MTN CDI Daily Report1.xls",1,5,line_end_output,9,10)
copyPasteTps(tpsim,"MTN CDI Daily Report1.xls",1,5,line_end_output,10,11)

######################del_succes######################""




pathfile="D:\ZABRE\Downloads\smsc"
os.chdir(pathfile)
fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
for fichier in fichiers:
    x=re.search("^smsc.", fichier) 
    if x:
        print(fichier)
        date=fichier[16:24]
        print(date)
        
        jour=date[6:]
        print(jour)
        jour=int(jour)
        line_start_output=jour + 1
        line_end_output=line_start_output + 1
        
        copyPasteDel(fichier,"MTN CDI Daily Report1.xls",9,line_start_output,line_end_output,1,7)
pathfile="D:\ZABRE\Downloads\evd"
os.chdir(pathfile)
fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
for fichier in fichiers:
    x=re.search("^evd.", fichier) 
    if x:
        print(fichier)
        date=fichier[15:23]
        print(date)
        
        jour=date[6:]
        print(jour)
        jour=int(jour)
        line_start_output=jour + 1
        line_end_output=line_start_output + 1
        copyPasteDel(fichier,"MTN CDI Daily Report1.xls",9,line_start_output,line_end_output,8,13)
pathfile="D:\ZABRE\Downloads\momo"
os.chdir(pathfile)
print(os.getcwd())
fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
for fichier in fichiers:
    x=re.search("^momo.", fichier) 
    if x:
        print(fichier)
        date=fichier[16:24]
        print(date)
        
        jour=date[6:]
        print(jour)
        jour=int(jour)
        line_start_output=jour + 1
        line_end_output=line_start_output + 1
        copyPasteDel(fichier,"MTN CDI Daily Report1.xls",9,line_start_output,line_end_output,14,19)    


########################app############################################
pathfile="D:\ZABRE\Downloads"
os.chdir(pathfile)

fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
for fichier in fichiers:
    x=re.search("^statscloud.", fichier) 
    if x:
        print(fichier)
        date=fichier[11:21]
        print(date)
        
        jour=fichier[19:21]
        print(jour)
        jour=int(jour)
        line_start_output=jour + 4
        line_end_output=line_start_output + 1
        numapp=fichier[27]
        print(numapp)
        if numapp == "1":
            copyPasteApp(fichier,"MTN CDI Daily Report1.xls",1,line_start_output,line_end_output,2,3)
        elif numapp == "2":
            copyPasteApp(fichier,"MTN CDI Daily Report1.xls",1,line_start_output,line_end_output,3,4)
        elif numapp == "3":
            copyPasteApp(fichier,"MTN CDI Daily Report1.xls",1,line_start_output,line_end_output,4,5)
        elif numapp =="4":   
            copyPasteApp(fichier,"MTN CDI Daily Report1.xls",1,line_start_output,line_end_output,5,6)
        elif numapp =="5":
            copyPasteApp(fichier,"MTN CDI Daily Report1.xls",1,line_start_output,line_end_output,6,7)
