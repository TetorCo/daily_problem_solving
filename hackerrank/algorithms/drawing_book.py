def pageCount(n, p):
    # Write your code here
    page = []
    front_cnt = 0
    back_cnt = 0
    min_cnt = 0
    
    for i in range(0, n+1, 2):
        page.append([i, i+1])
    
    for idx in range(len(page)):
        if p in page[idx]:
            min_cnt = front_cnt
        else:
            front_cnt += 1
    
    for idx in range(len(page)-1, -1, -1):
        if p in page[idx]:
            min_cnt = min(back_cnt, min_cnt)
        else:
            back_cnt += 1
    
    return min_cnt