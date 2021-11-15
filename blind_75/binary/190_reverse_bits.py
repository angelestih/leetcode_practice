class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
         #O(n) runtime and scpace complexity since only 32 iterations of the for loop
        # and only one pass
        for i in range(0,32):
            #shift bit stream result to the left for next bit being added from n
            result = result << 1
            #this masks the current bits of the original number that are left with 000...01
            # thus only the LSB is left and can be added as the LSB of the stream result 
            #by using an XOR operation
            result = result ^ (n&1) 
            #this will advance one more bit to the left of the LSB of the current bits of n
            n = n>>1
        return result