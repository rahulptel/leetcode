from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, blocks = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                # Cell not empty
                if board[i][j] != ".":
                    # Check in row
                    if i in rows and board[i][j] in rows[i]:
                        return False
                    else:
                        rows[i].add(board[i][j]) 

                    # Check in col
                    if j in cols and board[i][j] in cols[j]:
                        return False
                    else:
                        cols[j].add(board[i][j]) 

                    # Check in block
                    b = int(i / 3) + 3 * int(j /3)
                    if b in blocks and board[i][j] in blocks[b]:
                        return False
                    else:
                        blocks[b].add(board[i][j])

        return True

        
