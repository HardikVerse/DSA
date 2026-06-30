"""
Problem: Extraction of Digits from an Integer

Approach:
- Extract the last digit using % 10.
- Remove the last digit using // 10.
- Use abs() to handle negative numbers.

Time Complexity: O(log10 N)
Space Complexity: O(1)
"""


def reverseExtraction(num):
    if num == 0:
        print(0)
    else:
        num = abs(num)
        while num>0:
            last_digit = num % 10
            print(last_digit)
            num //= 10                # "//" floor division

number = 7714
reverseExtraction(number)


#TC = O(log10(n))
#SC = O(1)
