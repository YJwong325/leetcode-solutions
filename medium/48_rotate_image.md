# LeetCode 48: Rotate Image
[Problem statement on LeetCode](https://leetcode.com/problems/rotate-image/)

## Approach

Split the process of rotating the matrix in the clockwise direction by 90 degrees in 2 distinct steps. The first is to iterate through the whole matrix row by row and get the transpose of the matrix. Then, reflect the matrix about the center vertical line. 

### Transpose

The transpose of a matrix is obtained by swapping numbers in the strictly upper triangular part of the matrix with their reflected counterparts in the strictly lower triangular part of the matrix. 

For example:

$$
\begin{pmatrix}
D & A & B \\
X & D & C \\
Y & Z & D
\end{pmatrix}
$$

This is a matrix with the main diagonal filled with the value 'D'. To get the transpose of this matrix, we need to switch the numbers in the strictly upper triangular part of the matrix (A, B, C) with the numbers in the strictly lower triangular part of the matrix (X, Y, Z). Specifically, we need to switch the numbers in positions that are reflected about the main diagonal. 

$$\begin{pmatrix}
D & A & B \\
X & D & C \\
Y & Z & D
\end{pmatrix}
→
\begin{pmatrix}
D & X & Y \\
A & D & Z \\
B & C & D
\end{pmatrix}$$

## Example 1:

## Example 2:

## Possible Considerations

