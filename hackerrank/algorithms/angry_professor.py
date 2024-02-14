def angryProfessor(k, a):
    # Write your code here
    arrive_student = 0
    for time in a:
        if time <= 0:
            arrive_student += 1
            
    if k <= arrive_student:
        return "NO"
    else:
        return "YES"