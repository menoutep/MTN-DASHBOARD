'MsgBox "Bonjour le monde !"
'mon code 

main  ' appel de la fonction main ci-dessous


Function main()

sql_server_connexion()   ' appel de la fonction sql_server_connexion() ci-dessous
'telfichier()
End Function



Function sql_server_connexion()

dim NomUtilisateur, MotDePasse, NomServeur, NomBaseDeDonnees, code, kpi, caracteristique, secondindex, valeur, action, date_deb, date_fin , datte
Dim strConnection, conn, rs, strSQL
 
'strConnection = "Driver={SQL Server};Server=SQLServerName;" & _
'"Database=DBaseName;Uid=sa;Pwd=password;"
 
 'Définition de la chaîne de connexion
Set cnx = Wscript.CreateObject("ADODB.Connection")

NomUtilisateur="inmp"  ' l'ancien était test
MotDePasse="D@shboard"   ' l'ancien était test  droit de lecture seul
NomServeur="10.18.26.96"
NomBaseDeDonnees="CBillDash"

cnx.ConnectionString = "UID=" & NomUtilisateur &";PWD=" & MotDePasse & ";" & "DRIVER={SQL Server};Server=" & NomServeur & ";Database=" & NomBaseDeDonnees & ";"

'Ouverture de la base de données
cnx.Open
' creation d'un recordsetSet 
Set rs = Wscript.CreateObject("ADODB.recordset")

' Listing des 10 derniers enregistrements de la table
action = inputbox("Voulez vous voir les 10 derniers enregistrements de la table valeurs_QOS_MOMO? OUI ou NON") ' lire une donnée entrée au clavier dans la variabla action 

if action="OUI" or action="oui" then

'lecture de la table valeurs
strSQL = "SELECT TOP 10 * FROM valeurs_QOS_MOMO where code='MUSSDQ' order by event_date desc"
rs.open strSQL, cnx, 3,3

' va au premier enregistrement dans le recordset
rs.MoveFirst
while not Rs.eof
kpi = rs.fields("id_kpi")  ' ce champ se remplit lui meme
caracteristique = rs.fields("id_caracteristique")  ' ne devons avoir toujours la valuer 4
code = rs.fields("code")   ' doit être 'USSD USAGE RATE' pour le ussd comviva usage rate
valeur = rs.fields("valeur")
date_deb = rs.fields("process_date")  ' meme date du jour concerné dans le modèle '2015-07-15'
date_fin = rs.fields("event_date")    ' meme date du jour concerné dans le modèle '2015-07-15' 
totreq = rs.fields("Total_request")
totrep = rs.fields("Total_request_SUCCES")
 
MsgBox "kpi: " & kpi & "  caracteristique: " & caracteristique & "  code: " & code & "  total requetes: " & totreq & "  total success: " & totrep & "  valeur: " & valeur & "  datedebut: " & date_deb & "  datefin: "  & date_fin

rs.MoveNext 
wend
rs.Close
end if

' suppression des données de la table
action = inputbox("Voulez vous supprimer des donnees dans la table valeurs_QOS_MOMO ? OUI ou NON") ' lire une donnée entrée au clavier dans la variabla action 

if action="OUI" or action="oui" then
datte = inputbox("Entrer la date: '2015-10-05' mettre les simples cotes")
strSQL = "DELETE FROM valeurs_QOS_MOMO WHERE event_date = " + datte + " AND code = 'MUSSDQ'" 
'strSQL = "DELETE FROM Valeurs WHERE event_date = " + datte + ""

'msgbox strSQL
rs.open strSQL, cnx, 1,1
'rs.Close
end if

' insertion des donneees dans la table value 
action = inputbox("Voulez vous inserer des donnees dans la table valeurs_QOS_MOMO? OUI ou NON") ' lire une donnée entrée au clavier dans la variabla action 

if action="OUI" or action="oui" then
'lecture des donees
Set WshShell = WScript.CreateObject("WScript.Shell")
dim filesys, readfile, contents, annee, jour, mois, tpss, entiere, qos, datant, firstindex, datedepart, datearrivee, dateenreg  ' ici on fait un e déclaration des variables sur une meme ligne le type n'est pas indiqué
Set fso = CreateObject("Scripting.FileSystemObject")
set filesys = CreateObject("Scripting.FileSystemObject")   ' créer un objet de type fichier
set readfile = filesys.OpenTextFile("D:\On root D\statistic\MoMQoS", 1, false)    ' créer le fichier readfile et lui associer une valeur ie ke fichier "D:\On root D\dump_segment"

datedepart = inputbox("Merci de specifire la date de debut: 20160104") '
datearrivee = inputbox("Merci de specifire la date de fin: 20160110") '
do while readfile.AtEndOfStream=false 
contents = readfile.ReadLine 

dateenreg = Mid(contents, 1, 8)

if dateenreg >= datedepart and dateenreg <= datearrivee then

annee = Mid(contents, 1, 4) ' retire la chaine commencant par la position 1 et de longueur 4
mois = Mid(contents, 5, 2)
jour = Mid(contents, 7, 2)
tpss = Mid(contents, 37, 4)
datant= "'" & annee & "-" & mois & "-" & jour & "'"
tpss = Mid(contents, 37, 6)
totreqs=Mid(contents, 44, 8)
totreps=Mid(contents, 53, 8)
'MsgBox tpss
'suppression d'eventuelles donnes existentes
strSQL = "DELETE FROM valeurs_QOS_MOMO WHERE event_date = " + datant + " AND code = 'MUSSDQ'" 
rs.open strSQL, cnx, 1,1

' insertion des donnees
'strSQL = "INSERT INTO Valeurs ([id_caracteristique], [code], valeur, process_date, event_date ) VALUES ('4', 'USSD USAGE RATE', tpss, datant, datant)" ' sans variable
strSQL = "INSERT INTO valeurs_QOS_MOMO ([id_caracteristique], [code], valeur, process_date, event_date, Total_request, Total_request_SUCCES) VALUES ('4', 'MUSSDQ', " + tpss + ", " + datant + ", " + datant + ", " + totreqs + ", " + totreps + ")"  ' avec variable
rs.open strSQL, cnx, 1,1
'rs.Close
'Exit Do
end if
loop

end if



'rs.Close
Set rs = Nothing
 
cnx.Close
Set cnx = Nothing

End Function