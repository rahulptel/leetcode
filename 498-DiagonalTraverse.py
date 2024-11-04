class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 0 or len(mat[0]) == 0:
            return []
            
        m, n = len(mat), len(mat[0])
        x, y = 0, 0
        switch = True
        result = []
        i = 0
        while i < m + n - 1:
            if i < n:
                r, c = 0, i
            else:
                r, c = i - n + 1, n - 1            

            items = []
            while c > -1 and r < m:                
                items.append(mat[r][c])
                r += 1
                c -= 1
                
            if switch:
                items.reverse()                
                switch = False
            else:                
                switch = True
            result.extend(items)

            # if x == n-1 and y == m-1:
            #     break 

            # if top_right:
            #     x, y = x + 1, y - 1
            # else:
            #     x, y = x - 1, y + 1
            # print(x, y)

            # if x == n:
            #     x = n - 1
            #     top_right = False
            # if y == -1:
            #     y = 0
            #     top_right = False
            # if x == -1:
            #     x = 0
            #     top_right = True
            # if y == m:
            #     y = m - 1
            #     top_right = True
            # print(x, y)

            # i += 1
            # if i == n:
            #     j = 1
            i += 1

        return result






        
