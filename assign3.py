handle = open('Data/mark.txt')
lst = list()
dic = {}
val=''

for line in handle:
    if line.startswith('From '):
        lst = line.split()
        val= (lst[5].split(':'))[0]
        dic[val]= dic.get(val,0)+1

print dic.items()
t=dic.items()
t.sort()
for k,v in t:
    print k, v
