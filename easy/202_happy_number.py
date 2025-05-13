def isHappy(n):
    def sumOfDigitsSquared(n):
        sum = 0

        # go through all digits one by one from the right and adding the square to the sum
        while n != 0:
            digit = n % 10 # gets the right-most digit
            digit = digit ** 2
            sum += digit
            n = n // 10 # remove right-most digit

        return sum

    # a hash set to store seen numbers
    visited = set()

    # keep looping as long as numbers are not encountered twice
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