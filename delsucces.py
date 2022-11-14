import os
import re
import numpy as np 
from xlrd import open_workbook 
from xlutils.copy import copy
from xlwt.Worksheet import Worksheet
from datetime import date as d
from datetime import timedelta
import pandas as pd
pathfile = "D:\ZABRE\Downloads"
os.chdir(pathfile)

def copyDel(file):
    file=pd.ExcelFile(file)
    sheet_ = pd.read_excel(file,sheet_name=file)
    sheet = pd.DataFrame(sheet_)
    date_list_=sheet.iloc[0:,0:1]
    taille=len(date_list_)
    date_list=date_list_['DAY-WISE TPS REPORT'].unique()
    peak_list=[]
    date_list=np.delete(date_list,0)
    for date in date_list:
        date=str(date)
        temp=[]
        for a in range(0,taille-1):
            x=a+1
            cell=sheet.iloc[a:x,0:1]
            cell=cell['DAY-WISE TPS REPORT']
            cell =cell.values[0]
            cell=str(cell)
            if cell == date:
                values_peak =sheet.iloc[a:x,3:4]
                values_peak=values_peak.values[0][0]
                temp.append(values_peak)
        peak_list.append(max(temp))
        
    return peak_list
def copyDel(file_name):
    temp = []
    
    
    x=re.search("^smsc.", file_name)
    momo=re.search("^momo.", file_name)
    evd=re.search("^evd.", file_name)
    if x:
        
        os.chdir("D:\ZABRE\Downloads\smsc")
        data = pd.read_csv(file_name)
        y=0
        for i in range(3,9):
            xx=i+1
            line = data.iloc[i:xx,0:1].values
            temp.append(line[0][0])
            print(temp)   
            y=y+1 
    if momo:
        os.chdir("D:\ZABRE\Downloads\momo")
        data = pd.read_csv(file_name)  
        y=1  
        for i in range(3,8):
            xx=i+1
            line = data.iloc[i:xx,0:1].values
            temp.append(line[0][0])
            print(temp)
            y=y+1
    if evd:
        os.chdir("D:\ZABRE\Downloads\evd")
        data = pd.read_csv(file_name)  
        y=1  
        for i in range(3,8):
            xx=i+1
            line = data.iloc[i:xx,0:1].values
            temp.append(line[0][0])
            print(temp)
            y=y+1
    return temp

def colle(file,num_sheet,start_r,end_r,start_col,end_col,copie_):
    os.chdir("D:\ZABRE\Downloads")
    wb=open_workbook(file,formatting_info=True)
    wb_cp=copy(wb)
    sheet_cp=wb_cp.get_sheet(num_sheet)
    i=0
    try:
        for a_ in range(start_r,end_r):
            for b_ in range(start_col,end_col):
                cell=copie_[i]
                Worksheet.write(sheet_cp,a_,b_,cell)
                wb_cp.save(file)       
                i+=1

        wb_cp.save(file)
    except:
        print("...")
  
    return 0

def copyPasteDel(file_source:str,file_dest:str,num_sheet_dest:int,start_r_dest:int,end_r_dest:int,start_col_dest:int,end_col_dest:int):
    columns=copyDel(file_source)
    colle(file_dest,num_sheet_dest,start_r_dest,end_r_dest,start_col_dest,end_col_dest,columns)
    
    return 0

today = d.today()
yesterday = today - timedelta(days = 1)
#date = time.strftime('%Y-%m-%d')
date = yesterday
date=str(date)
jour = date[8:10]
jour=int(jour)
line_start_output=jour + 1
line_end_output=line_start_output + 1
date_ = re.sub("-","",date)
smsc="smsc_del_sucess."+date_+".csv"
evd="evd_del_sucess."+date_+".csv"
momo="momo_del_sucess."+date_+".csv"
#copyPasteDel(smsc,"MTN CDI Daily Report1.xls",9,line_start_output,line_end_output,1,7)
#copyPasteDel(evd,"MTN CDI Daily Report1.xls",9,line_start_output,line_end_output,8,13)
#copyPasteDel(momo,"MTN CDI Daily Report1.xls",9,line_start_output,line_end_output,14,19)