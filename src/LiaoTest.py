# -*- coding:utf-8 -*-
__author__ = 'sunsy3'

import os
from collections import Iterable

# print print '100 + 200 =', 100 + 200
# name = raw_input('please input your name:')
# print name
# ord('65')
# chr(65)
# print u'故宫'
# print u'ABC'.encode('utf-8')
# print 'abc'.decode('utf-8')
# ##list
# classmates = ['Michael', 'Bob', 'Tracy']
# classmates.append('Young')
# print len(classmates)
# classmates2 = ('Michael', 'Bob', 'Tracy','Blami','Young')
# #python高级特性 进行切片操作
# print classmates2[0:3]
# print classmates2[1:3]
# List = range(0,100)
# print List[:10:2]
# #python 迭代器
# #Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
# d = {'a':1,'b':2,'c':3}
# for value in d.itervalues():
#     print value
# print isinstance('abc', Iterable) # abc是否可以迭代
# print isinstance(classmates, Iterable) #list是否可以迭代
#
# for key,value in enumerate(classmates2): #转换了list成为类似java的list 有索引
#     print key,value
# # 列表生成式
# print [x*x for x in (1,2,3)]
# print [m+n for m in 'ABC' for n in 'DEF']

print [d for d in os.listdir('../.idea')]
L = ['Hello', 'World', 'IBM', 'Apple']
print [str.lower() for str in L]#转换成小写
L = ['Hello', 'World', 18, 'Apple']
print [ s.lower() if isinstance(s,basestring) else s for s in L]#转换成小写
print [ s.lower() for s in L if isinstance(s,basestring)]#x if A else c其实是一个表达式，如果A成立则为x，否则值取c。而if放后面，那是配合for循环加的判断语句。


#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
