def sockMerchant(n, ar):
    # Write your code here
    pairs_dict = {}
    result = 0
    
    for sock in ar:
        
        try:
            pairs_dict[sock] += 1
            
        except:
            pairs_dict[sock] = 1
            

    for key in pairs_dict:
        result += pairs_dict[key] // 2
    
    return result