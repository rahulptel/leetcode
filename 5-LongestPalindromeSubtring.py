class Solution:
    def longestPalindrome(self, s: str) -> str:
        mem = [[False for j in range(len(s))] for i in range(len(s))]
        start, end = 0, 0
                
        if len(s) == 1:
            return s

        for i in range(len(s)-1):
            mem[i][i] = True
            if s[i] == s[i+1]:
                mem[i][i+1] = True
                start, end = i, i+1
        mem[len(s)-1][len(s)-1] = True

        for diff in range(2, len(s)):
            for i in range(len(s)):                
                if i + diff <= len(s) - 1:
                    if s[i] == s[i+diff] and mem[i+1][i+diff-1]:
                        start, end = i, i + diff
                        mem[i][i+diff] = True
                else:
                    break
            

        return s[start: end+1]

