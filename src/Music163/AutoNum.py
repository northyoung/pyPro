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
# exp:getId3Data('D:\CloudMusic\Sabrepulse - Horizons (Remix).mp3')
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
# exp:modCdInfo('D:\CloudMusic\Sabrepulse - Horizons (Remix).mp3')
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

#向服务器发送获取专辑信息的请求
#url:请求的专辑url地址
def requestMusicInfo(url):
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Content-Type':'application/x-www-form-urlencoded',
        'Referer':'http://music.163.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Proxy-Connection':'keep-alive',
        'Cookie':'usertrack=ezq0aVTdvJ4eTEC8RZWyAg==; NETEASE_WDA_UID=33293408#|#1408087419403; usertrack=ZUcIhVT1I8u/zRQJIKN7Ag==; _ntes_nnid=9d33ac46010a49c7f6fc33a33cfed3c2,1425351633975; _ntes_nuid=9d33ac46010a49c7f6fc33a33cfed3c2; vjuids=38458f2ea.14be32ef121.0.19dea6d1; vjlast=1425445679.1425618427.13; vinfo_n_f_l_n3=1daee5b686cfee08.1.1.1425445679429.1425445685632.1425618462681; JSESSIONID-WYYY=ec99c6d12da1ba3d4590024991f7a07e675df2bca6947da396a64ab53e940b9e7e7776a196db9706f05ecb86aabeb3df8e3b4c6147aad7ea497c0448d8da83100999fb9c6c5ca719214a9a0669a55d5ababf89e1263573bd00fb58ce7829712330c0fc29c422959fe7a0cdb15e12dd13168a81903c021274d3f1880bc02267dd92811180; __utma=94650624.1922532604.1423817897.1426595771.1429185751.6; __utmb=94650624.8.10.1429185751; __utmc=94650624; __utmz=94650624.1426158782.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90'
    }
    req = urllib2.Request(url)
    req.add_header('Accept',headers['Accept'])
    req.add_header('Accept-Language',headers['Accept-Language'])
    req.add_header('Content-Type',headers['Content-Type'])
    req.add_header('Referer',headers['Referer'])
    req.add_header('User-Agent',headers['User-Agent'])
    req.add_header('Proxy-Connection',headers['Proxy-Connection'])
    req.add_header('Cookie',headers['Cookie'])
    response = urllib2.urlopen(req)
    html = response.read()
    # print html
    return html

#解析服务器返回的数据
#url:请求的专辑url地址
def getMusicInfo(url):
    outList = []
    soup = BeautifulSoup(requestMusicInfo(url))
    CdInfo = soup.find("h2","f-ff2").get_text()
    print u'专辑名称:',CdInfo
    # songListHtml = soup.find(id="m-song-list-module") #歌曲列表
    songList = soup.find("div","f-cb").findAll("span","txt")
    artistList = soup.findAll("div","text")
    for link in artistList:
        link
    print artistList
    for i in range(len(songList)):
        songName = BeautifulSoup(str(songList[i])).get_text().strip()#获取歌曲名称
        artistName = BeautifulSoup(str(artistList[i])).get_text().strip()#获取歌曲艺术家
        print u'第',str(i+1),u'首:',artistName," - ",songName
        outList.append(" - "+songName.encode('gbk'))
    return outList

#查找本地文件夹下面的音乐文件，进行匹配和名称修改
#dirName 音乐文件的下载地址
#MusicList 专辑歌曲列表 从网络获得
def getLocalFile(dirName,MusicList):
    print MusicList
    dirNameList = os.listdir(dirName)
    print dirNameList
    for count in range(len(MusicList)):
        for fileName in dirNameList:
            if MusicList[count].decode('utf-8') is fileName:
                print count,u' is ',fileName

if __name__ == '__main__':
    kid_a = 'http://music.163.com/album?id=2065424' #KID A -- radiohead

    dirName = 'F:\CloudMusic' #文件路径
    fileList = getMusicInfo(kid_a)
    getLocalFile(dirName,fileList)
