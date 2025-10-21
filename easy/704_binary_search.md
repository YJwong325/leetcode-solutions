# LeetCode 704: Binary Search
[Problem statement on LeetCode](https://leetcode.com/problems/binary-search/)

## Approach
Binary search is a process that involves halving the search space every iteration to search for a target in a list of elements. It is quicker than linear search, but it does require the list of elements to be sorted. If we know that the list of elements that contains our target element is sorted, binary search is the fastest method to search for the target element. 

Binary search uses a left and right pointer, as well as a middle pointer that points to the index of the element in between the left and right pointers. the middle pointer separates the list into 2 parts. Since the list is sorted, assuming it is sorted in ascending order, the smaller list to the right of the middle pointer will have values that are all be larger than the element pointed to by the middle pointer, and to the left will be all the elements that have a smaller value. In the case of a list sorted in descending order, the same concept applies in opposite order. All values to the right of the middle will be smaller than the middle and all values to the left will be larger. 

## Time Complexity
Binary search has a time complexity of O(log n), which performs extremely fast with a large number of elements. 

- search area is halved every iteration so if n is the search area:
- n -> n/2 -> n/4 -> n/8 -> n/16 -> ...
- so the pattern here is that the denominator is products of 2 and can be written as 2 raised to the power of k, 
where k is 0, 1, 2, 3, ... after every respective iteration
- and time complexity is calculated as the worst case scenario so we would need to calculate n/2^k = 1 because the target element will definitely be found when the search space is 1 because that means only 1 element is left
- rearranging the equation yields us n = 2^k and taking the log of both sides yields log n = log 2^k. then we bring k down as a coefficient of the log gives log n = k log 2. and k will give us the number of iterations when it is the worst case scenario where the target is not found until the final element and the search space is 1, which also means k is the time complexity. solving for k gives us k = log n / log 2. since we ignore all constants for time complexity, log 2 is ignored giving us only log n which is the time complexity of binary search.

## Possible Considerations


Notes:
 - explain binary search time complexity calculation