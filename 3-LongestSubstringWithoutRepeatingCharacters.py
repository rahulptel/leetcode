class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        if len(s) == 2:
            if s[0] != s[1]:
                return 2
            else:
                return 1

        i, j = 0, 1
        window = 1
        while j < len(s):
            if s[j] not in s[i:j]:
                if j - i + 1 > window:
                    window = j - i + 1
            else:
                idx = s[i:j].index(s[j])
                i += idx + 1

            j += 1

        return window        
