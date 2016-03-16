######################################################
#Programer: K Walter Schademan
#Date updated: 2/20/2016
#Program discription: This program is an answer to the 
#   first project euler problem.  This program finds 
#   the sum of all of the multiples of 3 and 5 below
#   a specified number
######################################################

import pylab

def euler_1(top):
    '''
    inputs:
        top = maximum value considered for suming
    outputs:
        sum = sum of all numbers below top that are mulitples of 3
        or five
    '''
    
    #define varibles
    mfive = []
    mthree = []
    mboth = []
    
    #deine win condition
    win = 0
    
    for i in range(0, top):
        
        if(i%3==0 and i%5==0):
            mboth = pylab.append(i, mboth)
            
        elif(i%3==0):
            mthree = pylab.append(i, mthree)
            
        elif(i%5==0):
            mfive = pylab.append(i, mfive)
            
    
    win = sum(mboth) + sum(mfive) + sum(mthree)
    
                            
    print win