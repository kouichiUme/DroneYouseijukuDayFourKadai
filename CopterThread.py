import time
import threading
import autocopter 

class CopterThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        time.sleep(2)
        print("main copter")
        # autocopter.copter()
