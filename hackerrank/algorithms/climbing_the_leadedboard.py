def climbingLeaderboard(ranked, player):

    ranked = sorted(set(ranked), reverse=True)  # 중복 제거 및 내림차순 정렬
    result = []

    for p in player:
        left, right = 0, len(ranked) - 1
        while left <= right:
            mid = (left + right) // 2
            if ranked[mid] == p:
                result.append(mid + 1)
                break
            elif ranked[mid] > p:
                left = mid + 1
            else:
                right = mid - 1
        else:
            result.append(left + 1)

    return result


if __name__ == "__main__":

    ranked = [100, 100, 50, 40, 40, 20, 10]
    player = [5, 25, 50, 120]
    print(climbingLeaderboard(ranked, player))


# def climbingLeaderboard(ranked, player):
#     # Write your code here
    
#     result = []
    
#     ranked = list(set(ranked))
#     ranked.sort(reverse=True)
    
#     for p in player:
#         if p > max(ranked):
#             result.append(1)
#         elif p < min(ranked):
#             result.append(len(ranked)+1)
#         else:
#             for idx in range(len(ranked)):
#                 if p > ranked[idx]:
#                     result.append(idx+1)
#                     break
#                 elif p == ranked[idx]:
#                     result.append(idx+1)
#                     break

#     print(ranked)
#     print(result)


# def climbingLeaderboard(ranked, player):

    # result = [1 for _ in range(len(player))]
    # sort_ranked = [0]
    # for idx in range(len(ranked)):
    #     if ranked[idx] not in sort_ranked:
    #         sort_ranked.append(ranked[idx])
    # ranked_len = len(sort_ranked)-1

    # for idx, p in enumerate(player):
    #     while ranked_len > -1:
    #         if p < sort_ranked[ranked_len]:
    #             result[idx] += ranked_len
    #             break
    #         ranked_len -= 1
    
    # return result

