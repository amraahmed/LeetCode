# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2



class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            print("1")
            return nums.index(target)
        else:
            if nums[0] > target:
                    print("2")
                    return 0
            else:
                for i in range(len(nums)-1):
                    if nums[i] > target < nums[i+1]:
                        return i+1

        
        
sol = Solution()
print(sol.searchInsert([1,3,5,6],2))


# Runtime 58 ms Beats 53.2%
# Memory 14.7 MB Beats 35.49%