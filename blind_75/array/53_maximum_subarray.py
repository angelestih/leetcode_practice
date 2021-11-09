from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = result = nums[0]
        for i in nums[1:]:
            current_max = max(i, current_max+i)
            result = max(current_max, result)

        return result