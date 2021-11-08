class Solution:
    #O(n^2) two nested for loops
    def containsDuplicate1(self, nums: List[int]) -> bool:
        for i in nums:
            for j in nums:
                if i==j:
                    return True
        return False
    
    #O(n) using hashTable to check if element was previously seen
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        for i in nums:
            if i in hashTable:
                return True
            hashTable[i] = i
        return False
        