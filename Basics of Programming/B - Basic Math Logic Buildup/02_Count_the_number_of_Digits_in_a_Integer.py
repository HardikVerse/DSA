"""
Problem: Count the Number of Digits
Approach 1: Floor Division
Approach 2: Logarithm
Time Complexity:
    - Floor Division: O(log10 N)
    - Logarithm: O(1)
Space Complexity:
    - O(1)
Concepts:
    - Floor Division
    - Logarithm
    - Edge Cases (0, negative numbers)
"""


# Method 1

def len_cal(num):
    count = 0 
    while num>0:
        count += 1
        num //= 10
    return(count)

print(len_cal(434))

# TC = O(log10(N)) = O(log (n)
# SC = O(1)


# Method 2

import math

def countDigit(num):
    if num == 0:
        return 1
    else:
        num = abs(num)
        return int(math.log10(num) + 1)

print(countDigit(3231312))

# TC = O(1)
# SC = O(1)