def beautifulDays(i, j, k):
    # Write your code here
    eval_num = 0
    
    for v in range(i, j+1):
        reverse_int = int(str(v)[::-1])
        
        if (abs(v - reverse_int) % k) == 0:
            eval_num += 1
            
    return eval_num


if __name__ == "__main__":
    # beautifulDays(20, 23, 6)
    print(beautifulDays(49860, 205494, 155635764))
    # a = 12345
    # print(int(str(a)[::-1]))