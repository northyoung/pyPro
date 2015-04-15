#! /usr/bin/env python
# -.- coding=utf-8

import os
import urllib2
import binascii
import json

id3_data = {}
frame_id = ['TIT2', 'TYER', 'TRCK', 'TALB','TPE2' ,'COMM','TPE1']

#获取mp3文件的ID3信息
def getid3data(file):
    file.read(10)
    while(True):
        id3_head = file.read(4)
        if id3_head not in frame_id:
            break
        size = int(binascii.b2a_hex(file.read(4)),16)
        file.read(2) #标志位
        id3_data[id3_head] = file.read(size).strip('\x00')
    return id3_data


if __name__ == '__main__':
    file = open('D:\CloudMusic\The Chemical Brothers - Believe.mp3','rb')
    print getid3data(file)
    # print json.dumps(jsonResult, ensure_ascii=False, encoding='gbk')

