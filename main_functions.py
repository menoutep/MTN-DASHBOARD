from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 
import os
import keyboard
import re       
from os import listdir
from os.path import isfile, join
from datetime import date as d
from datetime import timedelta


####################gestion des dates#############
today = d.today()
yesterday = today - timedelta(days = 1)
#date = time.strftime('%Y-%m-%d')
date = yesterday
date=str(date)
date_start = date[0:8]+"01 00"
jour = date[8:10]

if len(jour)==1:
    jour = "0"+jour
date_end = date[0:8]+jour+" 23"

v_an = date[0:4]
v_mois =date[5:7]
v_moiss=int(v_mois)
v_moiss=v_moiss-1
v_moiss=str(v_moiss)
p2pTrafficStatistics="p2pTrafficStatistics"+date+".xls"
a2pTrafficStatistics="a2pTrafficStatistics"+date+".xls"
p2aTrafficStatistics="p2pTrafficStatistics"+date+".xls"
epwmomTraffic="epwmomTraffic"+date+".xls"
seamlessTraffic="seamessTraffic"+date+".xls"
#####################fin gestion des dates #####################

###########chargement des differnts chemins utiliser dans le scipt ######################""
pathfile = "D:\ZABRE\Downloads"##changer par les chemins correspondant sur la machine qui execute le script
homepath=os.getcwd()
###########fin du chargement des chemins ##########################

#############chargement de l'instance driver #################""
s=Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://10.18.63.135:9090/im/getDashBoardData")
################fin du chargement d driver################



def accountWise(service):
    driver.find_element_by_link_text('Reports').click()
    time.sleep(5)
    #driver.find_element_by_link_text('Date Wise Report').click()
    driver.find_element_by_link_text('Date Wise Report').click()
    time.sleep(5)
    inp_start=driver.find_element_by_xpath("//*[@id='fromDate']")
    inp_start.send_keys(date_start)
    for i in range(50):
        inp_start.send_keys('\ue003')
    inp_start.send_keys(date_start)
    keyboard.press_and_release('tab')
    time.sleep(5)
    inp_end=driver.find_element_by_xpath("//*[@id='toDate']")
    inp_end.send_keys(date_end)
    for i in range(50):
        inp_end.send_keys('\ue003')
    inp_end.send_keys(date_end)
    keyboard.press_and_release('tab')
    driver.find_element_by_xpath("//*[@id='reportType']").click()
    driver.find_element_by_xpath("//*[@id='reportType']/option[2]").click()
    driver.find_element_by_id("messageType-3").click()
    box=driver.find_element_by_id("esmeAccounts")
    box.click()
    time.sleep(5)
    action__ = webdriver.ActionChains(driver)
    if service == "ewpmom":
        action__.move_to_element(driver.find_element_by_xpath("//*[@id='esmeAccounts']/option[@value='220']"))
        action__.click()
        action__.perform()
    elif service == "seamless":
        action__.move_to_element(driver.find_element_by_xpath("//*[@id='esmeAccounts']/option[@value='783']"))
        action__.click()
        action__.perform()       
    #for i in range(250):
        #box.send_keys('\ue015')
    #driver.find_element_by_xpath("//*[@id='esmeAccounts']/option[20]").click()
    time.sleep(5)
    driver.find_element_by_id("statsType-1").click()
    driver.find_element_by_id("statsType-2").click()
    driver.find_element_by_id("search").click()
    time.sleep(5)																																										

    driver.find_element_by_xpath("//*[@id='btnExport']").click()
    time.sleep(5)
    driver.switch_to.default_content()
    time.sleep(5)
    homepage=driver.find_element_by_xpath("//*[@id='header']/div[1]/a")    
    homepage.click()
    os.chdir(pathfile)
    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    for fichier in fichiers:
        x=re.search("^dateWiseReport.", fichier) 
        if x:
            print(fichier)
            file_newname_newfile = os.path.join(pathfile, service+"Wise"+date+".xls")
            file_oldname= os.path.join(pathfile, fichier)
            os.rename(file_oldname, file_newname_newfile)
    os.chdir(homepath)
    return 0


