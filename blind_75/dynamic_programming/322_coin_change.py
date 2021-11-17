from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #runtime O(len(coins)*amount) from two nested loops 
        #space complexity O(amount) from memo array
        memo = [float('inf')]*(amount+1)
        memo[0] = 0
        #create array with first element equal to zero, and the rest equal to infinite
        # this way the first coin that is started in the second nested loop is always taking 
        # value equal to 1, and the rest of the elements can be adjusted accordingly

        for i in coins:
            for j in range(i, amount + 1):
                memo[j] = min(memo[j], memo[j-i] + 1)

        if memo[amount] != float('inf'):
        # this means that the last element was calculated and is achievable
            return memo[amount]
        else:
            # this means amount is not achievable
            return -1