# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        for i in set(nums):
            if nums.count(i) > len(nums/2):
                return i 
            
        
        
# Runtime 170 ms Beats 78.80%
# Memory 15.5 MB Beats 29.95%