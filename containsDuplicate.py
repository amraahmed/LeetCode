# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
        
        
        
        
sol = Solution()
print(sol.containsDuplicate([3,3]))

# Runtime 1263 ms Beats 9.8%
# Memory 26.1 MB Beats 29.95%