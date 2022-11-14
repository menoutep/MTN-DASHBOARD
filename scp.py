import os 
from xlrd import open_workbook 
from xlutils.copy import copy
from xlwt.Worksheet import Worksheet
from datetime import date as d
from datetime import timedelta
pathfile = "D:\ZABRE\Downloads"
os.chdir(pathfile)

today = d.today()
yesterday = today - timedelta(days = 1)
date = yesterday
date = str(date)
jour = date[8:10]
jour=int(jour)
end_row = 5 + jour              
start_row = end_row - 1

def search(file,num_sheet):
    wb = open_workbook(file,formatting_info=True)
    sheet = wb.sheet_by_index(num_sheet)
    qos = [0,0,0,0,0]
    try:   
        for a in range(0,234):
            if sheet.cell_value(a,0) == "105":
                qos1 = sheet.cell_value(a,1)
                qos[0]=qos1
                
            if sheet.cell_value(a,0) == "133":
                qos2 = sheet.cell_value(a,1)
                qos[1]=qos2
               
            if sheet.cell_value(a,0) == "155":
                qos3 = sheet.cell_value(a,1)
                qos[2]=qos3
               
            if sheet.cell_value(a,0) == "422":
                qos4 = sheet.cell_value(a,1)
                qos[3]=qos4
                
            if sheet.cell_value(a,0) == "590":
                qos5 = sheet.cell_value(a,1)
                qos[4]=qos5
                
    except:
        
        print("...")
    return qos


                     

def searchcopy(file_input, sheet,file_output):
    qos=search(file_input,sheet)
    colle(file_output,1,start_row,end_row,12,17,qos)
    return 0

                      
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


def copyBlock(file_input, sheet_i,file_output):
    wb=open_workbook(file_input,formatting_info=True)

    xx=[]
    sheet=wb.sheet_by_index(sheet_i)
    try:
        for a in range(3,238):
            for b in range(0,3):
                xx.append(sheet.cell_value(a,b))
    except:
        print('...')
    
    wb=open_workbook(file_output,formatting_info=True)
    wb_cp=copy(wb)
 
    sheet_cp=wb_cp.get_sheet(8)
     
    end_line=len(xx) -1
    
    i=0
    try:
        for a_ in range(0,end_line):
            for b_ in range(0,3):
                cell=xx[i]
                
                Worksheet.write(sheet_cp,a_,b_,cell)
                i+=1
    except:
        print('...')
    wb_cp.save(file_output)


