class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j, max_errors):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                elif max_errors > 0:
                    return check_palindrome(s, i+1, j, max_errors - 1) or \
                            check_palindrome(s, i, j-1, max_errors - 1)
                else:
                    return False

            return True
                        
        i, j, max_errors = 0, len(s) - 1, 1
        return check_palindrome(s, i, j, max_errors)
