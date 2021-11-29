from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [True] * len(nums)
        #O(n) spce complexity from memo array
        #O(n^2)spacetime from two nested for loops
        for i in range(1, len(nums)):
            condition = False
            for j in range(i-1, -1, -1):
                distance = i-j
                possibility_j = memo[j]
                range_jump = nums[j]
                condition = condition or (possibility_j and range_jump >= distance)

                if condition == True:
                    break
            
            memo[i] = condition
        return memo[len(nums) - 1]

print("The resuslt is : " + str(Solution().canJump([3,2,1,0,4])))