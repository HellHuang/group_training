__author__ = 'fen'
#coding=utf-8
import random
list=[]
for i in range(5):
    list.append(int(random.random()*100))
print "fist list",list
print "top 3",list[:3]
for i in range(10):
    list.append((random.random()*50))
print "append list",list
list.sort()
print "soar list",list
list.sort(reverse=True)
print "decent list",list
print "max",max(list)


def sortedDictValues(dict):
    keys=dict.keys()
    keys.sort()
    return [dict[key] for key in keys]
dict={9:"9",4:"4",0:'0',5:"5"}
#print sortedDictValues(dict)


keys=dict.keys()
keys.sort(reverse=True)
l=[]
for i in keys:
    l.append(dict[i])
sort=[dict[key] for key in keys]
print sort
print l
