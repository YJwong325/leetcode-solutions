# LeetCode 22: Generate Parentheses
[Problem statement on LeetCode](https://leetcode.com/problems/generate-parentheses/)

## Approach
Given a number, `n`, we would need to generate all possible combinations of `n` parentheses pairs. Correct combinations follow the following rules:

1. Number of open parentheses must be equal to the number of closed parentheses.
2. Closed parenthesis cannot be added without a corresponding open parenthesis before it.
3. Number of open parentheses and closed parentheses cannot exceed `n`.

In order to obey the rules stated above, we need variables to keep track of each number of closed (`closedN`) and open (`openN`) parentheses. While building a valid combination, we can simplify the problem down to 2 decisions. Either we add an open parenthesis, `'('`, or a closed parenthesis, `')'`. We stop adding parentheses when the number of open (`openN`) and closed (`closedN`) parentheses are equal to `n`. These decisions can be further elaborated with the following points.

1. An open parenthesis, `'('`, can be added when `openN` is smaller than `n`.
2. A closed parenthesis, `')'`, can be added when `closedN` is smaller than `openN`.
3. Valid combination is found when `openN == closedN == n`.

### Backtracking
Since we need to consider all three decisions and a way to iterate until we reach condition number 3, we would use a backtracking algorithm to create our combinations. 

 - Backtracking allows us to visit each "branch" of decision until an end is reached and it rewinds back to the initial choice to take another "branch" and continue until all "branches" have been visited. 