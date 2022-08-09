from selenium import webdriver 
from selenium.webdriver.chrome.service import Service

#la methode openUrl permet d'ouvrir une url recu en parametre, 
# la methode renvoie une instance de webdriver qui permet de naviguer dans le DOM
def  openUrl(url):
    s = Service('chromedriver.exe')
    driver_ = webdriver.Chrome(service=s)
    driver_.get(url)
    return driver_

# creation de l'instance driver, cette instance devra toujours 
# etre declarer au debut du code juste apres la methode url
driver = openUrl("https://webscraper.io/test-sites")

#la methode cliquer permet de cliquer sur un element de la page, 
#elle prend en parametre la maniere dont on souhaite acceder a l'element de la page soit par son id s'il en possede, par sa classe, par son xpath
#attention lorsque l'on souhaite cliquer sur un lien l'on peut indiquer le text contenu dans le lien(voir documentation de selenium pour python)
#le second parametre est la valeur(id,class,name,...)
#le troisieme parametre est le driver precedemment creer 
def cliquer(way,element,driver):
    if way == "id":
      driver.find_element_by_id(element).click()
    elif way == "class":
        driver.find_element_by_class_name(element).click()
    elif way == "xpath":
        driver.find_element_by_xpath(element).is_selechted()
    elif way == "name":
        driver.find_element_by_name(element).click()
    elif way == "link_text":
        driver.find_element_by_link_text(element).click()
    return 0


#la methode loginWithId permet de se connecter sur un formulaire de connexion elle prend en parametre 
#l'id du champ imput pour le mail, 
# l'id du champ input pour le password, 
# la class du bouton submit , 
# une instance de driver, 
# le mail, 
# le password 
def loginWithId(id_mail,id_pwd,submit,driver,mail,pwd):
    
    driver.find_element_by_id(id_mail).send_keys(mail)
    driver.find_element_by_id(id_pwd).send_keys(pwd)
    cliquer("class",submit,driver)

    return 0


cliquer("xpath","//nav/ul/li[7]",driver)
loginWithId("username_id","password_id","signin-button" ,driver, "zabreseverin@gmail.com", "Leocadie0")
cliquer("link_text","Reports",driver)
cliquer("id", "Top Panel 3", driver)
cliquer("link_text","Traffic Statistics",driver)
cliquer("link_text","2022",driver)