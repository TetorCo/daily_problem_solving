from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_counter = Counter(s[:len(p)-1])
        p_counter = Counter(p)
        index = 0
        result = []
        
        for i in range(len(p)-1, len(s)):
            s_counter[s[i]] += 1
            if s_counter == p_counter:
                result.append(index)
            s_counter[s[index]] -= 1
            if s_counter[s[index]] == 0:
                del s_counter[s[index]]
            index += 1
        return result