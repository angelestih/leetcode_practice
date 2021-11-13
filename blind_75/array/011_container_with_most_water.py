from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left_bound = 0
        right_bound = len(height)-1
        while left_bound < right_bound:
            #height of container equal to the minimum of the heights marked 
            #by the two bounds
            height_container = min(height[left_bound],height[right_bound])
            # if new area is larger than previous one found, then replace result
            result = max(result, height_container*(right_bound - left_bound))
            #if left bound corresponds to the shorter height, advance further to the right
            left_bound = left_bound + (height_container == height[left_bound])
            #if left right corresponds to the shorter height, advance further to the left
            right_bound = right_bound - (height_container == height[right_bound])

        return result