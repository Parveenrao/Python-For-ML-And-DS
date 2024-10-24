import mysql.connector

try:
    conn = mysql.connector.connect(
           user = 'root',
           password = 'October@26/2009',
           host = 'localhost',
           port = 3306
)
    
    if conn.is_connected:
        print("Connected")

except:
    print("Unable to connect")  
    
 
curr  = conn.cursor()
curr.execute("Create Database Parveen")
curr.close()          
    
 
conn.close()    