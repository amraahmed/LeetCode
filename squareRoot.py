# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.


import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.sqrt(x)
    
    
    
    
    
# Runtime 31 ms Beats 95.41%
# Memory 13.8 MB Beats 51.74%