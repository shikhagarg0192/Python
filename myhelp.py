# to convert an integer into a list
a=2
map(int,str(a))
#to concat the lists use '+'
#to know the type of anything, use type(whatever)
#to make change in a string
a = 'hello'
a = list(a)
print a
a[2:2] = ['o','y']
print a
"".join(a)
print a
#now a is a string again
#so, convert a string in a list and then make the change and convert it back to a string using join function

#make brick question logic
def make_bricks(small, big, goal):
    if (goal/5 <= big) and ((goal - 5*(goal/5))<= small): return True
    elif (goal/5 >= big) and ((goal - 5*(big)) <= small): return True
    return False
	
#for summing only unique numbers
def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  
  return sum

#make_chocolate from small and big bar and return the no. of small bars used  
def make_chocolate(small, big, goal):
    if (goal/5)<=big and goal-((goal/5)*5)<=small : return goal-((goal/5)*5)
    if (goal/5)> big and goal-(big*5)<=small : return goal-(big*5)
    return -1
   
# 'the' = 'tthhee'  
 def double_char(str):
  result = ""
  for i in range(len(str)):
    result += str[i] + str[i]
  return result
  
  #difference between max and min in a list
 def big_diff(nums):
    if len(nums)==1 : return 0
    if len(nums)==2 : return abs(nums[1]-nums[0])
    mn=min(nums[0],nums[1])
    mx=max(nums[0],nums[1])
    for i in xrange(2,len(nums)):
        mn=min(nums[i],mn)
        mx=max(nums[i],mx)
    return mx-mn

	
	def centered_average(nums):
    mn = min(nums)
    mx = max(nums)
    nums.remove(mn)
    nums.remove(mx)
    sum=0
    l= len(nums)
    for num in nums:
        sum+=num
    return sum/l
	
	def sum13(nums):
    if len(nums)==0:return 0
    sum=0
    i=0
    for i in range(len(nums)):
        if i==0:
            if nums[i]==13: continue
            else: sum+=nums[i]
        if i!=0 :
            if nums[i]==13 or nums[i-1]==13: 
                continue
            else:
                sum=sum+nums[i]
    return sum
        
		
	def sum67(nums):
  sum=0
  found6=False
  for i in xrange(len(nums)):
      if found6==True and nums[i]==7:
          found6=False
          continue
      if found6==True:continue
      if nums[i]==6:
          found6=True
          continue
      sum+=nums[i]
          
  return sum

  