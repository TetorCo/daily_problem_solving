def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    max_cost = 0
    
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b:
                max_cost = max(keyboard + drive, max_cost)
                
    if max_cost == 0:
        max_cost = -1
        
    return max_cost