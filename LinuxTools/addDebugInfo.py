# coding:utf-8
'''
    这个文件主要时处理php文件，在每一个函数的最开始处添加一个输出当前文件、类、函数名到日志中的语句
    主要是不方便调试的时候分析php运行过程中的函数运行先后状况。
    后面接两个参数，第一个是要转化的原始目录，第二个是转化后存放文件的目录.
'''
__author__ = 'zhoulin'
__version__ = '20150418'


import re
import sys
import os
import shutil

initial_dir = sys.argv[1]
final_dir = sys.argv[2]

def addDebugInfo(file1,file2):
    # file = open("/home/zhoulin/sync/Dropbox/gci-zl/brs/cloudbackup/ZMC/test.php",'r')
    # Dfile = open("/home/zhoulin/sync/Dropbox/gci-zl/brs/cloudbackup/ZMC/DAlerts.php",'w')
    print("Writing:"+file2)
    file = open(file1,'r')
    Dfile = open(file2,'w')
    found = False

    while 1:
        line = file.readline()
        if not line:
            break
        if (line.find('function')>=0):
            found = True;
        if ( found ):
            if (line.strip().startswith('{')):
                line = line[0:-1]+ 'ZMC::auditlog(__FILE__.".".__CLASS__.".".__FUNCTION__)\n'
                found = False
            elif(line.strip().endswith('{')):
                line = line +'\t\tZMC::auditlog(__FILE__.".".__CLASS__.".".__FUNCTION__)\n'
                found = False

        # print line
        Dfile.write(line)

    file.close()
    Dfile.close()

for dirName,subDirList,fileList in os.walk(initial_dir):
    DdirName = final_dir+dirName[len(initial_dir):]
    print("Creating dir:"+DdirName)
    if(not os.path.isdir(DdirName)):
        os.makedirs(DdirName)
    for fname in fileList:

        file=dirName+os.sep+fname
        Dfile=DdirName+os.sep+fname
        # print("file:"+file)
        # print("Dfile:"+Dfile)
        if(fname.endswith('.php')):
            addDebugInfo(file,Dfile)
        else:
            print("Coping to:"+Dfile)
            shutil.copy(file,Dfile)