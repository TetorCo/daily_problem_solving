def circularArrayRotation(a, k, queries):
    # Write your code here
    result = []
    for idx in range(len(queries)):
        if k > len(a):
            k = k % len(a)
            new_idx = (len(a) - (k - idx)) - len(a)
            result.append(a[new_idx])
        else:
            new_idx = (len(a) - (k - idx)) - len(a)
            result.append(a[new_idx])

    return result