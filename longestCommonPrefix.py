# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, lst: list[str]) -> str:
        lst.sort(key=len, reverse=False)
        s = list(lst[0])        
        for i in lst:
            mi = min(len(i),len(s))
            for x in range(mi):
                if s[x] == i[x]:
                    pass
                else:
                    s= s[:x]
                    break
        return ''.join(s)
                    
                
        
                
                
# Runtime 28 ms Beats 96.63%
# Memory 14 MB Beats 44.41%