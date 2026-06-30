"""
Problem: Extract Digits in Reverse Order

Approach:
- Modulus (%)
- Floor Division (//)

Time Complexity:
- O(log10 N)

Space Complexity:
- O(1)

Concepts:
- Digit Manipulation
- Modulus (%)
- Floor Division (//)
- Edge Cases (0, Negative Numbers)
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
