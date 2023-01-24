# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
     s = re.sub(r'[^a-z]+', '', s.lower())
     return s == s[::-1]
     



sol = Solution()
print(sol.isPalindrome('A man, a plan, a canal: Panama'))

# Runtime 47 ms Beats 80.46%
# Memory 15.3 MB Beats 28.7%
