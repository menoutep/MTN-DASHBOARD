from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 
import os 

username = "zabreseverin@gmail.com"
pwd = "Leocadie0"
s=Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
date = time.strftime('%Y-%m-%d')#cette ligne permet de stocker la date actuel en format ex: 2022-09-28 y-m-d
driver.get("https://webscraper.io/test-sites")
driver.maximize_window() 
try:
    button_login=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
    button_login.click()
except TimeoutException:
    print ("la localisation du bouton met trop de temps ")

#button_login = driver.find_element(By.LINK_TEXT,"Login")

#driver.find_element_by_xpath("//*[contains(text(), 'Show Next Date Available')]").click()

def login(username, pwd):
    try:
        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='E-mail']")))#mettre le placeholder qui se trouve dans le placeholder du champ input du username
        #pwd_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Password']")))#mettre le placeholder qui se trouve dans le placeholder du champ input du password
    except:
        print("la localisation des deux champs input a echouer ")
    login_actions = webdriver.ActionChains(driver)
    login_actions.move_to_element(username_input)
    #time.sleep(3)
    login_actions.click(username_input)
    #time.sleep(3)
    login_actions.send_keys(username)
    login_actions.send_keys('\ue004')#cette ligne permet de faire croire au navigateur que l'on a appuyer sur la touche tab qui permet de passer d'un champ input au suivant 
    login_actions.send_keys(pwd)
    #login_actions.move_to_element(pwd_input)
    #login_actions.double_click(pwd_input)
    #login_actions.send_keys(pwd)
    login_actions.perform()
    return 0
login(username,pwd)
time.sleep(25)
driver.quit()
#webdriver.Keys('\ue004')