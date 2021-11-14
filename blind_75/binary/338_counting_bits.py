from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        #runtime O(n) since for loop runs n iterations
        #space complexity O(n) since result_array has length n+1
        result_array = [0]* (n + 1)
        #we have to check numbers from 0 to n, thus length of array is n + 1
        for i in range(1, n+1):
            #no need to include 0 since 0 has no 1 bits
            #number of bits equal to number of bits of half the number if even
            #or same number of bits from half + 1 if number is odd
            result_array[i] = result_array[i>>1] + i % 2

        return result_array