import ftplib 
host = "10.2.6.120" # adresse du serveur FTP
user = "alliman" # votre identifiant
password = "alliman" # votre mot de passe
connect = ftplib.FTP(host,user,password) # on se connecte
connect.cwd("/script/reports") # on récupère le listing
rep=connect.sendcmd("LS")
#rep=connect.transfercmd()
print(rep)
connect.quit()