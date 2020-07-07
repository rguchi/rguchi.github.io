from __future__ import print_function
from random import randint
import subprocess
import re
import time
import mysql.connector
import ast

cnx = mysql.connector.connect(user='root', password='Mysql', database='test')
cursor = cnx.cursor()


add_point = ("INSERT INTO test.tbl "
               "(time, val) "
               "VALUES (%s, %s);" )

# Loop with fio and SQL insert

proc = subprocess.Popen(["C:\\Users\\guptar1\\Servers\\fio\\fio.exe",
                         "--thread",              # suppress thread warning on windows
                         "--status-interval=1",   # print output every 1s
                         "--terse-version=3",
                         "--output-format=terse", # terse format
                         "C:\\Users\\guptar1\\Servers\\fioprof.fio"            
                         ]
                        ,stdout=subprocess.PIPE
                        ,stderr=None)

# Continue executing and adding the values to the SQL database
status = True
while status:
    status = False
    line = proc.stdout.readline()
    if not line == b"":
        out = line.decode("utf-8").rstrip()
        params = out.split(";")
        print (out,params[7])
        tpoint = int(time.time()*1000)               
        data_point = (tpoint, ast.literal_eval(params[7])*(randint(8,12)/12.0)/1000)
        # Insert new point
        cursor.execute(add_point, data_point)
        # Make sure data is committed to the database
        cnx.commit()

        status = True

    
    if not status and proc.poll() is not None:
        break
    

#Close database connection
cursor.close()
cnx.close()
