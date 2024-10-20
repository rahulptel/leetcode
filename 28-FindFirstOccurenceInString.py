class Solution:
    def strStr(self, haystack: str, needle: str) -> int:        
        if len(haystack) >= len(needle):
            i = 0
            while i <= len(haystack) - len(needle):
                if haystack[i: i+len(needle)] == needle:
                    return i
                i += 1

            
        return -1
