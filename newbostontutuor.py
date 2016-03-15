import math
#mathematical functions
print "2+2=", 2+2
print "6-3=",6-3
print "18/3=",18/3
print "8%7=",8%7
print "(pow)8**2=",8**2

#if you try -5**4 = -625 as -ve sign is taken as separate by python, so it finds out 5**4 and prepend the -ve sign with the output
#so to find -5 ** 4 write it as (-5)**4 = 625 :)

#variable assignments
x=18
print "val of x : ",x
y=18
print "val of y : ",y
print "x + y  : ", x+y
g=input("Enter a number : ") #takes integer and decimal numbers only
f=input() #just to show it can be empty also but still takes number. remember?
name = raw_input("Enter your name : ") # to input name (string)
print("Hi " + name)
print("using pow function to find 2^6 : "),pow(2,6)
print("using abs function to find abs(-2) : "),abs(-2)

#to use other mathematical functions like floor(18.7) import math is important

print "math.floor(18.7) = ",math.floor(18.7)
#also, u can put the big function name in a small variable like
a=math.sqrt
#now we can use a(4)
print "sqrt of 4  : ",a(4)

##Strings
self = 'He\'s a master of sorts' #escape chars \
self = "I said, \"hello whats up?\""

#concatenation
a = "hello "
b = "how are you"
print "concat eg : ", a+b

c = 23
print "2nd concat eg : ", a + str(c)
#or
print "2nd concat eg : ", a + `c`
#or
print "2nd concat eg : ", a + repr(c)

#sequence and lists
#indices    0      1      2      3      4
family = ['mom', 'dad', 'bro', 'sis', 'dog']

print "family list " , family
print "reading forward : ", family[0],family[1],family[2],family[3],family[4]
print "reading backward : ", family[-1],family[-2],family[-3],family[-4],family[-5]

#slicing on the lists
a = [0,1,2,3,4,5,6,7,8,9]
print a[0:9] #[0, 1, 2, 3, 4, 5, 6, 7, 8]
print a[4:10] #[4, 5, 6, 7, 8, 9]
print a[-5:-1] #print from 5 to 8
#a[-i:-j] prints from index -i to -j-1
print a[-5:] # from 5 to end
print a[:7] #from starting to index 7 i.e element value 6
print a[:] #print them all
print a[1:8:2] #alternate numbers starting from index 1 to 8 with difference 2 so, 1,3,5,7
print a[10:0:-2] # in reverse
print a[::-2] #same as above

#output till here
'''
2+2= 4
6-3= 3
18/3= 6
8%7= 1
(pow)8**2= 64
val of x :  18
val of y :  18
x + y  :  36
Enter a number : 3
2
Enter your name : dfg
Hi dfg
using pow function to find 2^6 :  64
using abs function to find abs(-2) :  2
math.floor(18.7) =  18.0
sqrt of 4  :  2.0
concat eg :  hello how are you
2nd concat eg :  hello 23
2nd concat eg :  hello 23
2nd concat eg :  hello 23
family list  ['mom', 'dad', 'bro', 'sis', 'dog']
reading forward :  mom dad bro sis dog
reading backward :  dog sis bro dad mom
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9]
[5, 6, 7, 8]
[5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 3, 5, 7]
[9, 7, 5, 3, 1]
[9, 7, 5, 3, 1]
'''

#editing sequences
print [1,2,3] + [4,5,6]
print 'shikha' + 'garg'
print 'shikha ' *10
print [1,2] * 10
name='shikha garg'
print 'k' in name
print 'r' in name
print 'u' in name

#lists
l= [4,2,6,1,5,2,63,34,33,89,8]
print len(l)
print max(l)
print min(l)
print list('shikha')
l[2] = 42 #change 6 in list to 42
print l
del l[3] #deletes l[3] i.e 1 from list

#slicing in lists
l = ['a','b','g','d','c','y','e','f']
print l
l[4:] = list('shikha') #update the list after 4th index with shikha
print l
l[4:] = list('shikhagarg')
print l

l = [7,8,9]
print l
l[1:1]=[3,3,3]  #insert the list at a pos
print l
l[1:5]=[]   #delete 3,3,3,8 from the list
#works pretty much like l[i:j] means from ith index to jth except jth element
print l

