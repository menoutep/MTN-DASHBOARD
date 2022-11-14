from selenium import webdriver
import time 
import os
import re
from os import listdir
from os.path import isfile, join
from main_functions import date, pathfile, driver , homepath, accountWise, kara, wisetraffic, trafficStat, ussd,tps

#creer une variable pour declencher le driver 

def nono():
    
####suppression des fichier sucess rate failure per service###########################
    os.chdir(pathfile)
    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    for fichier in fichiers:
        x=re.search("^SuccessFailure Rate per Service.", fichier) 
        if x:
            os.remove(fichier)
    os.chdir(homepath)
    print("Suppression du fichier SuccessFailure Rate per Service effectuée") 
    
##############################
    os.chdir(pathfile)
    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    for fichier in fichiers:
        x=re.search("^tps_.", fichier) 
        if x:
            print(fichier)
            os.remove(fichier)
    os.chdir(homepath)
    print("Suppression du fichier tps effectuée") 
###########################
##################################################################################
####suppression fichiers datewise  traffic, ewpmom et seamless
    file_oldname = os.path.join(pathfile , "dateWiseReport.xls")
    if os.path.exists(file_oldname):
        os.remove(file_oldname)
    else:
        print("Impossible de supprimer le fichier dateWiseReport.xls car il n'existe pas")


    ####suppression fichiers ewpmom et seamlessichiers account stattistics daily
    os.chdir(pathfile)
    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    for fichier in fichiers:
        x=re.search("^account_statistics_daily.", fichier) 
        if x:
            print(fichier)
            os.remove(fichier)
    os.chdir(homepath)
    print("Suppression des fichiers account statistic effectuée") 
    
    
   ####suppression fichiers  p2p,p2a,a2p daily ##################
    os.chdir(pathfile)
    fichiers = [f for f in listdir(pathfile) if isfile(join(pathfile, f))]
    for fichier in fichiers:
        x=re.search("^_daily_.", fichier) 
        if x:
            
            os.remove(fichier)
    os.chdir(homepath)
    print("Suppression des fichiers account statistic effectuée") 
    ################################""
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
    ################################################################################################################
    
    
    file__ = os.path.join(pathfile , "p2pTrafficStatistics"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"p2pTrafficStatistics"+date+".xls existe deja")
    else:
        try:
            trafficStat("p2p")
        except:
            driver.quit()
            
    time.sleep(3)

    file__ = os.path.join(pathfile , "p2aTrafficStatistics"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"p2aTrafficStatistics"+date+".xls existe deja")
    else:
        try:
            trafficStat("p2a")
        except:
            driver.quit()
            
    time.sleep(3)

    file__ = os.path.join(pathfile , "a2pTrafficStatistics"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"a2pTrafficStatistics"+date+".xls existe deja")
    else:
        try:
            trafficStat("a2p")
        except:
            driver.quit()
            
    time.sleep(3)
    
    #############
    ############################################################################################################################
    ################################Accounts wise seamless and epwmom##########################################################################
    
    file_tps_ussd_traffic = os.path.join(pathfile , "tpsussd"+date+".xls")
    if os.path.exists(file_tps_ussd_traffic):
        print("Le fichier "+"tpsussd"+date+".xls existe deja")
    else:
        print("Le fichier "+"tpsussd"+date+".xls n existe pas: debut extraction")
        try:
            tps("ussd")
        except:
            driver.quit()

    time.sleep(5)
    
    file_tps_sms_traffic = os.path.join(pathfile , "tpssms"+date+".xls")
    if os.path.exists(file_tps_sms_traffic):
        print("Le fichier "+"tpssms"+date+".xls existe deja")
    else:
        print("Le fichier "+"tpssms"+date+".xls n existe pas: debut extraction")
        try:
            tps("sms")
        except:
            driver.quit()

    time.sleep(5)
    
    file_tps_im_traffic = os.path.join(pathfile , "tpsim"+date+".xls")
    if os.path.exists(file_tps_im_traffic):
        print("Le fichier "+"tpsim"+date+".xls existe deja")
    else:
        print("Le fichier "+"tpsim"+date+".xls n existe pas: debut extraction")
        try:
            tps("im")
        except:
            driver.quit()

    time.sleep(5)
    ########################################waveci############################

    file_wave_traffic = os.path.join(pathfile , "WAVECITraffic"+date+".xls")
    if os.path.exists(file_wave_traffic):
        print("Le fichier "+"WAVECITraffic"+date+".xls existe deja")
    else:
        print("Le fichier "+"WAVECITraffic"+date+".xls n existe pas: debut extraction")
        try:
            kara("WAVECI")
        except:
            driver.quit()

    time.sleep(5)
    
    ############################################################################
    
    ########################################waveci2############################
    file_wave2_traffic = os.path.join(pathfile , "WAVECI2Traffic"+date+".xls")
    if os.path.exists(file_wave2_traffic):
        print("Le fichier "+"WAVECI2Traffic"+date+".xls existe deja")
    else:
        print("Le fichier "+"WAVECI2Traffic"+date+".xls n existe pas: debut extraction")
        try:
            kara("WAVECI2")
        except:
            driver.quit()

    time.sleep(5)
    
    ############################################################################
    ##########################################SuccessFailure Rate per Service#####################################################

    
    
    file__ = os.path.join(pathfile , "ussdqos"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"ussdqos"+date+".xls existe deja")
    else:
        try:
            ussd()
        except:
            driver.quit()
            
            
    time.sleep(3)



    #################################################################################################################################
    ##################################################################################################################################
    ####################Gestion Trafic statistics P2P  A2P  P2A  #####################################################################


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
    
    file__ = os.path.join(pathfile , "WAVECIWise"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"WAVECIWise"+date+".xls existe deja")
    else:
        print("Le fichier "+"WAVECIWise"+date+".xls n existe pas: debut extraction")
        try:
            accountWise("WAVECI")
        except:
            driver.quit()
    time.sleep(3)
    
    file__ = os.path.join(pathfile , "WAVECI2Wise"+date+".xls")
    if os.path.exists(file__):
        print("Le fichier "+"WAVECI2Wise"+date+".xls existe deja")
    else:
        print("Le fichier "+"WAVECI2Wise"+date+".xls n existe pas: debut extraction")
        try:
            accountWise("WAVECI2")
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
