import pandas as pd 
import os
import mysql.connector as mysql
mydb = mysql.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="taratata"
)
mycursor = mydb.cursor()
pathfile = "D:\TAF "
os.chdir(pathfile)
data = pd.ExcelFile('BH 3G May 2022.xlsx')#cette ligne permet de charger notre classeur excel dans la variable data
#une fois le classeur chargé, l'on fait print(data.sheet_names) pour voir le nom des feuille de travail contenue dans le classeur
print(data.sheet_names) 
momo_d= pd.read_excel('BH 3G May 2022.xlsx',sheet_name='QueryResult')
momo=pd.DataFrame(data=momo_d)


for i in range(1,10):
    line_one=momo.iloc[y:x,0:5] 
    x=i
    y=i-1
    #la fonction iloc permet de selectionner une partie precise de notre feuille de calcul on indique les ligne et colonnes 
    time=line_one.iloc[0,0:1]
    time = str(time)
    wcell=line_one.iloc[0,1:2]
    wcell=str(wcell)
    locality=line_one.iloc[0,2:3]
    locality=str(locality)
    mean_tcp=line_one.iloc[0,3:4]
    mean_tcp=float(mean_tcp)
    data_volume=line_one.iloc[0,4:5]
    data_volume=float(data_volume)
    sql = "INSERT INTO 3g (time, wcell, locality, mean_tcp, data_volume) VALUES (%s, %s, %s, %s, %s)"
    val = (time, wcell, locality, mean_tcp, data_volume)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
     # ma metode head() permet de renvoyer les premeiers element du tableau sur lequel est appelé
#momo.drop(['Day'],axis=1)permet de supprimer la colonne day de notre dataframe 
