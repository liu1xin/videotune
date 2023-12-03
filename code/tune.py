# -*- coding = utf-8 -*-

import os
import shutil

def renamefile(path, fname):
    rname = os.path.join(path, os.path.basename(fname))
    shutil.copy2(fname, rname)
    return rname

def meregefile(path, fname, vfile, afile):
    print("merge file {}{} to {}".format(vfile, afile, fname))

def endfile(vfile, afile):
    if os.path.isfile(vfile):
        os.remove(vfile)

    if os.path.isfile(afile):
        os.remove(afile)

def tuneFile(destpath, item):
    #todo destpath clean

    # prepare grouppath
    grouppath = os.path.join(destpath, item.get("groupname"))
    if not os.path.exists(grouppath):
        os.mkdir(grouppath)
    
    # move file and decrypt
    vfile = renamefile(grouppath, item.get("video"))
    afile = renamefile(grouppath, item.get("audio"))

    # merge to last file
    meregefile(grouppath, item.get("filename"), vfile, afile)

    # do clean
    endfile(vfile, afile)