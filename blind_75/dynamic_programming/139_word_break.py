from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # O(n) space complexity from memo array
        memo = [False] * (len(s) + 1)
        memo[0] = True
        #O(n^2) runtime since two nested for loops
        #lets assume the empty character is common to word dict
        #then if the substring s[0:i] is present in dictionary, lets check the rest 
        #of substrings starting from i to len(s) index
        for i in range(len(s)):
            if memo[i] == True:
                for j in range(i, len(s)):
                    if s[i:j+1] in wordDict:
                        memo[j+1] = True

        return memo[len(s)]
print("The resuslt is : " + str(Solution().wordBreak("leetcode",["leet","code"])))