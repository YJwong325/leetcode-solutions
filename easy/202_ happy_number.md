# LeetCode 202: Happy Number
[Problem statement on LeetCode](https://leetcode.com/problems/happy-number/)

## Approach
Keep calculating the sum of the squares of all digits and check if it eventually reaches 1.
If the sum of the squares results in a number that has been reached before, then the number is not happy because the number will loop infinitely without ever reaching 1. 
If the sum reaches 1, the original number is happy. 

## Example 1:
Let the original number be 25, so n = 25

25 → ?

So the next number is,

2<sup>2</sup> + 5<sup>2</sup> = 29

25 → 29 → ?

So the next number is,

2<sup>2</sup> + 9<sup>2</sup> = 85

25 → 29 → 85 → ?

Following this pattern we will reach,

25 → 29 → 85 → <u>**89**</u> → 145 → 42 → 20 → 4 → 16 → 37 → 58 → <u>**89**</u>

Here, we can see that one of the numbers in the sequence, 89, is repeated.

Since a number is repeated, the section between the two repeating numbers in the sequence:

25 → 29 → 85 → 89 → <u>145 → 42 → 20 → 4 → 16 → 37 → 58</u> → 89

will loop infinitely and never reach 1. Thus, the original number, 25, is **not happy**.

## Example 2:
Let the original number be 7, so n = 7

7 → ?

So the next number is,

7<sup>2</sup> = 49

7 → 49 → ?

So the next number is,

4<sup>2</sup> + 9<sup>2</sup> = 97

7 → 49 → 97 → ?

Following this pattern we will reach,

7 → 49 → 97 → 130 → 10 → <u>**1**</u>

Here, we can see that the sequence eventually reaches 1 as we continue calculating the sum of the squares of each digit of every number. Thus, the original number, 7, is **happy**.

## Possible Considerations

If an original number is a happy number because its sequence leads to a 1, we can also conclude that all following numbers leading up to the 1 is also a happy number. 

Take this sequence as an example:

31 → 10 → 1 

Since the sequence ends in a 1 and does not loop infinitely, the original number, 31, is a happy number. But what about the other numbers in the sequence? 

1 will always result in a 1 when squared, so it is also a happy number.

10 → 1

10 can also be considered a happy number because its sequence also ends in a 1, even when it is not part of another sequence.

Take a longer sequence as another example:

19 → 82 → 68 → 100 → 1

If we write out the sequences of all the individual numbers from the main sequence:

82 → 68 → 100 → 1

68 → 100 → 1

100 → 1

The sequences for the numbers do not change when we evaluate each number individually. We can say that all the numbers in this sequence are happy because the sequences of all individual numbers part of this sequence will end in a 1. 

Following this distinction, we can conclude that if the original number is unhappy, all the numbers in its sequence will share the same trait. This is called a **transitive relationship**. 

We can use this fact to make the solution more efficient through a process called **memoization**.

### Memoization
Memoization is a process of caching values that have results that are already determined and simply returns the same result if the same values are encountered at a later stage. We can use memoization for the current problem by storing all the numbers in the sequence in an array when the original number is determined to be happy. If the same number is encountered again, we will just return True if the number is inside the cache array. This saves computer resources and immediately returns a result without having to compute the entire sequence of a number again and again repeatedly. 

### Same digits
To make the solution even better, we could consider using the transitive relationship for numbers consisting of the same digits as the numbers inside the sequences. 

19 → 82 → 68 → 100 → 1

Here, 82 is considered a happy number as well due to a transitive relationship with the original number. We can also say the same for 28 because the sum of the squares of their digits will result in 68, which will also eventually lead to 1.