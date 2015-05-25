# -*- coding: utf-8 -*-  
#!/bin/python
#Des:replace ' ' and ':' to '_' in the name of files and dirs. 
#Author:zhoulin zhoulin@itzhoulin.com
#Date:20150401
#Update:
#20150403:判断目标文件夹名是否存在，如存在则尾部加_2，启用commands.getstatusoutput执行重命名操作
#20150524：加命令行参数决定是否执行重命名操作

import os
import sys
import re
import hashlib
from commands import getstatusoutput as cgso

doRename = ''
if len(sys.argv) > 2:
    doRename = sys.argv[2];
    if doRename != 'rename':
        print("Unrecognize arg;only support rename or no arg")
        exit(1)

def is_space(char):
    if re.search(r"\s",char):
        return True
    else:
        return False

def calcMD5(filename):
    m = hashlib.md5()
    with open(filename, "rb") as f:
        while True:
            buf = f.read(1024 * 1024)
            if buf:
                m.update(buf)
            else:
                break

    return m.hexdigest()

def renameDir(dirlist):
    #修改文件夹名中的空格需要从子目录开始一级一级目录修改
    dirlist.sort(reverse=True)
    print("\n===================================\n")
    for dirname in dirlist:
        print("initial:"+dirname)
        subdir = dirname.split('/')[-1]
        print("subdir:"+subdir)
        newsubdir = re.sub(' ','_',subdir)
        print(dirname.split('/')[:-1])
        newdirname=''
        for i in dirname.split('/')[:-1]:
            newdirname += i +os.sep
    #        print(newdirname)
        newdirname = newdirname+newsubdir
        if(os.path.exists(newdirname)):
            newdirname = newdirname+"_2"
        print("Final:"+newdirname)
        os.renames(dirname,newdirname)
        #status,output=cgso("mv "+dirname+"  "+newdirname)
        print("\n")

currentDir=sys.argv[1]
print("Working dir is:"+currentDir)
dirlist = []
for dirName,subDirList,fileList in os.walk(currentDir):
    for fname in fileList:
        absfilepath=dirName+os.sep+fname
        if(is_space(fname)):
            print("file:"+absfilepath)
            if doRename:
                newfname=re.sub(' ','_',fname)
                newfname=re.sub(':','_',newfname)
                print(dirName+os.sep+newfname)
                newfilename=dirName+os.sep+newfname
                #如果预计改名的文件名已存在，则判定md5值，若相同则删除含空格文件，不相同则在预计名字后加"_2"
                if(os.path.isfile(newfilename)):
                    oldMd5 = calcMD5(absfilepath)
                    newMd5 = calcMD5(newfilename)
                    if (oldMd5 == newMd5):
                        os.remove(newfilename)
                    else:
                        newfilename = newfilename+"_2"
                elif(os.path.isdir(newfilename)):
                    newfilename = newfilename+"_2"
                os.renames(absfilepath,newfilename)
    if(is_space(dirName)):
        if doRename:
            dirlist.append(dirName)
        else:
            print("dir :"+dirName)

#如果命令行参数启用重命名，则执行重命名
if doRename:
    renameDir(dirlist)