def wisetraffic():
    driver.find_element_by_link_text('Reports').click()
    time.sleep(3)
    driver.find_element_by_link_text('Date Wise Report').click()
    inp_start=driver.find_element_by_xpath("//*[@id='fromDate']")
    inp_start.send_keys(date_start)
    for i in range(50):
        inp_start.send_keys('\ue003')
    inp_start.send_keys(date_start)
    keyboard.press_and_release('tab')
    time.sleep(3)
    inp_end=driver.find_element_by_xpath("//*[@id='toDate']")
    inp_end.send_keys(date_end)
    for i in range(50):
        inp_end.send_keys('\ue003')
    inp_end.send_keys(date_end)
    keyboard.press_and_release('tab')
    driver.find_element_by_xpath("//*[@id='reportType']").click()
    driver.find_element_by_xpath("//*[@id='reportType']/option[5]").click()

    driver.find_element_by_id("messageType-1").click()
    driver.find_element_by_id("messageType-2").click()
    driver.find_element_by_id("messageType-3").click()
    driver.find_element_by_id("statsType-1").click()
    driver.find_element_by_id("statsType-2").click()
    driver.find_element_by_id("search").click()
    time.sleep(5)																																										

    driver.find_element_by_xpath("//*[@id='btnExport']").click()
    time.sleep(4)
    driver.switch_to.default_content()
    time.sleep(1)
    homepage=driver.find_element_by_xpath("//*[@id='header']/div[1]/a")    
    homepage.click()
    os.chdir(pathfile)
    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    for fichier in fichiers:
        x=re.search("^dateWiseReport.", fichier) 
        if x:
            print(fichier)
            file_newname_newfile = os.path.join(pathfile,"trafficWise"+date+".xls")
            file_oldname= os.path.join(pathfile, fichier)
            os.rename(file_oldname, file_newname_newfile)
    os.chdir(homepath)

    return 0

 
def kara(service):
    driver.find_element_by_link_text('Reports').click()
    time.sleep(5)
    driver.find_element_by_link_text('Account Statistics').click()
    time.sleep(5)
    container_frame = driver.find_element_by_xpath("//iframe")
    driver.switch_to.frame(container_frame)
    time.sleep(5)
    lien_date=driver.find_element_by_xpath("/html/body/div[2]/form/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/div[1]/a")
    lien_date.click()
    time.sleep(5)
    driver.switch_to.default_content()
    time.sleep(5)
    container_frame = driver.find_element_by_xpath("//iframe")
    driver.switch_to.frame(container_frame)
    input_date_1 = driver.find_element_by_id("fromDate")
    input_date_1.send_keys(date)

    input_date_2 = driver.find_element_by_id("toDate")
    input_date_2.send_keys(date)
    submit_date = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/table/tbody/tr/td/table/tbody/tr[6]/td/table[2]/tbody/tr/th[2]/div/input")
    submit_date.click()
    time.sleep(5)
    driver.switch_to.default_content()
    time.sleep(5)
    container_frame = driver.find_element_by_xpath("//iframe")
    driver.switch_to.frame(container_frame)
    time.sleep(5)
    presence=driver.find_elements_by_link_text(service)
    next_button = driver.find_element_by_xpath("//*[@id='nextEnabled']")
#next_button = driver.find_element_by_xpath("//*[@id='nextEnabled']")
    while len(presence) !=1:
       
        next_button = driver.find_element_by_xpath("//*[@id='nextEnabled']")
        next_button.click()
        time.sleep(5)
        presence=driver.find_elements_by_link_text(service)

    ewpmom = driver.find_element_by_link_text(service)
    ewpmom.click()
    time.sleep(5)
    print("ouverture pour MoMo")
    driver.switch_to.default_content()
    time.sleep(5)
    container_frame = driver.find_element_by_xpath("//iframe")
    driver.switch_to.frame(container_frame)
    driver.find_element_by_link_text(v_an).click()
    time.sleep(5)
    driver.switch_to.default_content()
    time.sleep(5)
    container_frame = driver.find_element_by_xpath("//iframe")
    driver.switch_to.frame(container_frame)
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='__bookmark_3']/tbody/tr["+v_moiss+"]/td[1]/div/a").click()
    #//*[@id="__bookmark_3"]/tbody/tr[7]/td[1]/div/a
    #//*[@id="__bookmark_3"]/tbody/tr[8]/td[1]/div/a
    #//*[@id="__bookmark_3"]/tbody/tr[8]/td[1]/div/a
    #//*[@id="__bookmark_2"]/tbody/tr[8]/td[2]/div/a
    #//*[@id="__bookmark_2"]/tbody/tr[8]/td[2]/div/a
    driver.switch_to.default_content()
    time.sleep(5)	
																																							