#methods
l = [21,18,30]
print l
l.append(45)
print l
l2 = ['i', 'love' , 'my', 'family']
print l2.count('my') #no. of times my is in the list
one = [1,2,3]
two = [4,5,6]
print one.extend(two) #appends two as a list again so its like 1,2,3,4,5,6
l=[1,2]
print one.append(l) #appends l as one element not as a list again : 1,2,3,4,5,6,[1,2]
print l2.index('love')
l2.insert(2,'really')
print l2
l2.pop() #pop the last element and print it too whereas del funcition only deletes it not print
print l2
l2.pop(1)
print l2
l2.insert(1,'fine')
print l2
l2.insert(1,'awesome')
print l2
l2.remove('i')
print l2
l2.reverse()
print l2

#sort and tuples
l = [6,2,3,9,1,5,0,3]
l.sort()
print l
print sorted('shikhagarg')

a=(1,2,3,4) #tuple (immutable like strings so cant be changed)
print a[2]


#strings
a = "hey there %s, how are %s"
b = ('shikha','you')
print a % b
c= ('anku','parents')
print a % c
a= a % b
print a.find('shikha') # will print 10

glue = 'f***'
print glue.join(a) #'hf***ef***yf*** f***tf***hf***ef***rf***ef*** f***sf***hf***if***kf***hf***af***,f*** f***hf***of***wf*** f***af***rf***ef*** f***yf***of***u'
a = ['hey','there','hello','fire']
print glue.join(a) #'heyf***theref***hellof***fire'

say = 'I have a CAR'
print say
print say.lower() #will show in lower case but wont update it in say
print say.replace('CAR','fridge') # will replace but  wont update

#dictionary
book = {} #key-value pairs
book = {'Dad':'Papa','Mom':'Mummy','Bro':'shivi','Sis':'Anku'}
print book['Bro']
book.clear()
print book
ages = {'Dad':'51','Mom':'45'}
print ages
copyage = ages.copy()
print copyage
print ages.has_key('Mom') #true
print ages.has_key('Mm') #false

#if statement,else,elif
a = "garg"
if a=="shikha":
    print 'yes its shikha'
elif a=="garg":
    print 'I hope its not'
else:
    print 'its not'

#nesting
thing = "animal"
animal = "cat"

if thing == "animal":
    if animal == "cat":
        print "its a cat"
    else:
        print "Animal but not a cat"
else :
    print 'I dont know what this thing is'

#comparison operators
print 9<7 #false
print 9<=9
print 9!=3
print 9!=9
print "dog" < "cat" #false
one = [21,22,23]
two = [21,22,23]
print one==two  #true
print one is two    #false : as one is pointing to different list and two to another
pizza = "pizzahut"
print 'z' in pizza #true

#And and OR
ex = 5
if ex < 3 and ex > 0 :
    print "num is between 0 and 3"
else:
    print "num is greater than 3" #"num is greater than 3"

if ex < 3 or ex > 0 :
    print "num is between 0 and 3"
else:
    print "num is greater than 3"   #"num is between 0 and 3"

#for and while loop
b=1
while b<=10 :
    print b
    b += 1

g = ['a','b','c','d','e']
print g
for alpha in g:
    print 'I want ' + alpha

#infinite loops and breaks
ages = {'Dad':'51','Mom':'45','Sis':'20'}
print ages
for items in ages:
    print items, ages[items]        #print key value pair

while 1:
    name=raw_input("Enter the name : ")
    if name=='quit' :
        break

#defining functions
def whatsup(x):
    return 'whats up ' + x

print whatsup('shikha')
def plusten(y):
    return y+10
print plusten(40)

#default parameters
def name(first='give',last='something'):
    print '%s %s' % (first,last)
print name('shikha','garg')
print name()
print name('shikha') #assumes it to be first parameter and prints shikha something
print name(last='garg') #prints give garg

#multiple parameters
def list1(*food): #treat food parameter as multiple elements
    print food
print list1('apples')
print list1('apples','mango')

def profile(name,*ages):
    print name
    print ages
