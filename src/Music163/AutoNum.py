#! /usr/bin/env python
# -.- coding=utf-8

import os
import urllib
import binascii
import json
import datetime
import eyed3
from eyed3.id3 import Tag
from eyed3.id3 import ID3_V1_0, ID3_V1_1, ID3_V2_3, ID3_V2_4


id3_data = {}
frame_id = ['TIT2', 'TYER', 'TRCK', 'TALB','TPE2' ,'COMM','TPE1']

#获取mp3文件的ID3信息 未使用插件
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

#获取专辑所有信息
def getCdAllInfo(filename):
    audiofile = eyed3.load(filename)

#获取mp3文件的ID3信息
def getId3Data(filename):
    audiofile = eyed3.load(filename)
    print u'音乐作者'+audiofile.tag.artist
    print u'音乐名称'+audiofile.tag.title
    print u'专辑名称'+audiofile.tag.album
    print u'出品年代'+str(audiofile.tag.recording_date)
    print u'音轨号码'+str(audiofile.tag.track_num)
    print audiofile.tag.original_release_date
    print audiofile.tag.recording_date

#修改专辑的音轨号,出品年代，专辑类型
def modCdInfo(filename,num,sum):
    audiofile = eyed3.load(filename)
    audiofile.tag.track_num =(num,sum) # 音轨号码
    # audiofile.tag.release_date = "1990-10-11"
    # audiofile.tag.original_release_date = "1990-10-11"
    # audiofile.tag.encoding_date = "2002-03"
    # audiofile.tag.tagging_date = "2012-2-5"
    # audiofile.tag.recording_date = 2009
    # audiofile.tag.recording_date = 1990
    audiofile.tag.save()

if __name__ == '__main__':
    # file = open('D:\CloudMusic\The Chemical Brothers - Believe.mp3','rb')
    # getid3data(file)
    # print json.dumps(jsonResult, ensure_ascii=False, encoding='gbk')
    # getCdAllInfo('D:\CloudMusic\Sabrepulse - Horizons (Remix).mp3')
    # modCdInfo('D:\CloudMusic\Sabrepulse - Horizons (Remix).mp3')
    # getId3Data('D:\CloudMusic\Sabrepulse - Horizons (Remix).mp3')
    # modCdInfo('F:\A.R.Y. - Fried Moonlight.mp3')
    getId3Data('F:\A.R.Y. - Fried Moonlight.mp3')
    req = urllib.urlopen('http://music.163.com/#/album?id=427271')
    # print req.read()
