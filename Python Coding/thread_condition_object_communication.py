# in this conditon object method we can communicate between multiple threads

# acquire() ---- lock mechanism
# release() ----- release lock
# wait[timeout] ----  method is used to block the threads
# notify() ---- wake only 1 thread
# notify_all() --- wake up all threads

import threading
from time import sleep

con = threading.Condition()
def write_data():
    con.acquire()
    with open('report.txt', 'w') as file1:
        days = ['Monday', 'Tuesday', 'Wednessday', 'Thrusday', 'Friday', 'Saturday', 'Sunday']
        for day in days:
            temp = input(f"Enter temperature for {day}")
            file1.write(temp+ "\n")
    con.notify_all()
    con.release()

def max_temp():
    con.acquire()
    con.wait(timeout=0)
    with open('report.txt' , 'r') as file1:
        data = file1.readline()
        max1 = float(data[0].strip("\n"))
        for temp in data[1:]:
            temp = float(temp.strip("\n"))
            if temp > max1:
                max1 = temp
    print(f"maximum temperature is {max1}")
    con.release()

def avg():
    con.acquire()
    con.wait(timeout=0)
    with open('report.txt', 'r') as file1:
        data = file1.readline()
        sum1 = 0
        for temp in data:
            temp = float(temp.strip("\n"))
            sum1 = sum1 + temp
        avg = sum1/len(data)
        print(f"average temperature is {avg}")
        con.release()

t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg)

t1.start()
t2.start()
t3.start()







