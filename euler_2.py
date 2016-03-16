######################################################
#Programer: K Walter Schademan and Scott Selevagg
#Date updated: 3/12/2016
#Program discription: solves the second project euler
#   problem.  sums all of the even fibbonacci numbers
######################################################

#import libraries
import pylab

def euler_2(end):
    '''
    inputs:
        end = largest value considered for fibbonacci numbers
    outputs:
        win = sum of even fibbonacci numbers
    '''
    
    #define variables
    win = 0
    fib_1 = 1
    fib_2 = 1
    fib = fib_1 + fib_2
    
    while(fib < end):
        if(fib%2 == 0):
            win = win + fib
        fib_2 = fib_1
        fib_1 = fib
        fib = fib_1 + fib_2
        
        
        if(fib > end):
           break
        
        print fib
        
    print "win"
    print win
    