# -*- coding:utf-8 -*-
__author__ = 'young'
import urllib2
import urllib
import re
import os

#进行页面匹配的正则
REG1 = '<a class="img" href="(.*)">[\s]*<img src=".*" />[\s]*</a>[\s]*</div>[\s]*<div class="text"><p>(.*)<br /></p>'
REG2 = '<a href="#" class="img imgclasstag" imggroup=".*" bigimgwidth=".*" bigimgheight=".*" bigimgsrc="(.*)">[\s]*'

# 请求的url网址获取html
def getHtml(requestUrl):
    try:
        print u'请求网址:',requestUrl
        responseHtml = urllib2.urlopen(requestUrl,timeout=50)
        return responseHtml.read()
    except Exception:
        print u'ERROR 请求网址:',requestUrl,u'失败'

# 获取页数
# def getPage():

# 对获取主页面进行剪辑
def rePage(responseHtml,reg):
    pattern = re.compile(reg)
    linkList = re.findall(pattern,responseHtml)#返回了页面图片列表
    return linkList

# 创建文件夹
def makeDir(filePage,dirName):
    try:
        fileName = filePage+dirName
        if os.path.exists(unicode(fileName,'utf-8')):
            print u'文件夹已存在：',fileName
        else:
            print u'文件夹不存在，创建文件夹:',fileName
            os.mkdir(unicode(fileName,'utf-8'))
    except Exception:
        print u'ERROR 创建文件夹失败',fileName

# 进行图片存储
def savePic(dirName,picUrl):
    try:
        if os.path.exists(unicode(dirName,'utf-8') + os.sep + os.path.basename(picUrl)):
            print u'图片已存在'
            return
        else:
            r = getHtml(picUrl)
            print u'正在写入：',dirName
            with open(unicode(dirName,'utf-8') + os.sep + os.path.basename(picUrl), "wb") as f:
                f.write(r)
            f.close()
    except Exception:
        print u'ERROR 图片存储失败'

if __name__ == '__main__':
    for i in range(1,5000):
        responseHtml = getHtml('http://sexy.faceks.com/?page='+str(i))
        # print responseHtml
        linkList = rePage(responseHtml,REG1)
        if linkList is None:
            break
        else:
            for pageUrl in linkList:
                print pageUrl[1]
                dirName = makeDir(os.getcwd(),os.sep+pageUrl[1].replace('&nbsp;',''))
                sonLinkList = rePage(getHtml(pageUrl[0]),REG2)
                for imgFile in sonLinkList:#进行图片储存
                    savePic(os.getcwd()+os.sep+pageUrl[1].replace('&nbsp;',''),imgFile)


