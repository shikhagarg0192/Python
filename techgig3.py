def maxarea(input1,input2):
    c = input1[0]
    r = input1[1]
    if len(input2) != r:
        return -1
    for  i in xrange(r):
        input2[i] = input2[i].split('#')
    if len(input2[i]) != c:
        return -1
    counts = [[0]*c for _ in xrange(r)]
    for i in reversed(xrange(r)):
        for j in reversed(xrange(c)):
            if input2[i][j]=='o':
                counts[i][j] = (1 + min(
                    counts[i][j+1],
                    counts[i+1][j],
                    counts[i+1][j+1]
                    )) if i < (r - 1) and j < (c - 1) else 1
    return max(c for rows in counts for c in rows)

a=['x#o#o#o#x#o', 'x#o#o#o#x#x', 'x#o#o#o#x#x', 'x#o#x#o#o#x']
#a=['o#o','o#o']
print maxarea([6,5],a)
