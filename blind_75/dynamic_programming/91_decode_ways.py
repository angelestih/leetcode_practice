class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1 and s[0] == "0":
            #only element is 0, not mapped to any character
            return 0 
        #O(n) space from memo array
        #O(n) runtime from for loop
        memo = [0]*(len(s)+1)
        memo[0] = 1 #for the case where the first two numbers in s are valid, so add 1
        if s[0] == "0":
            memo[1] = 0
        else:
            memo[1] = 1

        for i in range(2,len(s)+1):
            if 1 <= int(s[i-1:i]) <= 9:
                memo[i] = memo[i] + memo[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                memo[i] = memo[i] + memo[i-2]
        return memo[len(s)]

print("The resuslt is : " + str(Solution().numDecodings("255")))