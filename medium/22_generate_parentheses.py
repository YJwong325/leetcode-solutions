# Author: Yuan Jie Wong
# Last Updated: 2025-12-22

def generateParenthesis(n):
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN < n:
            stack.append('(')
            backtrack(openN + 1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(')')
            backtrack(openN, closedN + 1)
            stack.pop()
        if n == closedN == openN:
            res.append("".join(stack))

    backtrack(0, 0)
    return res

print("Different combinations generated for 3 pairs of parentheses:")
print(generateParenthesis(3))

print("\n\nDifferent combinations generated for 7 pairs of parentheses:")
print(generateParenthesis(7))