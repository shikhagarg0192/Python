import random
def name_to_number(name):
    if name=='rock': return 0
    elif name=='spock':return 1
    elif name=='paper': return 2
    elif name=='lizard':return 3
    elif name=='scissors':return 4
    else: pass
    
def number_to_name(num):
    if num==0: return 'rock'
    elif num==1: return 'spock'
    elif num==2: return 'paper'
    elif num==3: return 'lizard'
    elif num==4: return 'scissors'
    else: pass
    
def rpsls(pchoice):
    print ""
    print "Player chooses ",pchoice
    p_choice = name_to_number(pchoice)
    c_choice = random.randrange(0,5)
    print "Computer chooses ",number_to_name(c_choice)
    if p_choice==c_choice: print "Player and computer tie!"
    elif (p_choice-c_choice)>0 and (p_choice-c_choice)<3:
        print "Player wins!"
    elif p_choice-c_choice>0 : print "Computer wins!"
    elif p_choice-c_choice<0 and (p_choice-c_choice)%5 < 3 : print "Player wins!"
    elif p_choice-c_choice<0: print "Computer wins!"
    else: pass
    

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


