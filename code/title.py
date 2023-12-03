# -*- coding = utf-8 -*-

import json
import os
import glob

def pathcheckinvalid(path):
    return os.path.isfile(path)

def parseVideoInfoFile(path):
    videoinfo = {}
    vinfofile = os.path.join(path, '.videoInfo')
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
    video = parseVideoInfoFile(path)
    va = getVideoAudioFile(path)
    video["video"] = va[0]
    video["audio"] = va[1]
    video["step"] = 0
    
    return video
    
def addToFileQueue(path, show=False):
    fileinfos = []
    for dirpath in os.listdir(path):
        if not pathcheckinvalid(os.path.join(path, dirpath)):
            fileinfos.append(getVideoMeta(os.path.join(path, dirpath)))
    
    if show is True:
        for item in fileinfos:
            print("get videometa", item)
                
    return fileinfos