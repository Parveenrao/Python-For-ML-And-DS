from threading import Thread
from time import sleep

def upload():
    print("Uploading Started")
    sleep(3)
    print("Video Uploaded")

def notification():
    print("Sending Notification to subscriber code")

t1 = Thread(target=upload)
t2 = Thread(target=notification)
t1.start()
t1.join()   # now first thread will be executed and then other thread will be started
t2.start()
t2.join()

# main thread
for i in range(4):
    print("Hello Parveen")

    # this is  not the case notification should be send after the video was uploaded , so we use join method

    # join method is used when one thread waits for other thread to be executed


