def isHappy(n):
    def sumOfDigitsSquared(n):
        sum = 0

        while n != 0:
            digit = n % 10
            digit = digit ** 2
            sum += digit
            n = n // 10

        return sum

    visited = set()

    while n not in visited:
        visited.add(n)
        n = sumOfDigitsSquared(n)

        if n == 1:
            return True
        
    return False

# The original number, n
n = 7

happy = isHappy(n)

if happy:
    print("The number", n, "is happy.")
else:
    print("The number", n, "is not happy.")