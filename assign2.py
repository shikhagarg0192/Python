fh = open('Data/romeo.txt')
lst = list()
l = list()
for line in fh:
    line = line.rstrip()
    l = line.split()
    for word in l:
        if word not in lst:
            lst.append(word)
lst.sort()
print lst
