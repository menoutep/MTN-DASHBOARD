from xlrd import open_workbook 
from xlutils.copy import copy
from xlwt.Worksheet import Worksheet
import os

pathfile = "D:\ZABRE\Downloads"
os.chdir(pathfile)

def copie(file,num_sheet,start_r,end_r,start_col,end_col):
    wb=open_workbook(file)
    sheet = wb.sheet_by_index(num_sheet)
    columns = []
    for a in range(start_r,end_r):
        for b in range(start_col,end_col):
            columns.append(sheet.cell_value(a,b))       
    return columns
            
            

columns=copie("seamlessTraffic2022-08-24.xls",0,3,30,0,11)


def colle(file,num_sheet,start_r,end_r,start_col,end_col):
    wb=open_workbook(file)
    wb_cp=copy(wb)
    sheet_cp=wb_cp.get_sheet(num_sheet)
    i=0
    for a_ in range(start_r,end_r):
        for b_ in range(start_col,end_col):
            cell=columns[i]
            Worksheet.write(sheet_cp,a_,b_,cell)
            i+=1
    wb_cp.save(file)
    return 0

colle("MTN CDI Daily Report.xls",0,23,50,0,11)   
