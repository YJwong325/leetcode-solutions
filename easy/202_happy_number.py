# Author: Yuan Jie Wong
# Last Updated: 2025-05-14

# Normal method without memoization
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

# Caching happy numbers method
cache = set() # cache all the happy numbers

def isHappy2(n):
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
    temp = set()

    # keep looping as long as numbers are not encountered twice
    while n not in visited:
        if n in cache or int(str(n)[::-1] in cache):
            cache.update(temp)
            return True
        
        visited.add(n)
        temp.add(n)
        n = sumOfDigitsSquared(n)

        if n == 1:
            cache.update(temp)
            return True
        
    return False

# Caching both happy and unhappy numbers method
happy = set() # cache all the happy numbers
unhappy = set() # cache all the unhappy numbers

def isHappy3(n):
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
    temp = set()

    # keep looping as long as numbers are not encountered twice
    while n not in visited:
        if n in happy or int(str(n)[::-1]) in happy:
            happy.update(temp)
            return True
        elif n in unhappy or int(str(n)[::-1]) in unhappy:
            unhappy.update(temp)
            return False
        
        visited.add(n)
        temp.add(n)
        n = sumOfDigitsSquared(n)

        if n == 1:
            happy.update(temp)
            return True
        
    unhappy.update(temp)
    return False

# The original number, n
n = 7

for i in range(3):
    h = isHappy3(n)

    if h:
        print("Happy cache is:", happy)
        print("The number", n, "is happy.")
    else:
        print("Unhappy cache is:", unhappy)
        print("The number", n, "is not happy.")
    
    n += 1