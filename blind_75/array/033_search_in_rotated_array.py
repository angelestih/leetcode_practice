from typing import List



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_bound = 0
        right_bound = len(nums)-1

        while left_bound <= right_bound:
            middle = left_bound + (right_bound - left_bound) //2
            
            if nums[middle] == target:
                return middle
            if nums[left_bound] <= nums[middle]:
                if nums[left_bound]<= target and target < nums[middle]:
                    right_bound = middle -1
                else:
                    left_bound = middle + 1
            else:
                if nums[left_bound] > target and target >= nums[middle]:
                    left_bound = middle + 1
                else:
                    right_bound = middle - 1
        return -1
