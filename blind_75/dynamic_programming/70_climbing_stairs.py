from _typeshed import Self


class Solution:
    def climbStairs(self, n: int) -> int:
        #base case
        if n ==1:
            return 1
        #array for memoization
        memo = [0]*(n)
        memo[0] = 1
        memo[1] = 2
        #start at index 2 since 0 and 1 are already defined
        for i in range(2,n):
            #O(n) space because of memo array and 
            #O(n) runtime since access to array elements should be constant
            memo[i] = memo[i-1]+memo[i-2]
        
        return memo[n-1]
