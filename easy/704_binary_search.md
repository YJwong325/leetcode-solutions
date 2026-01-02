# LeetCode 704: Binary Search
[Problem statement on LeetCode](https://leetcode.com/problems/binary-search/)

## Approach
Binary search is a process that involves halving the search space every iteration to search for a target in a list of elements. It is quicker than linear search, but it does require the list of elements to be sorted. If we know that the list of elements that contains our target element is sorted, binary search is the fastest method to search for the target element. 

Binary search uses a left and right pointer, as well as a middle pointer that points to the index of the element in between the left and right pointers. the middle pointer separates the list into 2 parts. Since the list is sorted, assuming it is sorted in ascending order, the smaller list to the right of the middle pointer will have values that are all be larger than the element pointed to by the middle pointer, and to the left will be all the elements that have a smaller value. In the case of a list sorted in descending order, the same concept applies in opposite order. All values to the right of the middle will be smaller than the middle and all values to the left will be larger. 

## Example 1:

$$
\large\begin{array}{cccccccccccc|}
\textbf{[} & 3, & 12, & 25, & 33, & 41, & 57, & 68, & 74, & 92 & \textbf{]} &
\end{array}
\quad \text{Target = 57} 
$$

Given the above array, we will use binary search to find the target in the array. First, we need to initialize 2 pointers, l and r, at the beginning and end of the array respectively. 

$$
\large\begin{array}{cccccccccccc|}
\textbf{[} & 3, & 12, & 25, & 33, & 41, & 57, & 68, & 74, & 92 & \textbf{]} & \\
& \uparrow & & & & & & & & \uparrow \\
& \textit{l} & & & & & & & & \textit{r}
\end{array}
\quad \text{Target = 57} 
$$

Next, we determine the middle of the array by adding half the distance between the left and right pointers to the left pointer, using the formula `l + (r - l) // 2`. The left and right pointers hold the index of the elements they are pointing to.

$$
\large\begin{array}{cccccccccccc|}
\textbf{[} & 3, & 12, & 25, & 33, & 41, & 57, & 68, & 74, & 92 & \textbf{]} & \\
& \uparrow & & & & \uparrow & & & & \uparrow \\
& \textit{l} & & & & \textit{mid} & & & & \textit{r}
\end{array}
\quad \text{Target = 57} 
$$

This creates 2 distinct sections that contain a sequence of numbers. The right section will always be larger than all elements in the left section. The element pointed to by `mid` is compared to the target, and if it is equal, `mid` is returned.

Otherwise, we need to determine which section the target number might fall into. If the target is larger than the element at `mid`, the target would belong in the right section. Otherwise, the target would reside in the left section.

Since `57 > 41`, the target belongs to the right section and the left pointer is moved to update the search area.

$$
\large\begin{array}{cccccccccccc|}
\textbf{[} & 3, & 12, & 25, & 33, & 41, & 57, & 68, & 74, & 92 & \textbf{]} & \\
& & & & & \uparrow & \uparrow & & & \uparrow \\
& & & & & \textit{mid} & \textit{l} & & & \textit{r}
\end{array}
\quad \text{Target = 57} 
$$

Then, the mid pointer is updated again using the same formula, `l + (r - l) // 2`.

$$
\large\begin{array}{cccccccccccc|}
\textbf{[} & 3, & 12, & 25, & 33, & 41, & 57, & 68, & 74, & 92 & \textbf{]} & \\
& & & & & & \uparrow & \uparrow & & \uparrow \\
& & & & & & \textit{l} & \textit{mid} & & \textit{r}
\end{array}
\quad \text{Target = 57} 
$$

The element pointed to by `mid` is then compared to the target again. Since `68 > 57`, the target is at the left section this time, and the right pointer is moved to update the search area.

$$
\large\begin{array}{cccccccccccc|}
\textbf{[} & 3, & 12, & 25, & 33, & 41, & 57, & 68, & 74, & 92 & \textbf{]} & \\
& & & & & & \uparrow & \uparrow & &  \\
& & & & & & \textit{l, r} & \textit{mid} & & 
\end{array}
\quad \text{Target = 57} 
$$

Then `mid` is updated using the same formula, `l + (r - l) // 2`, for the final time.

$$
\large\begin{array}{cccccccccccc|}
\textbf{[} & 3, & 12, & 25, & 33, & 41, & 57, & 68, & 74, & 92 & \textbf{]} & \\
& & & & & & \uparrow & & &  \\
& & & & & & \textit{l, r,} & & &  \\
& & & & & & \textit{mid}
\end{array}
\quad \text{Target = 57} 
$$

Finally, the element at `mid` is compared with the target. Since the element at `mid` is equal to the target, the value at `mid`, **5**, is returned. 

## Example 2:

$$
\large\begin{array}{ccccccccccccc|}
\textbf{[} & 97, & 92, & 88, & 81, & 76, & 70, & 65, & 59, & 43 & 21 & \textbf{]} &
\end{array}
\quad \text{Target = 92} 
$$

Given the above array, we will use binary search to find the target in the array. Instead of being sorted in ascending order like the first example, this array is sorted in descending order. Similar to example 1, we need to initialize 2 pointers, l and r, at the beginning and end of the array respectively.

$$
\large\begin{array}{cccccccccccc|}
\textbf{[} & 97, & 92, & 88, & 81, & 76, & 70, & 65, & 59, & 43 & 21 & \textbf{]} & \\
& \uparrow & & & & & & & & & \uparrow \\
& \textit{l} & & & & & & & & & \textit{r}
\end{array}
\quad \text{Target = 92} 
$$

Next, `mid` is calculated using the formula `l + (r - l) // 2`. 

$$
\large\begin{array}{cccccccccccc|}
\textbf{[} & 97, & 92, & 88, & 81, & 76, & 70, & 65, & 59, & 43 & 21 & \textbf{]} & \\
& \uparrow & & & & \uparrow & & & & & \uparrow \\
& \textit{l} & & & & \textit{mid} & & & & & \textit{r}
\end{array}
\quad \text{Target = 92} 
$$

Since `92 > 76`, the target belongs to the left section and the right pointer is moved to update the search area. Because the array is sorted in descending order, comparisons are opposite to those in example 1, and every element in the right section will always be smaller than the elements in the left section.

$$
\large\begin{array}{cccccccccccc|}
\textbf{[} & 97, & 92, & 88, & 81, & 76, & 70, & 65, & 59, & 43 & 21 & \textbf{]} & \\
& \uparrow & & & \uparrow & \uparrow & & & & & \\
& \textit{l} & & & \textit{r} & \textit{mid} & & & & &
\end{array}
\quad \text{Target = 92} 
$$

The right pointer is moved to update the search area.

$$
\large\begin{array}{cccccccccccc|}
\textbf{[} & 97, & 92, & 88, & 81, & 76, & 70, & 65, & 59, & 43 & 21 & \textbf{]} & \\
& \uparrow & \uparrow & & \uparrow & & & & & & \\
& \textit{l} & \textit{mid} & & \textit{r} & & & & & &
\end{array}
\quad \text{Target = 92} 
$$

Since the value at `mid` is equal to target, the value at `mid`, **1**, is returned. 

## Time Complexity
Binary search has a time complexity of $O(\log_{} {n})$, which performs extremely fast with a large number of elements. 

To calculate the time complexity of Binary Search, we need to determine the search area after every iteration. If we let $n$ be the search area, we can effectively show the search area of the list of elements after every iteration. 

$$
\begin{array}{ccccccccccc}
\large n & \rightarrow & \LARGE\frac{n}{2} & \rightarrow & \LARGE\frac{n}{4} & \rightarrow & \LARGE\frac{n}{8} & \rightarrow & \LARGE\frac{n}{16} & \rightarrow & ... \\
i = 0 & & i = 1 & & i = 2 & & i = 3 & & i = 4
\end{array}
$$

The denominators of the search area of each iteration is a product of 2 and can be written as 2 raised to the power of $k$, where $k$ is $0, 1, 2, 3, ...$ with respect to every iteration.

$$
\begin{array}{ccccccccccccc}
\LARGE\frac{n}{2^0} & \rightarrow & \LARGE\frac{n}{2^1} & \rightarrow & \LARGE\frac{n}{2^2} & \rightarrow & \LARGE\frac{n}{2^3} & \rightarrow & \LARGE\frac{n}{2^4} & \rightarrow & ... & \rightarrow & \LARGE\frac{n}{2^k} \\
i = 0 & & i = 1 & & i = 2 & & i = 3 & & i = 4 & & & & i = k
\end{array}
$$

Since time complexity is calculated as the worst case scenario, we would need to let $\frac{n}{2^k} = 1$. When the search area reaches 1, there is only 1 element left in the list, which means the target element would definitely be found in the search area given that the target is in the list.

$$
\begin{array}{ccc}
\LARGE\frac{n}{2^k} & = & 1 \\
\large n & = & \large 2^k
\end{array}
$$

Rearranging the equation gives us $n = 2^k$.

$$
\begin{array}{ccc}
\large \log_{10} n & = & \large\log_{10} {2^k}
\end{array}
$$

We then take the log of both sides to bring $k$ down as a coefficient of the log on the right hand side of the equation.

$$
\begin{array}{ccc}
\large \log_{10} n & = & \large{k}\log_{10} {2}
\end{array}
$$

In this equation, $k$ will give us the number of iterations to get to the worst case scenario where the target is not found until the search area is 1, and $n$ represents the original search area of the list of elements when `i = 0`. Given the definition of $k$, it represents the time complexity of binary search. 

$$
\begin{array}{ccc}
\large{k} & = & \frac{\large\log_{10} {n}}{\large\log_{10} {2}} 
\end{array}
$$

Solving for $k$ gives us $k = \frac{\normalsize\log_{10} {n}}{\normalsize\log_{10} {2}}$. Since we ignore all constants for time complexity, all bases of the $log$ and $\log_{10} {2}$ are ignored, giving us only $\log_{} {n}$ as the **time complexity** of **Binary Search**.

$$
\begin{array}{ccc}
\large O(\frac{\large\log_{10} {n}}{\large\log_{10} {2}}) & = & \large O(\log_{} {n})
\end{array}
$$

$$
\therefore \text{Time Complexity} = \large O(\log_{} {n})
$$