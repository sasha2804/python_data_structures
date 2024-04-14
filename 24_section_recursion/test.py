

def recurs(x):


    if x == 0:
        return 1 
        
    
    return x * recurs(x-1)


print(recurs(3))