class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [["_" for i in range(n)] for j in range(n)]
        self.game_over = False
        self.sign = {
            1: "x",
            2: "o"
        }

    def right_diag_check(self, player):
        for i in range(self.n):
            if self.board[i][i] != self.sign.get(player):
                return False
                
        return True
                    
    def left_diag_check(self, player):
        for i in range(self.n):
            if self.board[i][self.n - i - 1] != self.sign.get(player):
                return False
                
        return True

    def row_check(self, row, player):
        for j in range(self.n):
            if self.board[row][j] != self.sign.get(player):
                return False

        return True

    def col_check(self, col, player):
        for j in range(self.n):
            if self.board[j][col] != self.sign.get(player):
                return False

        return True

    def move(self, row: int, col: int, player: int) -> int:
        if not self.game_over:
            if self.board[row][col] == "_":
                self.board[row][col] = self.sign.get(player)
                
                if self.row_check(row, player):
                    return player

                if self.col_check(col, player):
                    return player
                
                if row == col and self.right_diag_check(player):
                    return player
                
                if row == self.n - col - 1 and self.left_diag_check(player):
                    return player
                    
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
