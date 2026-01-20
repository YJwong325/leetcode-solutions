# Author: Yuan Jie Wong
# Last Updated: 2025-05-16

def rotate(matrix):
    n = len(matrix)

    for r in range(n):
        # step 1: Transpose
        for c in range(r + 1, n): # starting from r + 1 which will iterate through the numbers in the strictly upper triangular part of the matrix
            # matrix[r][c] will be a number in the strictly upper triangular part and matrix[c][r] is a number in the strictly lower triangular part of the matrix
            # the position at matrix[c][r] is a reflection of the position at matrix[r][c] across the main diagonal
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # step 2: reflect in the center vertical line
        for c in range(n // 2): # only loop through the first half of each row to reflect
            # position at matrix[r][n - c - 1] is the reflection of the position at matrix[r][c] across the center vertical line
            matrix[r][c], matrix[r][n - c - 1] = matrix[r][n - c - 1], matrix[r][c]