print profile('shikha',42,43,54,12,36)

#parameter types
def cart(**items):  #** to convert it to a dictionary
    print items

print cart(apples=4, orange=5,peaches=6, mango=2)

def profile(first,last,*ages,**items):
    print first,last
    print ages
    print items

print profile('shikha','garg',23,45,12,67,89, banana=23, apple=34)

#tuples and parameters
def ex(a,b,c):
    return a+b*c
tuna = (5,7,3)
print ex(*tuna) #* to express you are working with tuple
#** for dictionary

def exd(**this):
    print this

bac = {'a':1,'b':2}
print exd(**bac)

#object oriented programming
'''
object is a thing that contains data and has methods. methods are functions.
e.g : bucky is the object. so how to describe bucky
bucky.smart
activies of bucky : bucky.walk()
class is a blueprint of the object
'''
class ex:
    eye = "black"
    age = 22 #first method has to be self, is a placeholder for the calling object
    def thismethod(self):
            return 'hey'
ex
exobj = ex()
print exobj.eye
print exobj.age
print exobj.thismethod()

#classes and self
class cn :
    def createname(self,name):
        self.name=name
    def displayname(self): #super methods bcoz of self
        return self.name
    def saying(self):
        print "hello %s " % self.name

cn
fcnobj = cn()
scnobj = cn()
fcnobj.createname('shikha')
scnobj.createname('garg')
fcnobj.displayname()
scnobj.displayname()
fcnobj.saying()

#subclassses and superclasses

class parent:
    var1="i am var1"
    var2="i am var2"

class child(parent):
    pass #doesn't do anything aka blank

pobj = parent()
print pobj.var1
print pobj.var2
cobj = child()
print cobj.var1 + cobj.var2

#overwrite variable on sub
class parent:
    var1="i am var1"
    var2="i am var2"

class child(parent):
    var2="no i am not"

p = parent()
c = child()
print p.var1, p.var2, c.var1, c.var2

#multiple parent classes
class mom:
    var1="mom"

class dad:
    var2="dad"

class child(mom,dad):
    var3="child"

c = child()
print c.var1,c.var2,c.var3

#constructors
class old:
    def ap(self):
        print "bellooooo"

obj = old()
print obj.ap()

class new:
    def __init__(self): #two underscores on each side
        print "bellooooo2"  #runs every time an object of this class is defined aka constructor

obj = new()

#import modules
def testmod():
    print "import module"
'''
click on save as at the location in python27 folder
then it is saved as a module
use it as import filename
import test1 (in my case)
then call the function as test1.testmod()
note: now if you need to make chnage in ur module and import the module again. not possible in the same idle screen
solution is to close the current idle window and make change in the module and import now. It will work :)
'''

#reload module
#also one more thinf can be done : var = test1.testmod
#var() will print import module

'''
now about editing the module and opening a new idle window, there is a way to make it work in same window
using reload(test1)
now it is updated version
'''

#getting module info
import math
print math.sqrt(81)
'''
dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf',
'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p',
'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
'''
#for more detailed version
'''help(math)'''

print math.__doc__
#'This module is always available.  It provides access to the\nmathematical
#functions defined by the C standard.'

#FILES
fob = open('C:\Temp\TestData01.txt','w')  #file in write mode
fob.write('hey now brown cow')
fob.close()

fob = open('C:\Temp\TestData01.txt','r')  #file in read mode
fob.read(3) #first 3 chars
fob.read() #reads the rest of the file
fob.close()

fob = open('C:\Temp\TestData01.txt','r')  #file in read mode
print fob.readline() #read first line
print fob.readlines() #reads all the lines and put those lines line by line in a list
fob.close()

fob = open('C:\Temp\TestData01.txt','w')  #file in write mode
fob.write('this is a new line\nthis is second\nthird\n')
fob.close()

fob = open('C:\Temp\TestData01.txt','r')  #file in read mode
temp = fob.readlines()
print temp
fob.close()
temp[2] = "mum i love apple\n"
print temp

fob = open('C:\Temp\TestData01.txt','w')
fob.writelines(temp)
fob.close()
#there is no writeline func only writelines






raw_input("Press<Enter> to quit")
