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