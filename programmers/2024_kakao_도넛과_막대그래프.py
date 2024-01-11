def solution(edges):
    """
    정점과 각 그래프가 가지고 있는 규칙을 이용해서 풀이한다.
    정점 = 들어오는 간선 0개 / 나가는 간선 2개 이상
    막대 그래프 = 들어오는 간선 0개 / 나가는 간선 1개
    8자 그래프 = 들어오고, 나가는 간선 2개 이상
    도넛 그래프 = 나머지

    아래 사이트를 보고 풀이함.
    https://velog.io/@carrotcookie/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8F%84%EB%84%9B%EA%B3%BC-%EB%A7%89%EB%8C%80-%EA%B7%B8%EB%9E%98%ED%94%84
    """

    answer = [0, 0, 0, 0]
    graph = {}

    for edge in edges:
        if not graph.get(edge[0]):
            graph[edge[0]] = [0, 0]
        if not graph.get(edge[1]):
            graph[edge[1]] = [0, 0]

        graph[edge[0]][0] += 1  ## edge[0]이 다른 정점으로 나가는 선의 개수
        graph[edge[1]][1] += 1  ## edge[1]이 다른 정좀으로부터 들어오는 선의 개수

    for idx in graph:
        out_line = graph[idx][0]
        in_line = graph[idx][1]
        
        if out_line >= 2 and in_line == 0:  ## 정점
            answer[0] = idx
        elif out_line == 0 and in_line > 0:  ## 막대 그래프
            answer[2] += 1
        elif out_line >= 2 and in_line >= 2:  ## 8자 그래프
            answer[3] += 1

    ### 정점은 그래프 개수에 포함되지 않으니 제외
    answer[1] = graph[answer[0]][0] - answer[2] - answer[3]

    return answer