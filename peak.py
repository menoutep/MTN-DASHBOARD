import os 
import numpy as np
from xlrd import open_workbook 
from xlutils.copy import copy
from xlwt.Worksheet import Worksheet
from datetime import date as d
from datetime import timedelta
import pandas as pd
pathfile = "D:\ZABRE\Downloads"
os.chdir(pathfile)

today = d.today()
yesterday = today - timedelta(days = 1)
date = yesterday
date = str(date)
jour = date[8:10]
jour=int(jour)
                    
def colle(file,num_sheet,start_r,end_r,start_col,end_col,copie_):
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

def copyTps(file):
    file=pd.ExcelFile(file)
    sheet_ = pd.read_excel(file,sheet_name='Report')
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

def copyPasteTps(file_input,file,num_sheet,start_r,end_r,start_col,end_col):
    xx=copyTps(file_input)
    colle(file,num_sheet,start_r,end_r,start_col,end_col,xx)

line_end_output=jour + 6


            
    
