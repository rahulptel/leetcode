from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            d = defaultdict(int)
            for k in range(len(s)):
                d[s[k]] += 1
                d[t[k]] -= 1

            for v in d.values():
                if v != 0:
                    return False

            return True
        return False
