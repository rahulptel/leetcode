class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                offset = min(i, j)
                parent_i, parent_j = i - offset, j - offset
                if matrix[parent_i][parent_j] != matrix[i][j]:
                    return False

        return True
