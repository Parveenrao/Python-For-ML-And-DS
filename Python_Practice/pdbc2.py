# show database using python 

import mysql.connector

try:
    conn = mysql.connector.connect(
        user = 'root',
        password = 'October@26/2009',
        host = 'localhost',
        port = 3306
    )
    
    
    if conn.is_connected:
        print('Connected')


except:
    print('Unable to Connect')
            
curr = conn.cursor()
curr.execute("ShOW DATABASES")
for data in curr:
    print(data)
    
curr.close()
conn.close()                