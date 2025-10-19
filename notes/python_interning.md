# Interning in Python

Given the code in Python  below, what would the output be? 

## Code
```python
a = 256
b = 256
c = 257
d = 257

print(a is b, c is d)
```

## Explanation
The answer is True False.

This is because of a concept called Interning in Python. 

### Interning
Interning is Python's way of reusing immutable objects, such as an integer, to be used by multiple different variables without instantiating new ones every time. The most widely used Python implementation, CPython, interns all integers between -5 and 256. Interned numbers share the same object, so any number between -5 and 256 reference the same object. 

### Interning in the example code
In the example above, `a` and `b` are both initialized with the value 256, so Python interns an object with the value 256 and both `a` and `b` refer to the same object for their values. The `is` operator compares the memory location of each variable instead of the values. Thus, `a is b` returns True. For `c` and `d`, however, their values are outside the range of -5 and 256, which is why they are not interned and a different object instance is created for each of the variables `c` and `d`. Thus, `c is d` returns False because each variable is referencing different instances of objects with different memory locations.