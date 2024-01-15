def gradingStudents(grades):
    # Write your code here
    ## 0 ~ 100 사이의 점수를 모든 학생들이 받는다.
    ## 40 미만의 점수는 미달 점수이다.
    ## 만약, 수강생 점수가 5의 배수가 아닌 경우,
    ## 수강생의 점수와 다음 5의 배수의 차가 3 미만일 경우 점수는 다음 5의 배수가 된다.
    ## 단, 40 미만의 점수는 해당되지 않는다
    
    ## 풀이 방법
    ## 1. 수강생 점수가 5의 배수인지 아닌지 체크
    ## 2. 0~100 사이의 5의 배수 리스트를 이진탐색을 활용해 수강생 점수의 다음 5의 배수를 찾는다 - 실패
    ## 2-1. 수강생 점수의 일의 자리가 1 ~ 4 범위일 때는 다음 5의 배수의 일의 자리는 5이기 때문에 그 차이만큼 수강생 점수에 더해준다. e.g. 41 -> 45 / 5 - 1 = 4 / 41 + 4 = 45 / 45 - 41 < 3 
    
    answer = []
    
    for grade in grades:
        ## 점수가 35미만이고, 5의 배수일 경우 answer에 바로 추가
        if grade < 35 or grade % 5 == 0:
            answer.append(grade)
        ## 점수가 35이상이고, 5의 배수가 아닐경우
        else:
            ## 점수를 문자형으로 변환
            string_grade = str(grade)
            
            ## 일의 자리가 5보다 작을 때
            if int(string_grade[1]) < 5:
                next_multiple = (grade+(5-int(string_grade[1])))
                if next_multiple - grade < 3:
                    answer.append(next_multiple)
                else:
                    answer.append(grade)
            ## 일의 자리가 5보다 클 때
            else:
                next_multiple = grade+(10-int(string_grade[1]))
                if next_multiple - grade < 3:
                    answer.append(next_multiple)
                else:
                    answer.append(grade)
    return answer

print(gradingStudents([73, 67]))