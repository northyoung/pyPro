#! /usr/bin/env python
# -.- coding=utf-8

import os
import urllib2
import binascii
import json
import datetime
import eyed3
import chardet
import cookielib
from eyed3.id3 import Tag
from eyed3.id3 import ID3_V1_0, ID3_V1_1, ID3_V2_3, ID3_V2_4

from bs4 import BeautifulSoup

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
    req = urllib2.Request('http://music.163.com/album?id=427271')
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Encoding','gzip, deflate')
    req.add_header('Accept-Language','zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3')
    req.add_header('Content-Type','application/x-www-form-urlencoded')
    req.add_header('Referer','http://music.163.com/')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0')
    req.add_header('Proxy-Connection','keep-alive')
    req.add_header('Cookie','usertrack=ezq0aVTdvJ4eTEC8RZWyAg==; NETEASE_WDA_UID=33293408#|#1408087419403; usertrack=ZUcIhVT1I8u/zRQJIKN7Ag==; _ntes_nnid=9d33ac46010a49c7f6fc33a33cfed3c2,1425351633975; _ntes_nuid=9d33ac46010a49c7f6fc33a33cfed3c2; vjuids=38458f2ea.14be32ef121.0.19dea6d1; vjlast=1425445679.1425618427.13; vinfo_n_f_l_n3=1daee5b686cfee08.1.1.1425445679429.1425445685632.1425618462681; JSESSIONID-WYYY=ec99c6d12da1ba3d4590024991f7a07e675df2bca6947da396a64ab53e940b9e7e7776a196db9706f05ecb86aabeb3df8e3b4c6147aad7ea497c0448d8da83100999fb9c6c5ca719214a9a0669a55d5ababf89e1263573bd00fb58ce7829712330c0fc29c422959fe7a0cdb15e12dd13168a81903c021274d3f1880bc02267dd92811180; __utma=94650624.1922532604.1423817897.1426595771.1429185751.6; __utmb=94650624.8.10.1429185751; __utmc=94650624; __utmz=94650624.1426158782.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90')

    response = urllib2.urlopen(req)
    print response.read()
    print chardet.detect(response.read())
    # soup = BeautifulSoup()
    # songList = soup.find(id="m-song-list-module")
    # print songList