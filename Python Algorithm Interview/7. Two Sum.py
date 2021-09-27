# 1. Two Sum
# Q. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input : nums = [2,7,11,15], target = 9
# Output : [0,1]
# Output : Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input : nums = [3,2,4], target = 6
# Output : [1,2]

# Example 3:
# Input : nums = [3,3], target = 6
# Output : [0,1]

# My solution (Brute-Force = Bad solution ㅠㅡㅠ)  -> O(n^2)
# Runtime : 4148ms
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):           
            for j in range(i+1, len(nums)):           
                if nums[i] + nums[j] == target:
                    return [i, j]

# Other solution -> O(n^2) but, 'in' faster than 'double for sentense'
# Runtime : 640ms
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

# Optimal solution -> O(n) because, dictionary(hash_table) is average O(1) / worst(O(N))
# Runtime : 64ms
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
        