# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


class Solution:
    def romanToInt(self, s: str) -> int:
        s = list(s)
        romval = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        rom = list(romval.keys())
        num = 0
        for i in range(len(s)-1):
            if rom.index(s[i]) < rom.index(s[i+1]):
                value = -romval[s[i]]
            else:
                value = romval[s[i]]
                
            num += value
        return num + romval[s[-1]]
                            
                
                
                
                
# Runtime 52 ms Beats 69.96%
#Memory 13.8 MB Beats 71.49%