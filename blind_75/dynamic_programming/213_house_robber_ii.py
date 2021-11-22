from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_i(nums):
            #O(len(nums)) space complexity from memo array
            #O(len(nums)) runtime complexity from for loop
            if len(nums) == 1:
                return nums[0]
    
            memo = [0] * (len(nums))
            memo[0] = nums[0]
            memo[1] = max(memo[0], nums[1])

            
            for i in range(2, len(nums)):
            #here we decide whether to take the amount accumulated in the element i -1 of
            #the memo array, or we skip that one and accumulate the
            #element i -2 and the current element i of the nums array
            #thus, always tracking the largest possible accumulation until the end
                memo[i] = max(memo[i-1],memo[i-2] + nums[i])
            return memo[len(nums)-1]
        if len(nums) == 1:
            return nums[0]
        
        return max(rob_i(nums[0:-1]), rob_i(nums[1:len(nums)]))

print("The resuslt is : " + str(Solution().rob([2,5])))