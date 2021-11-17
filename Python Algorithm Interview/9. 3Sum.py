# 15. 3Sum
# Q. Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input : nums = [-1,0,1,2,-1,-4]
# Output : [[-1,-1,2],[-1,0,1]]
# Explanation : The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2 :
# Input : nums = []
# Output : []

# Example 3 :
# Input : nums = [0]
# Output : []

# My solution - Bruth Force O(n^3) <- Time Limit Exceeded
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp = []

        if len(nums) < 3:
            pass

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tripleit = [nums[i], nums[j], nums[k]]
                        tripleit.sort()

                        if tripleit in temp:
                            continue
                        else:
                            temp.append(tripleit)
        
        return temp

