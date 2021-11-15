from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_elem = 0
        for i in range(0,len(nums)+1):
            #here we get the signature of xoring all 
            #the elements in the range including n
            missing_elem = missing_elem ^ i

        for j in nums:
            #here we get the signature of the actual elements present in the array
            missing_elem = missing_elem ^ j
        
        return missing_elem