#retour à la page principale puis accès au iframe pour selectionner format fichier et export
    container_frame = driver.find_element_by_xpath("//iframe")
    driver.switch_to.frame(container_frame)
    select=driver.find_element_by_xpath("//*[@id='fileFormatList']/select")
    select.click()
    driver.find_element_by_xpath("//*[@id='fileFormatList']/select/option[3]").click()
    driver.find_element_by_id("item2").click()
    driver.switch_to.default_content()
    time.sleep(5)
    homepage=driver.find_element_by_xpath("//*[@id='header']/div[1]/a")    
    homepage.click()
    time.sleep(5)

    os.chdir(pathfile)
    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    for fichier in fichiers:
        x=re.search("^account_statistics_daily.", fichier) 
        if x:
            print(fichier)
            file_newname_newfile = os.path.join(pathfile, service+"Traffic"+date+".xls")
            file_oldname= os.path.join(pathfile, fichier)
            os.rename(file_oldname, file_newname_newfile)
    os.chdir(homepath)
    return 0
    
       
def trafficStat(service):
    
    if service == "p2p":
        path = "//*[@id='__bookmark_2']/tbody/tr["+v_mois+"]/td[2]/div/a"
    elif service == "a2p":
        path = "//*[@id='__bookmark_2']/tbody/tr["+v_mois+"]/td[3]/div/a"
    elif service == "p2a":
        path = "//*[@id='__bookmark_2']/tbody/tr["+v_mois+"]/td[4]/div/a"


    driver.find_element_by_link_text('Reports').click()
    driver.find_element_by_link_text('Traffic Statistics').click()
    time.sleep(5)
    
    driver.switch_to.default_content()
    time.sleep(1)
    container_frame = driver.find_element_by_xpath("//iframe")
    driver.switch_to.frame(container_frame)
    time.sleep(4)
    
    driver.find_element_by_link_text(v_an).click()        
    


# Entrer dans le internal frame et selectionner par son path du trafic P2P
    driver.switch_to.default_content()
    time.sleep(2)
    container_frame = driver.find_element_by_xpath("//iframe")
    driver.switch_to.frame(container_frame)
    time.sleep(3)
    service_value=driver.find_element_by_xpath(path)
    service_value.click()
    time.sleep(1)
    driver.switch_to.default_content()

#selection du mois pour le P2P
    time.sleep(3)
    driver.switch_to.default_content()
    for i in range(2):
        keyboard.press_and_release('tab')
    keyboard.press_and_release('enter')
#//*[@id="__bookmark_2"]/tbody/tr[2]/td[1]/div/a
#//*[@id="__bookmark_2"]/tbody/tr[2]/td[1]/div/a

#retour à la page principale puis accès au iframe pour selectionner format fichier et export
    time.sleep(3)
    container_frame = driver.find_element_by_xpath("//iframe")
    driver.switch_to.frame(container_frame)
    select=driver.find_element_by_xpath("//*[@id='fileFormatList']/select")
    select.click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='fileFormatList']/select/option[3]").click()
    time.sleep(1)
    driver.find_element_by_id("item2").click()
    time.sleep(1)
#retour a la page principale
    driver.switch_to.default_content()
    time.sleep(3)
    homepage=driver.find_element_by_xpath("//*[@id='header']/div[1]/a")    
    homepage.click()
    time.sleep(3)
    
    os.chdir(pathfile)
    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    for fichier in fichiers:
        service_=service.upper()+"_daily_"
        if service=="p2a":
            service_=service.upper()+"_Daily_"
        x=re.search(service_, fichier) 
        if x:
            print(fichier)
            file_newname_newfile = os.path.join(pathfile, service+"TrafficStatistics"+date+".xls")
            file_oldname= os.path.join(pathfile, fichier)
            os.rename(file_oldname, file_newname_newfile)
    os.chdir(homepath)
    return 0

