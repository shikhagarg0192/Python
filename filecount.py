import sys


def wordcount():
    global wc,l
    n=l.split()
    wc += len(n)
    

wc = 0
f = open('Data/1.txt')
fl = f.readlines()
lc = len(fl)
for l in fl :
    wordcount()
print lc," ", wc
