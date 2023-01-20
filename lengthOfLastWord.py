# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        res = []
        for ele in s:
            if ele.strip():
                res.append(ele)
        return len(res[-1])
            
    
    
    
sol = Solution()
print(sol.lengthOfLastWord("Hello World "))


# Runtime 37 ms Beats 51.89%
# Memory 13.9 MB Beats 75.50%