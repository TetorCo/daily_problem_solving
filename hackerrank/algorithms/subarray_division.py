def birthday(s, d, m):
    # Write your code here
    result = []
    
    for idx in range(len(s)-m+1):
        if sum(s[idx:idx+m]) == d:
            if s[idx:idx+m] not in result:
                result.append(s[idx:idx+m])

    return len(result)