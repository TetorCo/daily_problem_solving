def kangaroo(x1, v1, x2, v2):
    # Write your code here
    for i in range(10000):
        if x1 == x2:
            return "YES"
        else:
            x1 += v1
            x2 += v2
    return "NO"