from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(int)
        for ss in s:
            counter[ss] += 1

        for i, ss in enumerate(s):
            if counter[ss] == 1:
                return i
                
        return -1

        
