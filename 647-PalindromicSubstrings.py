class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def countPalindrome(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        for i in range(len(s)):
            res += countPalindrome(s, i, i)
            res += countPalindrome(s, i, i+1)

        return res
        
