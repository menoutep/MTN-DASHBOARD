from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 
import os 
###############################
###############################
#############################
#la seule partie a modifier est celle entre les fleches, remplacer zabre... par votre username et Leo... par votre password
#==============================>
username = "zabreseverin@gmail.com" #mettre votre username entre les cote 
pwd = "Leocadie0"#mettre votre password entre les cote 
#==============================>
s=Service('chromedriver.exe')#permet d'indiquer le webdriver que l'on souhaite utiliser (Chrome, firefox...)
driver = webdriver.Chrome(service=s) #permet de recuperer une instance de l'objet webdriver representant une session de navigation 
date = time.strftime('%Y-%m-%d')#cette ligne permet de stocker la date actuel en format ex: 2022-09-28 y-m-d
driver.get("https://10.18.63.135/9090/im/")#mettre l'url du site souhaitez entre cote 
driver.maximize_window()#permet d'ouvrir la page en mode grand ecran  
try:
    button_parametre_avance=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "details-button")))#recupere le boutton parametre avancé
    button_parametre_avance.click()#permet de cliquer sur boutton
    lien = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "proceed-link")))
    lien.click()
except :
    print ("something went wrong between the line 17 and line 22 ")

#button_login = driver.find_element(By.LINK_TEXT,"Login")

#driver.find_element_by_xpath("//*[contains(text(), 'Show Next Date Available')]").click()
##############################################################
#ne pas modifier la fonction login
##############################################################
def login(username, pwd):
    try:
        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='UserName']")))#mettre le placeholder qui se trouve dans le placeholder du champ input du username
        button_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"loginForm_Login")))#mettre le placeholder qui se trouve dans le placeholder du champ input du password
    except:
        print("la localisation du champs pour le username input a echouer,  modifier la ligne 32, remplacer BY.XPATH par By.ID et ce ce qui se trouve entre les cote par: username ")
    login_actions = webdriver.ActionChains(driver)#intialisation d'une chaine d'actions
    login_actions.move_to_element(username_input)#permet de pointer le curseur de la souris sur le input username
    #time.sleep(3)
    login_actions.click(username_input)#click sur le input username 
    #time.sleep(3)
    login_actions.send_keys(username)#permet d'envoyer le contenu de la variable username dans le user input
    login_actions.send_keys('\ue004')#cette ligne permet de faire croire au navigateur que l'on a appuyer sur la touche tab qui permet de passer d'un champ input au suivant 
    login_actions.send_keys(pwd)#permet d'envoyer le contenu de la variable username dans le password input
    login_actions.move_to_element(button_login)
    login_actions.click(button_login)
    #login_actions.send_keys(pwd)
    login_actions.perform()#lance la chaine d'actions
    return 0
###################################################################################""
login(username,pwd)#appelle de la methode login
time.sleep(25)
driver.quit()
#webdriver.Keys('\ue004')