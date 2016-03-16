######################################################
#Programer: Scott Sellevaag and K Walter Schademan
#Date updated: 3/12/2016
#Program discription: solves the sixth project euler
#   problem.  sum square difference
######################################################


def play():
    
    array = [x for x in range(0,101)]
    total = 0
    win = 0
    diff = 0
    
    print array
    
    for x in range(0,len(array)):
        total = total + array[x]
        
    total = total**2
        
    for x in array:
        array[x] = array[x]**2
    
    print array
    
    
        
    for x in array:
        win = win + x
        
    diff=total-win
    
    print total
    print win
    print diff