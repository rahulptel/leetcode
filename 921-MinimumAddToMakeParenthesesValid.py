class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_paren = 0
        open_required = 0

        for i in s:            
            if i == ")":
                if open_paren > 0:
                    open_paren -= 1
                else:
                    open_required += 1
            else:
                open_paren += 1
        
        return open_paren + open_required
