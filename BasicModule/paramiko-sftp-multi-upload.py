#!/usr/bin/python
#coding:utf-8

import paramiko
import os
import datetime
from ConfigParser import ConfigParser
##ConfigParser模块详解：http://blog.csdn.net/gexiaobaohelloworld/article/details/7976944
              
ConfigFile='config-mutiupload.ini'
config=ConfigParser()
config.read(ConfigFile)
hostname1=''.join(config.get('IP','ipaddress'))    #.join 字段分隔符
address=hostname1.split(';')
print address

username='root'
password='123456'
port=22
local_dir='/tmp/'
remote_dir='/tmp/'

if __name__=="__main__":
    for ip in address:
        t=paramiko.Transport((ip, port))
        t.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
        #files=sftp.listdir(remote_dir)
        files=os.listdir(local_dir)
        for f in files:
            print ''
            print '####################################################'
            print 'Beginning to upload file to %s host.' % ip
            print datetime.datetime.now()
            print 'Uploading file: ',os.path.join(local_dir,f)
            #sftp.get(os.path.join(remote_dir,f), os.path.join(local_dir,f))             #返回路径
            sftp.put(os.path.join(local_dir,f), os.path.join(remote_dir,f))
            print 'Upload success %s.' % datetime.datetime.now()
            print ''
        t.close()
