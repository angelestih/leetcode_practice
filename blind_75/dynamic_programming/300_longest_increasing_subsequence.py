from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #here we have an array that keeps track of the largest increasing subsequence that ends with
        # element in current_pos
        # then we simply return the max number in array memo
        #  O(n^2) runtime for nested loops
        # O(n) space complexity for array memo
        memo = [1] * (len(nums))
        for current_pos in range(1, len(nums)):
            for sooner_position in range(0,current_pos):
                if nums[current_pos] > nums[sooner_position]:
                    memo[current_pos] = max(memo[current_pos],memo[sooner_position]+1)

        return max(memo)