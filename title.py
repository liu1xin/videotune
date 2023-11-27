# -*- coding = utf-8 -*-

import json
import os
import glob

def filecheck(path):
    return True

def parseVideoInfoFile(path):
    videoinfo = {}
    vinfofile = os.path.join(path, '.videoInfo')
    print(vinfofile)
    with open(vinfofile, 'r') as f:
        data = json.load(f)
        videoinfo["groupname"] = data["groupTitle"]
        videoinfo["filename"] = data["title"]
        videoinfo["cid"] = data["cid"]
        
    return videoinfo
    
def getVideoAudioFile(path):
    m4sfiles = glob.glob(os.path.join(path, '*.m4s'))
    size1 = os.path.getsize(m4sfiles[0])
    size2 = os.path.getsize(m4sfiles[1])
    if (size1 > size2):
        return (m4sfiles[0], m4sfiles[1])
    else:
        return (m4sfiles[1], m4sfiles[0])
    

def getVideoMeta(path):
    if not filecheck(path):
        print("path {0} check fail".format(path))
        return 1
        
    video = parseVideoInfoFile(path)
    va = getVideoAudioFile(path)
    video["video"] = va[0]
    video["audio"] = va[1]
    
    print(video)
    
    
path = r'./1316729774'
getVideoMeta(path)
