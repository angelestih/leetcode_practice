from typing import Counter


class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for i in range(32):
            # 1<<i will keep shifting 1 to the left 
            #so that when anded with n, the reult would nbe 1 if there was a 1 in that position i
            if (n&(1<<i) !=0):
                counter += 1

        return counter