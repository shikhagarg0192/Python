str1 = "Hello"
str2 = 'there'

bob = str1 + str2 
print bob

str3 = '123'

x = 1 + int(str3)
print x

print 'n' in 'fruit'
print 's' in 'shikha'

print 'hello'.upper()
print 'HELLO'.lower()

st = 'hi'
print type(st)

print dir(st) #will print all the functions st can use

#stripping whitespace
s1=" hello "
print s1.lstrip()
print s1.rstrip()
print s1.strip()

s1 = 'heelo'
print s1.startswith('h') #case sensitive
print s1.startswith('H')

data = "from a guard"
atpos = data.find('a')
print atpos
sppos = data.find('a',atpos+1)
print sppos
