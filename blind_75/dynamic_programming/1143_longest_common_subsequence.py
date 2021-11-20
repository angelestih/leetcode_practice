class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            max_string = text1
            min_string = text2
        else:
            max_string = text2
            min_string = text1

        memo = [0] * (len(min_string)+1)

        for i in range(1, len(max_string)+1):
            
            back_row_col = 0
            for j in range(1, len(min_string)+1):
                back_row = memo[j]
                
                if max_string[i-1] == min_string[j-1]:
                    memo[j] = back_row_col+1
                else:
                    memo[j] = max(memo[j-1], back_row)
                back_row_col = back_row
        return memo[len(min_string)]


print("The resuslt is : " + str(Solution().longestCommonSubsequence("abcba","abcbcba")))