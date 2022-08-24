from selenium import webdriver

import time 
import os

import re
from os import listdir
from os.path import isfile, join
from isis import date, date_end, date_start, pathfile, driver , homepath, accountWise, kara, wisetraffic, trafficStat

#creer une variable pour declencher le driver 

def nono():
####suppression fichiers datewise  traffic, ewpmom et seamless
    file_oldname = os.path.join(pathfile , "dateWiseReport.xls")
    if os.path.exists(file_oldname):
        os.remove(file_oldname)
    else:
        print("Impossible de supprimer le fichier dateWiseReport.xls car il n'existe pas")


    ####suppression fichiers datewise  traffic, ewpmom et seamlessichiers account stattistics daily
    os.chdir(pathfile)
    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    for fichier in fichiers:
        x=re.search("^account_statistics_daily.", fichier) 
        if x:
            print(fichier)
            os.remove(fichier)
    os.chdir(homepath)
    print("Suppression des fichiers account statistic effectuée") 

    driver.maximize_window()
    ###############################################Login au GUI#############################################################################
    driver.find_element_by_id('details-button').click()
    driver.find_element_by_id('proceed-link').click()
    driver.find_element_by_id('relogin').click()
    driver.find_element_by_name("loginModel.UserName").send_keys("ALLIMAN")
    driver.find_element_by_name("loginModel.UserName").send_keys('\ue004')
    actions=webdriver.ActionChains(driver)#intialisation 
    actions.send_keys("Desdje!@#1")
    actions.perform()
    
    try:
        driver.find_element_by_id('loginForm_Login').click()
    except:
        driver.quit()
    #############################################################################################################################
    ############################################################################################################################
    ################################Accounts wise seamless and epwmom##########################################################################


    #############################################################################################################################





    #################################################################################################################################
    ##################################################################################################################################
    ####################Gestion Trafic statistics P2P  A2P  P2A  #####################################################################
    file__ = os.path.join(pathfile , "P2PTrafficStatistics"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"P2PTrafficStatistics"+date+".xls existe deja")
    else:
        try:
            trafficStat("P2P")
        except:
            driver.quit()
            
    time.sleep(3)

    file__ = os.path.join(pathfile , "P2ATrafficStatistics"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"P2ATrafficStatistics"+date+".xls existe deja")
    else:
        try:
            trafficStat("P2A")
        except:
            driver.quit()
            
    time.sleep(3)

    file__ = os.path.join(pathfile , "A2PTrafficStatistics"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"A2PTrafficStatistics"+date+".xls existe deja")
    else:
        try:
            trafficStat("A2P")
        except:
            driver.quit()
            
    time.sleep(3)

    ################################FIN GESTION TRAFIC STATISTICS P2P A2P P2A    ###################################################
    ##################################################################################################################################
    #################################################################################################################################




    ###################################### telechargement datewise ewpmom seamless et traffic puis renommage
    file__ = os.path.join(pathfile , "ewpmomWise"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"ewpmomWise"+date+".xls existe deja")
    else:
        try:
            accountWise("ewpmom")
        except:
            driver.quit()
    time.sleep(3)


    file__ = os.path.join(pathfile , "seamlessWise"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"seamlessWise"+date+".xls existe deja")
    else:
        print("Le fichier "+"seamlessWise"+date+".xls n existe pas: debut extraction")
        try:
            accountWise("seamless")
        except:
            driver.quit()
    time.sleep(3)


    file__ = os.path.join(pathfile , "trafficWise"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"trafficWise"+date+".xls existe deja")
    else:
        print("Le fichier "+"trafficWise"+date+".xls n existe pas: debut extraction")
        try:
            wisetraffic()
        except:
            driver.quit()
    time.sleep(3)
    ##################################fin telechargement et renommage#################

    ###############################Fin function Kara########################################################

    ##################################################################################################################################
    ####################telechargement fichier Trafic MoMo et seamless si n'existent pas puis renommage  #####################################################################

    file_mom_traffic = os.path.join(pathfile , "ewpmomTraffic"+date+".xls")
    if os.path.exists(file_mom_traffic):
        print("Le fichier "+"ewpmomTraffic"+date+".xls existe deja")
    else:
        print("Le fichier "+"trafficWise"+date+".xls n existe pas: debut extraction")
        try:
            kara("ewpmom")
        except:
            driver.quit()
            
    time.sleep(5)
    file_seam_traffic = os.path.join(pathfile , "seamlessTraffic"+date+".xls")
    if os.path.exists(file_seam_traffic):
        print("Le fichier "+"seamlessTraffic"+date+".xls existe deja")
    else:
        print("Le fichier "+"seamlessTraffic"+date+".xls n existe pas: debut extraction")
        try:
            kara("seamless")
        except:
            driver.quit()

    driver.quit()


###############################Fin Trafic seamless and Mobile money########################################################
##################################################################################################################################
#################################################################################################################################

nono()
driver.quit()
