# LeetCode 48: Rotate Image
[Problem statement on LeetCode](https://leetcode.com/problems/rotate-image/)

## Approach

Split the process of rotating the matrix in the clockwise direction by 90 degrees in 2 distinct steps. The first is to iterate through the whole matrix row by row and get the transpose of the matrix. Then, reflect the matrix about the center vertical line. 

### Transposition

The transpose of a matrix is obtained by swapping numbers in the strictly upper triangular part of the matrix with their reflected counterparts in the strictly lower triangular part of the matrix. 

For example:

$$
\begin{array}{c}
\textit{Original} \\
\left[\begin{array}{ccc}
D & A & B \\
X & D & C \\
Y & Z & D
\end{array}\right]
\end{array}
$$

This is a matrix with the main diagonal filled with the value 'D'. To get the transpose of this matrix, we need to switch the numbers in the strictly upper triangular part of the matrix (A, B, C) with the numbers in the strictly lower triangular part of the matrix (X, Y, Z). Specifically, we need to switch the numbers with their counterparts that are reflected about the main diagonal (X is a counterpart of A and so on).

$$
\begin{array}{ccc}
& \textit{Transpose} & \\
\left[\begin{array}{ccc}
D & A & B \\
X & D & C \\
Y & Z & D
\end{array}\right]
&
\longrightarrow
&
\left[\begin{array}{ccc}
D & X & Y \\
A & D & Z \\
B & C & D
\end{array}\right]
\end{array}
$$

### Reflection

After we have transposed the number, we need to reverse the columns of the matrix, which can be done by reflecting the numbers about the center vertical line. 

1 2 3 4

Imagine these are the columns of a matrix. We need to end up with:

1 2 3 4 → 4 3 2 1

This can be done in 2 steps by swapping the last column with the first and then column 3 with column 2.

1 2 3 4 → 4 2 3 1 → 4 3 2 1

This reflects the entire matrix about a center vertical line, which effectively reverses the columns of the matrix. Using this on the earlier matrix will result in a **final** matrix that is equivalent to rotating the **original** matrix **90 degrees clockwise**.

$$
\begin{array}{ccc}
& \textit{Reflect} & \\
\left[\begin{array}{ccc}
D & X & Y \\
A & D & Z \\
B & C & D
\end{array}\right]
&
\longrightarrow
&
\left[\begin{array}{ccc}
Y & X & D \\
Z & D & A \\
D & C & B
\end{array}\right]
\end{array}
$$

Thus,

$$
\begin{array}{ccc}
\textit{Original} & & \textit{Final} \\
\left[\begin{array}{ccc}
D & A & B \\
X & D & C \\
Y & Z & D
\end{array}\right]
&
\longrightarrow
&
\left[\begin{array}{ccc}
Y & X & D \\
Z & D & A \\
D & C & B
\end{array}\right]
\end{array}
$$

## Example 1:

## Example 2:

## Possible Considerations

