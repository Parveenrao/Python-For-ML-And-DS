from time import sleep
from threading import Thread

videos = ['Machine Learning' , 'Deep Learning' , 'Natural Language Processing' , 'Computer Vision']


class Myclass(Thread):
    def run(self):
        for vid in videos:
            print(f"{vid} start uploading")
            sleep(3)
            print(f"{vid} is uploaded")


for i in range(4):
    sleep(0.3)
    print("Checking Copyrights")
 
 
t1 = Myclass()
t1.start()           