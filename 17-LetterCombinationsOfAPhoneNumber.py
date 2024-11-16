class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        l2d = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = [c for c in l2d[int(digits[0])-2]]

        i = 1
        while i < len(digits):
            _result = []

            for ch in l2d[int(digits[i]) - 2]:
                for r in result:
                    _result.append(r + ch)            
            result = _result
            
            i += 1
        return result
