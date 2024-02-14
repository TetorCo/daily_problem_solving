def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    valley = 0
    
    for idx in range(len(path)):
        if path[idx] == 'D':
            sea_level -= 1
        elif path[idx] == 'U':
            sea_level += 1
            
            if sea_level == 0:
                valley += 1
                
    return valley


if __name__ == "__main__":
    print(countingValleys(8, "UDDDUDUUU"))
    # print(countingValleys(8, "DDUUDDUDUUUD"))