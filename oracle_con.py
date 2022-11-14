import cx_Oracle

try:
    pathfile = "C:\oracle\instantclient_21_6"
    cx_Oracle.init_oracle_client(lib_dir=pathfile)
    con = cx_Oracle.connect('unouser/unopass@vas-scan')
 
except cx_Oracle.DatabaseError as er:
    print('There is an error in the Oracle database:', er)
 
else:
    try:
        cur = con.cursor()
 
        # fetchall() is used to fetch all records from result set
        cur.execute('select * from LTRIM')
        rows = cur.fetchall()
        print(rows)
 
        # fetchmany(int) is used to fetch limited number of records from result set based on integer argument passed in it
        cur.execute('select * from LTRIM')
        rows = cur.fetchmany(3)
        print(rows)
 
        # fetchone() is used fetch one record from top of the result set
        cur.execute('select * from LTRIM')
        rows = cur.fetchone()
        print(rows)
 
    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)
 
    except Exception as er:
        print('Error:'+str(er))
 
    finally:
        if cur:
            cur.close()
 
finally:
    if con:
        con.close()
