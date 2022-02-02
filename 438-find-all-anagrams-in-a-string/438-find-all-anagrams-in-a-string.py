from collections import Counter

class Solution:
    ### Search Solution
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_counter = Counter(s[:len(p)-1])  # s_counter에 비교하고 싶은(p) 문자열의 -1 길이만큼 저장한다. / s='cbaebabacd', p='abc' => s_counter=Counter({c:1, b:1})
        p_counter = Counter(p)
        index = 0  # index 값을 담을 변수
        result = []
        
        for i in range(len(p)-1, len(s)):  # s_counter에 이미 담겨있는 문자열을 제외한 나머지 문자열로 반복한다. / s='cbaebabacd' => 이미 담겨있는 c,b는 제외, a부터 반복한다.
            s_counter[s[i]] += 1  # s[i] 값을 s_counter에 저장하고 값을 1 더해준다.
            if s_counter == p_counter:  # s_counter과 p_counter이 같은 지를 비교한다. / ex) s_counter=Counter({c:1, b:1, a:1}), p_counter=Counter({a:1, b:1, c:1})
                result.append(index)  # 같다면 result에 index를 삽입해준다.
            s_counter[s[index]] -= 1  # s[index] => c / s_counter[c] = 1, 이 값을 1 빼준다.
            if s_counter[s[index]] == 0:  # 만약에 지정된 값이 0이라면
                del s_counter[s[index]]  # 값을 삭제해준다.
            index += 1  # index update
        return result

# ========================================================== # 
#     ### My Solution
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#     n = len(s)
#     m = len(p)
#     p = Counter(p)
#     result = []
#     compare, plus_m = None, m

#     for idx in range(n-m+1):
#         if idx == 0:
#             compare = Counter(s[:m])
#             print(compare)
#         else:
#             plus_m += 1
#             compare = Counter(s[idx:plus_m])
#             print(compare)
#         if len(p - compare) == 0:
#             result.append(idx)
#         return result
# ============================================================ #