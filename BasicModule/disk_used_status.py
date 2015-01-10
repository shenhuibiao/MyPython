#!/usr/bin/python
# -*- coding: utf-8 -*-

#磁盘利用率

import os

def disk_stat():
    hd={}
    disk = os.statvfs("/")
    hd['available'] = disk.f_bsize * disk.f_bavail/(1024*1024*1024)
    hd['capacity'] = disk.f_bsize * disk.f_blocks/(1024*1024*1024)
	hd['used'] = hd['capacity'] - hd['available']
    #hd['used'] = disk.f_bsize * disk.f_bfree/(1024*1024*1024)
    return hd

print disk_stat()

##available这里表示可用的空间单位是G
##capacity表示总共的空间  单位是G
##used是hd['capacity'] - hd['available']
##这里的结果和df有点区别  原因：f_bsize为1块的大小  1块为4k即4096个字节，df最后除以的是/1024*1000

