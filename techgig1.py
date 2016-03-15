ip1 = list('10110101101')
ip2 = list('10110101101')

i = 3
j = 4
n=0
l = len(ip1)
for fst in range(i-1,l,i):
    if(ip2[fst]==0):
        ip2[fst]='1'
    else:
        ip2[fst]='0'
for fst in range(j-1,l,j):
    if(ip2[fst]==0):
        ip2[fst]='1'
    else:
        ip2[fst]='0'

for x in range(0,l):
    if ip1[x] == ip2[x]:
        n += 1

print n
