def pickingNumbers(a):
    # Write your code here
    temp = [0 for _ in range(101)]
    result = 0
    max_value = 0
    
    for v in a:
        temp[v] += 1
        if v > max_value:
            max_value = v
    
    for idx in range(2, max_value+1):
        result = max(result, max(temp[idx-1] + temp[idx], temp[idx] + temp[idx+1]))
    
    return result


if __name__ == "__main__":

    # pickingNumbers([4, 6, 5, 3, 3, 1])
    pickingNumbers([98, 3, 99, 1, 97, 2])