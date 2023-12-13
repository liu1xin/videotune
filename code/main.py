# -*- coding = utf-8 -*-

import sys
import threading
import time
from title import addToFileQueue
from tune import tuneFile

def addFileMock():
    filequeue.append({"file": "hello.txt",
                      "step": 0})
    filequeue.append({"file": "jubmp.txt",
                      "step": 0})
    filequeue.append({"file": "world.txt",
                      "step": 0})
    filequeue.append({"file": "dance.txt",
                      "step": 0})
    

def scanTask(procnum=3):
    for item in filequeue:
        if 0 == item.get("step", 0):
            tuneThreadStart(item)
        
    time.sleep(3)
    return 0

def tuneThreadStart(item):
    tt = threading.Thread(target=tuneTask, args=[item])
    tt.start()

def tuneTask(item):
    print("process file {}".format(item.get("file")))

filequeue = list()

if __name__ == "__main__":
    procnum = int(sys.argv[1])
    frompath = sys.argv[2]
    destpath = sys.argv[3]
    
    filequeue.extend(addToFileQueue(frompath, show=False))
    tuneFile(destpath, filequeue[0])
    tuneFile(destpath, filequeue[1])
    tuneFile(destpath, filequeue[2])
    tuneFile(destpath, filequeue[3])
              
             

    #st = threading.Thread(target=scanTask, args=[procnum])
    #st.start()
    #st.join()