cd /D D:\ZABRE\Downloads
@echo off
set datte=%date%
Set sep=-
set an=%datte:~6,4%
set mois=%datte:~3,2%
set jour=%datte:~0,2%
If Not %datte:~0,2% EQU 01 goto D-1

Rem ############# Il faut calculer le mois si 28, 29 30 ou 31 jour pour faire mois -1 !
 
If %mois% == 01 goto DECEMBRE
If %mois% == 03 goto MARS
If %mois% == 05 goto Mois30
If %mois% == 07 goto Mois30
If %mois% == 08 goto DECEMBRE
If %mois% == 10 goto Mois30
If %mois% == 12 goto Mois30
 
Rem ############# Le mois actuel est un mois de 30 jours et pas Janvier ou Mars
Set jour=31
Set /A mois=%mois% - 1
Rem ############# On ajour un 0 pour l'affichage si le mois est de 01 à 09
IF %mois% LSS 10 set mois=0%mois%
Set /A an=%an% - 1  
Goto Suite
 
 
 
Rem ############## Je suis le 1 Janvier, je passe en 31 décembre année - 1
Rem ############## Je suis le 1 Aout, je passe le 31 Juillet
:DECEMBRE
Set jour=31
If %mois% == 08 goto AOUT
Set mois=12
Set /A an=%an% - 1
Goto suite
 
:AOUT
Set mois=07
goto Suite
 
 
:MARS
If Not %mois% == 03 goto M04
Rem ############# On est au mois de mars donc il faut calculer le mois de février
If %an% == 2008 goto NBCT
If %an% == 2012 goto NBCT
If %an% == 2016 goto NBCT
If %an% == 2020 goto NBCT
If %an% == 2024 goto NBCT
If %an% == 2028 goto NBCT
If %an% == 2032 goto NBCT
 
Rem ############## Mois de Février Normal
Set jour=28
Set /A mois=%mois% - 1
IF %mois% LSS 10 set mois=0%mois%
Goto Suite
 
:NBCT
Rem ############# Année Bct Mois de Février 28 jours
Set jour=29
Set /A mois=%mois% - 1
IF %mois% LSS 10 set mois=0%mois%
Goto Suite
 
 
 
 
Rem ############# Le mois actuel est un mois de 31 jours et pas Mars ou Aout
:Mois30
Set jour=31
Set Mt=%mois%
Set /A mois=%Mt% - 1
Rem ############# On ajour un 0 pour l'affichage si le mois est de 01 à 09
IF %mois% LSS 10 set mois=0%mois%
 
Goto Suite
 



:D-1
Set /A Jour=%Jour% - 1
IF %jour% LSS 10 set jour=0%jour%

:Suite
set etoile=*

set datecolle=%an%%mois%%jour%
set datesepare=%an%%sep%%mois%%sep%%jour%

set datecolle=%an%%mois%%etoile%
set datesepare=%an%%sep%%mois%%sep%%etoile%



>file.ftp echo open 10.2.6.120
>>file.ftp echo user alliman alliman
>>file.ftp echo lcd "D:\ZABRE\Downloads"
>>file.ftp echo cd /home/alliman2
>>file.ftp echo mget statscloud_%datesepare%_drapp1
>>file.ftp echo mget statscloud_%datesepare%_drapp2
>>file.ftp echo mget statscloud_%datesepare%_drapp3
>>file.ftp echo mget statscloud_%datesepare%_drapp4
>>file.ftp echo mget statscloud_%datesepare%_drapp5
>>file.ftp echo cd /script/reports
>>file.ftp echo lcd "D:\ZABRE\Downloads\smsc"
>>file.ftp echo mget sms_sucess.%datecolle%.csv 
Rem smsc_del_sucess.%datecolle%.csv
>>file.ftp echo cd /script/seamless_reports
>>file.ftp echo lcd "D:\ZABRE\Downloads\evd"
>>file.ftp echo mget sms_sucess.%datecolle%.csv 
Rem evd_del_sucess.%datecolle%.csv
>>file.ftp echo cd /script/ewp_reports
>>file.ftp echo lcd "D:\ZABRE\Downloads\momo"
>>file.ftp echo mget sms_sucess.%datecolle%.csv 
Rem momo_del_sucess.%datecolle%.csv


ftp -n -i -s:file.ftp
#sftp -n -i -s:file.ftp