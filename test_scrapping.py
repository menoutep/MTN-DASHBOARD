from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.action_chains import ActionChains
import time 
import os 
#creer une variable pour declencher le driver 
s=Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
date = time.strftime('%Y-%m-%d')
driver.get("https://webscraper.io/test-sites")
driver.maximize_window() #permet de mettre la page en grand ecran 
#driver.fullscreen_window() permet de mettre la page en plein ecran 

button_login=driver.find_element_by_link_text("Login")
button_login.click()
user=driver.find_element_by_id("username_id")
pwd=driver.find_element_by_id("password_id")
actions = webdriver.ActionChains(driver)
actions.move_to_element(user)
#time.sleep(3)
actions.double_click(user)
#time.sleep(3)
actions.send_keys("zabreseverin@gmail.com")
actions.move_to_element(pwd)
#time.sleep(3)
actions.double_click(pwd)
#time.sleep(3)
actions.send_keys("Leocadie0")
actions.perform()
driver.find_element_by_class_name("signin-btn").click()
download=driver.find_elements_by_xpath("//tr/td[12]/div[1]/div/button")
options=driver.find_element_by_xpath("//tr/td[12]/div[1]/div/ul/li[2]")
driver.implicitly_wait(3)
checkboxs=driver.find_elements_by_id("checkbox")
checkboxs[0].click()
download[0].click()
options.click()
time.sleep(20)
driver.close()
actions = webdriver.ActionChains()
#actions.move_to_element(username_input)



#actions.click(username_input)
#actions.send_keys("joza")

#actions.move_to_element(password_input)




