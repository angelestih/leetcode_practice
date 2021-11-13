class Solution(object):
    def getSum(self, a, b):
        mask_32 = 0xffffffff
        sum = 0
        while b:
            #keep summing bit by bit
            binary_sum = (a^b) & mask_32
            carry = ((a&b)<<1) & mask_32
            a = binary_sum
            b = carry
        if a > 0x7fffffff:
            #check if a is bigger than 32 bits, by comparing to max number of 32 bits
            return ~(a^mask_32)

        return a