# -*- coding: utf-8 -*-
# @Time     :2022/6/28 1:51
# @Author   :yq-Liang
# Good Luck !

import sys
import os

#get the system encoding
defEncoding=sys.getfilesystemencoding()

#convert the code to system encoding
def sysEncode(content):
    return content.encode(defEncoding).decode(defEncoding)

def runCommand(command):
    os.system(command)

def re_enterMessage(message):
    print(sysEncode("*"+message))
    print(sysEncode(u"重新输入或者按crtl+C退出程序")+os.linesep)

def getSettingFilePath(fpath):
    return fpath+os.sep+'desktop.ini'

def addCommentToFolder(fpath,comment):
    content=sysEncode(u'[.ShellClassInfo]'+os.linesep+'InfoTip=')
    #设置备注信息
    settingFilePath=getSettingFilePath(fpath)
    with open(settingFilePath,'w')as f:
        f.write(content)
        f.write(sysEncode(comment+os.linesep))

    #添加保护
    runCommand('attrib '+settingFilePath+'-s -h')
    runCommand('attrib '+fpath+'-s')

    print(u'备注成功！')

def addComment(fpath=None,comment=None):
    inputPathMsg=sysEncode(u'请输入文件夹：')
    inputCommentMsg=sysEncode(u'请输入文件夹备注：')

    #输入文件夹路径
    if(fpath==None):
        if(len(sys.argv)==1):
            fpath=input(inputPathMsg)
            fpath=fpath[1:-1]
        else:
            fpath=sys.argv[1]

    #判断路径是否存在文件夹
    while not os.path.isdir(fpath):
        print(fpath)
        re_enterMessage(u'输入文件夹不存在')
        fpath=input(inputPathMsg)

    settingFilePath=getSettingFilePath(fpath)

    #判断文件夹是否存在
    if(os.path.exists(settingFilePath)):
        #去除保护
        runCommand('atrrib '+settingFilePath+'-s -h')

    #输入文件夹备注
    if(comment==None):
        comment=input(inputCommentMsg)

    while not comment:
        re_enterMessage(u'备注不要为空')
        comment=input(inputCommentMsg)

    addCommentToFolder(fpath,comment)
if __name__=="__main__":
    addComment()