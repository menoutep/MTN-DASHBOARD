import os
from cp_function import copyPaste

from datetime import date as d
from datetime import timedelta

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
seamlessWise = "seamlessWise"+date+".xls"
trafficWise ="trafficWise"+date+".xls"
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

