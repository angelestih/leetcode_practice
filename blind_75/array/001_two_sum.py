class Solution:
    #brute force O(n^2)
    def two_Sum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if (num1+num2 == target):
                    return [i, j]
    #follow up using hash table to get O(n) worst case to go over all elements in array once
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable= {}
        for i, num in enumerate(nums):
            if num in hashTable:
                return [hashTable[num],i]
            else:
                hashTable[target - num] = i