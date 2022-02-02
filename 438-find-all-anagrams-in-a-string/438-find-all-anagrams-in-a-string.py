from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        p = Counter(p)
        result = []
        compare, plus_m = None, m

        for idx in range(n-m+1):
            if idx == 0:
                compare = Counter(s[:m])
            else:
                plus_m += 1
                compare = Counter(s[idx:plus_m])
            if len(p-compare) == 0:
                result.append(idx)
        return result