class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        mem = {}

        def check_palindrome(s, i, j):
            # Same element
            if i == j:
                return 0
            # Two elements
            if j - i == 1:
                return 0 if s[i] == s[j] else 1
            # Check memory for existing mismatch count
            if (i, j) in mem:
                return mem[(i, j)]

            # No mismatch at index (i, j)
            if s[i] == s[j]:
                mem[(i, j)] = check_palindrome(s, i+1, j-1)                
                return mem[(i, j)]
                        
            # Mismatch at index (i, j). Increase mismatch count by 1 and check other sub-arrays
            mem[(i, j)] = 1 + min(check_palindrome(s, i, j-1), check_palindrome(s, i+1, j))
            return mem[(i, j)]
        
        return check_palindrome(s, 0, len(s) - 1) <= k
        
