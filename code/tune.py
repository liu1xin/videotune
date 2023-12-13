# -*- coding = utf-8 -*-

import os
import shutil
import subprocess
import shlex

DECRYPT_BILIBILI_OFFSET = 9
FFMPEG_SIMPLE = "ffmpeg -loglevel quiet -i video.m4s -i audio.m4s -c copy -y out.mp4"


def renamefile(path, fname):
    rname = os.path.join(path, os.path.basename(fname))
    with open(fname, 'rb') as source:
        source.seek(DECRYPT_BILIBILI_OFFSET)  # 跳过前9个加密用字节
        with open(rname, 'wb') as dest:  
            shutil.copyfileobj(source, dest)

    return rname

def meregefile(path, fname, vfile, afile):
    #print("merge file {} and {} to {}/{}.mp4".format(vfile, afile, path, fname))
    ffmpegcmd = "ffmpeg -loglevel quiet -i {} -i {} -c copy -y '{}/{}.mp4'".format(vfile, afile, path, fname)
    print(ffmpegcmd)
    cmdlist = shlex.split(ffmpegcmd)
    p = subprocess.Popen(cmdlist, shell=False)
    p.wait()

def cleantmpfile(vfile, afile):
    if os.path.isfile(vfile):
        os.remove(vfile)

    if os.path.isfile(afile):
        os.remove(afile)

def tuneFile(destpath, item):
    #todo destpath clean

    # prepare grouppath
    grouppath = os.path.join(destpath, str(item.get("groupid")))
    if not os.path.exists(grouppath):
        os.mkdir(grouppath)
    
    # decrypt m4s file
    vfile = renamefile(grouppath, item.get("video"))
    afile = renamefile(grouppath, item.get("audio"))

    # merge to last file
    meregefile(grouppath, item.get("filename"), vfile, afile)

    # clean tmp m4s file
    cleantmpfile(vfile, afile)