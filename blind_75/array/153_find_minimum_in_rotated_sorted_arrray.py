from typing import List


class Solution:
    #this is O(log(n)) runtime since the array is being halved until the left bound equals the minimum value.
    #since there are no extra arrays, this is O(1) space complexity
    def findMin(self, nums: List[int]) -> int:
        left_bound = 0
        right_bound = len(nums)-1

        while left_bound < right_bound:
            middle = (left_bound + right_bound)//2
            if nums[middle] < nums[right_bound]:
                right_bound = middle
            else:
                left_bound = middle + 1

        return nums[left_bound]

