#! /usr/bin/env python
#coding=utf-8
import os
import sys
import urllib2


if __name__ == '__main__':
    request = urllib2.urlopen('https://raw.githubusercontent.com/vokins/simpleu/master/hosts')
    html = request.read().decode('utf-8')
    try:
        f_hosts=open("C:\Windows\System32\drivers\etc\hosts","w")
        f_hosts.write(html)
    except BaseException:
        args = [sys.executable] + sys.argv
        #os.execlp('su', 'su', '-c', ' '.join(args))
        os.execlp('sudo', 'sudo', *args)
    finally:
        f_hosts.close()
    print("Write hosts success!")