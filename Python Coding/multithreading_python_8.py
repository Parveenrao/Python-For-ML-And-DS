# builtin function in multithreading
# 1) is_alive()---> check thread is running or not
# 2) main_thread()---> return main thread details
# 3) active_count() ---> no. of running thread
# 4) enumerate () ----> list of all running thread
# 5) get_native_id()---> return native id of thread

from threading import Thread, main_thread , active_count ,enumerate
def display():
    print("main thread details" , main_thread())
    for i in range(4):
        print("hello world")

def show():
    for i in range(3):
        print("Hey Parveen")


t1 = Thread(target=display)
print("before",t1.is_alive())
t1.start()
print('after',t1.is_alive())

print("No of active running threads" , active_count())
print(enumerate())
