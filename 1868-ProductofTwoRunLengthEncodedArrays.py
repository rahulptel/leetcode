class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        sub1, sub2 = None, None
        while i < len(encoded1) or j < len(encoded2):
            if sub1 is None:
                sub1 = encoded1[i]
                i += 1
            if sub2 is None:
                sub2 = encoded2[j]
                j += 1

            
            end = min(sub1[1], sub2[1])                        
            mul = sub1[0] * sub2[0]
            if len(result) and result[-1][0] == mul:
                result[-1][1] += end
            else:
                result.append([mul, end])

            if sub1[1] > end:
                sub1 = [sub1[0], sub1[1] - end]
            else:
                sub1 = None

            if sub2[1] > end:                
                sub2 = [sub2[0], sub2[1] - end]                
            else:                
                sub2 = None

        return result
        
