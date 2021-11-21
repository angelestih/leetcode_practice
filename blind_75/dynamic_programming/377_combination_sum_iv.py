from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #runtime O(len(nums)*target) from two nested loops 
        #space complexity O(target) from memo array
        memo = [0]*(target+1)
        memo[0] = 1
        
        #go from 1 to target, at each number check
        #for all the numbers in nums, if i is larger or equal to j 
        #then this means we can add as many instances to the memo array in index i 
        #as was used in the iteration i - j

        for i in range(1,target+1):
            for j in nums:
                if i >= j:
                    memo[i] = memo[i] + memo[i-j]

        return memo[target]
      