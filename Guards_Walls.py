class Solution:
    #time complexitY O(m*n)
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Create an m x n matrix with all elements initialized to 0
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        # Mark guards and walls in the matrix
        for row, col in guards:
            matrix[row][col] = 'g'
        
        for row, col in walls:
            matrix[row][col] = 'w'

        # Mark influence of guards
        for row, col in guards:
            # Mark all cells in the guard's row to the left
            for k in range(col - 1, -1, -1):
                if matrix[row][k] in ('g', 'w'):
                    break
                matrix[row][k] = 1
            
            # Mark all cells in the guard's row to the right
            for k in range(col + 1, n):
                if matrix[row][k] in ('g', 'w'):
                    break
                matrix[row][k] = 1

            # Mark all cells in the guard's column upwards
            for j in range(row - 1, -1, -1):
                if matrix[j][col] in ('g', 'w'):
                    break
                matrix[j][col] = 1

            # Mark all cells in the guard's column downwards
            for j in range(row + 1, m):
                if matrix[j][col] in ('g', 'w'):
                    break
                matrix[j][col] = 1

        # Count unguarded cells
        counter = 0
        for row in matrix:
            for element in row:
                if element == 0:
                    counter += 1

        return counter
