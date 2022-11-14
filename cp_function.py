import os 
from xlrd import open_workbook 
from xlutils.copy import copy
from xlwt.Worksheet import Worksheet

pathfile = "D:\ZABRE\Downloads"
os.chdir(pathfile)

################traitement fichier excel##############

def copie(file,num_sheet,start_r,end_r,start_col,end_col):
    wb=open_workbook(file,formatting_info=True)
    sheet = wb.sheet_by_index(num_sheet)
    columns = []
    try:
        for a in range(start_r,end_r):
            for b in range(start_col,end_col):
                
                columns.append(sheet.cell_value(a,b))
    except:
        print("...")      
    return columns
                      
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
                        
                i+=1
    except:
        print("...")

    wb_cp.save(file)
  
    return 0

   
def copyPaste(file_source:str,num_sheet_source:int,start_r_source:int,end_r_source:int,start_col_source:int,end_col_source:int,file_dest:str,num_sheet_dest:int,start_r_dest:int,end_r_dest:int,start_col_dest:int,end_col_dest:int):
    columns=copie(file_source,num_sheet_source,start_r_source,end_r_source,start_col_source,end_col_source)
    colle(file_dest,num_sheet_dest,start_r_dest,end_r_dest,start_col_dest,end_col_dest,columns)
    
    return 0

##############fin traitement#############################