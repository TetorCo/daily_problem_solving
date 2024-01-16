def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    ## s ~ t가 집의 크기
    ## apple와 orange가 나무에서 떨어졌을 때 집의 범위 안에 들어오는 개수를 계산.
    answer = [0, 0]

    for apple in apples:
        apple_fall_locate = a+apple
        if apple_fall_locate >= s and apple_fall_locate <= t:
            answer[0] += 1
    for orange in oranges:
        orange_fall_locate = b+orange
        if orange_fall_locate >= s and orange_fall_locate <= t:
            answer[1] += 1
            
    for ans in answer:
        print(ans)