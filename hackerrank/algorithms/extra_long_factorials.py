def extraLongFactorials(n):
    # Write your code here
    if n == 1:
        return n
    else:
        value = extraLongFactorials(n-1)
        result = n * value
        return result
    

if __name__ == "__main__":
    print(extraLongFactorials(25))