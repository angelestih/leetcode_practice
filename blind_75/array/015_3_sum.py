from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result_array = []
        for i in range(len(nums)):
            if nums[i] >0:
                break 
                #all the elements are greater than zero, so no three indexes satisfy
            if i > 0 and nums[i] == nums[i-1]:
                continue
                #two consecutive elements are equal to each other, 
                #so no need to look for another triplet with same index again
            left_bound = i + 1
            right_bound = len(nums) - 1

            while left_bound < right_bound:
                #go on until the left and right bounds match
                three_sum = nums[left_bound] + nums[i] + nums[right_bound]
                if three_sum < 0:
                    #if sum is negative, we need less negative numbers
                    left_bound +=  1
                elif three_sum > 0:
                    #if sum is positive, we need lesss positive numbers
                    right_bound -= 1
                else:
                    result_array.append([nums[right_bound],nums[i],nums[left_bound]])
                    left_bound += 1
                    #no need to include same left bound element which was used already
                    while left_bound < right_bound and nums[left_bound] == nums[left_bound-1]:
                        left_bound += 1
                        #if the left bound still hasnt matched the right one, 
                        #and there are two consecutive elements that are the same,
                        #simply keep going to the next element until reaching a different one

        return result_array
