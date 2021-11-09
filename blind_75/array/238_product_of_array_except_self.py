from typing import List
class Solution:
    # O(n^2) two nested for loops
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        product = 1
        answer = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!= j:
                    product = product*nums[j]
            
            answer[i] = product
            product = 1
        
        return answer
    #O(n) runtime and O(1) space
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_incremental = 1
        product_decremental = 1
        answer = [1] * len(nums)
        
        for i in range(1, len(nums)):
            product_incremental = product_incremental*nums[i-1]
            answer[i] = answer[i] * product_incremental

        for i in range(len(nums)-2,-1,-1):
            product_decremental = product_decremental*nums[i+1]
            answer[i] = answer[i]* product_decremental
        
        return answer
