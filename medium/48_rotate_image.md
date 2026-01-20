# LeetCode 48: Rotate Image
[Problem statement on LeetCode](https://leetcode.com/problems/rotate-image/)

**Author:** Yuan Jie Wong  
**Last Updated:** 2026-01-01

## Approach

Split the process of rotating the matrix in the clockwise direction by 90° in 2 distinct steps. The first is to iterate through the whole matrix row by row and get the transpose of the matrix. Then, reflect the matrix about the center vertical line. 

### Transposition

The transpose of a matrix is obtained by swapping numbers in the strictly upper triangular part of the matrix with their reflected counterparts in the strictly lower triangular part of the matrix. 

For example:

$$
\begin{array}{c}
\textit{Original} \\
\left[\space\space\begin{array}{ccc}
D & A & B \\
X & D & C \\
Y & Z & D
\end{array}\space\space\right]
\end{array}
$$

This is a matrix with the main diagonal filled with the value 'D'. To get the transpose of this matrix, we need to switch the numbers in the strictly upper triangular part of the matrix (A, B, C) with the numbers in the strictly lower triangular part of the matrix (X, Y, Z). Specifically, we need to switch the numbers with their counterparts that are reflected about the main diagonal (X is a counterpart of A and so on).

$$
\begin{array}{ccc}
& \textit{Transpose} & \\
\left[\space\begin{array}{ccc}
D & A & B \\
X & D & C \\
Y & Z & D
\end{array}\space\right]
&
\longrightarrow
&
\left[\space\begin{array}{ccc}
D & X & Y \\
A & D & Z \\
B & C & D
\end{array}\space\right]
\end{array}
$$

### Reflection

After we have transposed the number, we need to reverse the columns of the matrix, which can be done by reflecting the numbers about the center vertical line. 

1 2 3 4

Imagine these are the columns of a matrix. We need to end up with:

1 2 3 4 → 4 3 2 1

This can be done in 2 steps by swapping the last column with the first and then column 3 with column 2.

1 2 3 4 → 4 2 3 1 → 4 3 2 1

This reflects the entire matrix about a center vertical line, which effectively reverses the columns of the matrix. Using this on the earlier matrix will result in a **final** matrix that is equivalent to rotating the **original** matrix **90° clockwise**.

$$
\begin{array}{ccc}
& \textit{Reflect} & \\
\left[\space\begin{array}{ccc}
D & X & Y \\
A & D & Z \\
B & C & D
\end{array}\space\right]
&
\longrightarrow
&
\left[\space\begin{array}{ccc}
Y & X & D \\
Z & D & A \\
D & C & B
\end{array}\space\right]
\end{array}
$$

Thus,

$$
\begin{array}{ccc}
\textit{Original} & & \textit{Final} \\
\left[\space\begin{array}{ccc}
D & A & B \\
X & D & C \\
Y & Z & D
\end{array}\space\right]
&
\longrightarrow
&
\left[\space\begin{array}{ccc}
Y & X & D \\
Z & D & A \\
D & C & B
\end{array}\space\right]
\end{array}
$$

## Example 1:

Let the original matrix be:

$$
\begin{array}{c}
\textit{Original} \\
\left[\space\begin{array}{cc}
1 & 27 \\
4 & 38 
\end{array}\space\right]
\end{array}
$$

We want to end up with a matrix that is equivalent to rotating the original matrix 90° clockwise. 

$$
\begin{array}{ccc}
\textit{Original} & \textit{Rotate 90°} & \textit{Final} \\
\left[\space\begin{array}{cc}
1 & 27 \\
4 & 38 
\end{array}\space\right]
&
\longrightarrow
&
\left[\space\begin{array}{cc}
4 & 1 \\
38 & 27
\end{array}\space\right]
\end{array}
$$

### Step 1: Transpose
First, we need to find the transpose of the original matrix.

$$
\begin{array}{ccc}
\textit{Original} & \textit{Transpose} & \\
\left[\space\begin{array}{ccc}
1 & 27 \\
4 & 38 
\end{array}\space\right]
&
\longrightarrow
&
\left[\space\begin{array}{ccc}
1 & 4 \\
27 & 38 
\end{array}\space\right]
\end{array}
$$

### Step 2: Reflect
Then, we need to reflect the resulting matrix after the transposition operation, which will give us the matrix that is equivalent to rotating the original matrix 90° clockwise.

$$
\begin{array}{ccc}
& \textit{Reflect} & \textit{Final} \\
\left[\space\begin{array}{ccc}
1 & 4 \\
27 & 38 
\end{array}\space\right]
&
\longrightarrow
&
\left[\space\begin{array}{ccc}
4 & 1 \\
38 & 27 
\end{array}\space\right]
\end{array}
$$

## Example 2:

We can try this approach on a larger matrix to prove that it works. Let the original matrix be:

$$
\begin{array}{c}
\textit{Original} \\
\left[\space\begin{array}{ccccc}
7 & 2 & 9 & 4 & 1 \\
3 & 8 & 6 & 0 & 5 \\
4 & 1 & 3 & 7 & 2 \\
9 & 6 & 5 & 8 & 0 \\
2 & 7 & 0 & 1 & 3
\end{array}\space\right]
\end{array}
$$

We want to end up with a matrix that is equivalent to rotating the original matrix 90° clockwise. 

$$
\begin{array}{ccc}
\textit{Original} & \textit{Rotate 90°} & \textit{Final} \\
\left[\space\begin{array}{cc}
7 & 2 & 9 & 4 & 1 \\
3 & 8 & 6 & 0 & 5 \\
4 & 1 & 3 & 7 & 2 \\
9 & 6 & 5 & 8 & 0 \\
2 & 7 & 0 & 1 & 3
\end{array}\space\right]
&
\longrightarrow
&
\left[\space\begin{array}{cc}
2 & 9 & 4 & 3 & 7 \\
7 & 6 & 1 & 8 & 2 \\
0 & 5 & 3 & 6 & 9 \\
1 & 8 & 7 & 0 & 4 \\
3 & 0 & 2 & 5 & 1
\end{array}\space\right]
\end{array}
$$

### Step 1: Transpose
First, we need to find the transpose of the original matrix.

$$
\begin{array}{ccc}
\textit{Original} & \textit{Transpose} & \\
\left[\space\begin{array}{ccc}
7 & 2 & 9 & 4 & 1 \\
3 & 8 & 6 & 0 & 5 \\
4 & 1 & 3 & 7 & 2 \\
9 & 6 & 5 & 8 & 0 \\
2 & 7 & 0 & 1 & 3
\end{array}\space\right]
&
\longrightarrow
&
\left[\space\begin{array}{ccc}
7 & 3 & 4 & 9 & 2 \\
2 & 8 & 1 & 6 & 7 \\
9 & 6 & 3 & 5 & 0 \\
4 & 0 & 7 & 8 & 1 \\
1 & 5 & 2 & 0 & 3
\end{array}\space\right]
\end{array}
$$

### Step 2: Reflect
Then, we need to reflect the resulting matrix after the transposition operation, which will give us the matrix that is equivalent to rotating the original matrix 90° clockwise.

$$
\begin{array}{ccc}
& \textit{Reflect} & \textit{Final} \\
\left[\space\begin{array}{ccc}
7 & 3 & 4 & 9 & 2 \\
2 & 8 & 1 & 6 & 7 \\
9 & 6 & 3 & 5 & 0 \\
4 & 0 & 7 & 8 & 1 \\
1 & 5 & 2 & 0 & 3
\end{array}\space\right]
&
\longrightarrow
&
\left[\space\begin{array}{ccc}
2 & 9 & 4 & 3 & 7 \\
7 & 6 & 1 & 8 & 2 \\
0 & 5 & 3 & 6 & 9 \\
1 & 8 & 7 & 0 & 4 \\
3 & 0 & 2 & 5 & 1
\end{array}\space\right]
\end{array}
$$

## Code

```python
def rotate(matrix):
    n = len(matrix)

    for r in range(n):
        # step 1: Transpose
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # step 2: reflect in the center vertical line
        for c in range(n // 2):
            matrix[r][c], matrix[r][n - c - 1] = matrix[r][n - c - 1], matrix[r][c]
```

### Step 1 notes

- The FOR loop in step 1 starts from r + 1, which will iterate through the numbers in the strictly upper triangular part of the matrix (numbers above the main diagonal). 
- matrix[r][c] $\rightarrow$ numbers above the main diagonal (strictly upper triangular part)
- matrix[c][r] $\rightarrow$ numbers below the main diagonal (strictly lower triangular part)
- the position at matrix[c][r] is a reflection of the position at matrix[r][c] across the main diagonal.

### Step 2 notes

- The FOR loop in step 2 only loops through the first half of each row starting from 0, which prevents the undoing of the reflection operation. Otherwise, if the loop iterates through the entire row, each element would be swapped twice, which would cause the numbers in the row to be swapped back to their original positions when the loop iterates through the second half of the row. 
- position at matrix[r][n - c - 1] is the reflection of the position at matrix[r][c] across the center vertical line.
- n - c - 1 is a trick to iterate in reverse order as the index c increments normally starting from 0.