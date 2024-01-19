def migratoryBirds(arr):
    # Write your code here
    cnt_birds_list = [0 for i in range(len(arr)+1)]  ## 주어진 arr의 새의 수 만큼의 리스트 생성
    
    for v in arr:
        cnt_birds_list[v] += 1  ## 새의 번호를 인덱스로 사용해 수 계산
        
    max_value = max(cnt_birds_list)  ## 가장 많은 새의 수
    result = []
    
    for idx, cnt_bird in enumerate(cnt_birds_list):
        if cnt_bird == max_value:
            result.append(idx)  ## max_value와 일치하는 인덱스 저장
            
    return min(result)